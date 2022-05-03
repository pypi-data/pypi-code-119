from typing import Optional, Union
import numpy as np
import csv
import json
from pathlib import Path
from collections import Sequence
import datetime as dt

from . import plot
from .utils import load_effcal, old_config
from .data import ipoly2
from . import misc


def read_data(names):
    """
    Reads a csv datafile from disk and returns it. The csv files have to contain at least two columns.

    The Ascii file is parsed so that possible headers are stripped and reading of the data is started on the first row
    containing comma separated numbers. This is a bit silly implementation, as the header can not contain commas.

    :param names:
    :return:
    """

    datas = []
    if isinstance(names, str) or isinstance(names, Path):
        names = [names]
    for histo in names:
        data = []
        print('histotoprint', histo)
        with open(histo, 'r', newline='') as fil:
            reader = csv.reader(fil)  # , dialect='excel', **fmtparams)
            for line in reader:
                if len(line) >= 2:  # right length
                    try:
                        row = [float(x) for x in line]
                        rowlen = len(row)
                        break
                    except ValueError:
                        # not yet past header
                        print('value error')
                        raise
                        #continue
                else:
                    print('Incorrect line!')
                    print(line)
                    raise
            data.append(row)
            for line in reader:
                row = [float(x) for x in line]
                if len(row) == rowlen:
                    data.append(row)

        datas.append(np.array(data))

    return datas


def read_histo(names, unpack=True):
    """
    An alias of read_data for histograms. Unpacks the histograms by default, so that missing bins in between are given
    zero count values. The bin size can be badly inferred for sparse histograms. In this case most of the data will be
    empty.

    :param names:
    :param unpack:
    :return:
    """

    if unpack:
        histo_list = []
        histos = read_data(names)
        for hist in histos:
            histo_list.append(unpack_histo(hist))
    else:
        histo_list = read_data(names)

    return histo_list


def write_histo(data, data_path: Union[str, Path]='.', name: str='spectrum', saveall=False):
    """
    Writes a histogram into a .csv file.

    :param data: Histogram as a 2-d numpy array or a tuple of 1-d arrays. First column is the left edges of bins, the
                  second column is the counts. Optional third and fourth colums are written if present
                  (for example the upper and/or lower uncertainties).
    :param data_path: A pathlib path for the target directory.
    :param name: Name of the output file. Including the .csv is not necessary.
    :param saveall: Intermediate empty bins are printed also. This will help if doing bin by bin mathematics.

    :return: nada
    """

    if isinstance(data, np.ndarray):
        histo = data
    elif isinstance(data, Sequence) and not isinstance(data, str):

        histo = np.concatenate((data[0][:data[1].shape[0], None], data[1][:, None]), axis=1)
    else:
        raise ValueError('Wrong input type in write_histo.')

    with (Path(data_path)/(Path(name).stem + '.csv')).open('w') as fil:

        for i in range(histo.shape[0]):
            if saveall:
                fil.write(', '.join([str(histo[i, x]) for x in range(histo.shape[1])]) + '\n')
            else:
                if np.any(histo[i, 1:] != 0):
                    fil.write(', '.join([str(histo[i, x]) for x in range(histo.shape[1])]) + '\n')


def write_map(data, data_path: Union[str, Path]='.', name: str='spectrum', saveall=False):
    """
    Writes a 2-d map into a .csv file.

    :param data: a tuple of Histogram bins as a tuple of 1-d numpy arrays and histogram values as a 2d array so that
                 bins give coordinates into value matrix. ((xbin, ybin), val)

    :param data_path: A pathlib path for the target directory.
    :param name: Name of the output file Including the .csv is not necessary.
    :param saveall: Intermediate empty bins are printed also. This will help if doing bin by bin mathematics. For 2d
                    data this is probably unnecessary though.

    :return: nada
    """

    with (Path(data_path)/(Path(name).stem + '.csv')).open('w') as fil:

        if isinstance(data, Sequence) and not isinstance(data, str):
            bins = data[0]
            histo = data[1]

        else:
            raise ValueError('Wrong input type in write_histo.')

        for i in range(bins[0].shape[0]-1):
             for j in range(bins[1].shape[0]-1):
                 if saveall:
                     fil.write('{}, {}, {}\n'.format(bins[0][i],
                                                     bins[1][j], histo[i, j]))
                 else:
                     if histo[i, j] != 0:
                         fil.write('{}, {}, {}\n'.format(bins[0][i],
                                                         bins[1][j], histo[i, j]))


def write_meta(config, data_path: Union[str, Path]='.', name: str='spectrum'):
    """
    Writes the configurations defining a plot into a single .json file.

    :param config:      A config dictionary containing all information about a plot.
    :param data_path:   A pathlib path for the target directory.
    :param name:        Name of the output file. Including the .json is not necessary.

    :return:            None
    """

    with (Path(data_path)/(Path(name).stem + '.json')).open('w') as fil:
        
        json.dump(misc.sanitize_for_json(config), fil, indent=0)


def unpack_histo(data: np.ndarray) -> np.ndarray:
    """
    Histograms are packed on save by removing bins containing zero counts. For histogram summing etc., though, the zero-
    event bins must be restored. Here the bin size inferred by finding the smallest delta between consecutive bins.

    This will fail if the histogram is so sparse that there are no two filled bins next to each other. Also, using this
    to data where the first column is not composed of monotonically increasing multiples of a bin_size will produce
    nonsense.

    :param data:
    :return:
    """

    low_lim = data[0, 0]
    high_lim = data[-1, 0]
    bin_width = (data[1:, 0] - data[:-1, 0]).min()
    offset = (data[0, 0]/bin_width - data[0, 0]//bin_width)*bin_width
    #bin_width = data[1, 0] - data[0, 0]
    num_bins = int(round((high_lim - low_lim)/bin_width)) + 1  # +1 to include end bin
    bins = np.linspace(low_lim, high_lim, num_bins)

    idx1 = 0
    out_histo = np.stack((bins, np.zeros_like(bins)), axis=1)

    for bin_idx, bin_val in enumerate(bins):
        if np.isclose(bin_val, data[idx1, 0], rtol=0.0001):
            out_histo[bin_idx, 1] += data[idx1, 1]
            idx1 += 1
            if idx1 == data.shape[0]:
                break

    return out_histo


def write_ascii(plot: plot.Plot, out_path:Union[str, Path], out_name: str,
                effcal: Optional[Union[str, dict]]=None, calibrate: bool=True, saveall: bool=False) -> None:

    """
    Write a given plot in ascii mode. The full setup and path information is saved along as json file with
    the same name.

    :param plot:    A limonade Plot object to be written. The Plot object is used to get access to full
                    metadata of the measurement, including data paths and time slices.
    :param path:    The output path. If None, the data path will be used.
    :param effcal:  Efficiency calibration for the measurement. Either None (for default) or a dictionary
                    containing the efficiency calibration for the given channel. It is not used for the
                    ascii write, but is stored in the metadata .json file.
    
    """
    out_path = Path(out_path)
    print('Saving histograms to disk!')

    # get full metadata. This is always
    configs = plot.get_plot_info()

    # TEMPORARY FIX
    # until config is changed from namespace to plain dictionary, we need to fix loaded config dict by expanding
    # the top level to a namespace. We'll be using limonade.utils.old_config(config) to do it.
    cfg = old_config(configs)

    # handle efficiency calibation
    if effcal is None:
        # load default effcal
        effcal = load_effcal(cfg)
    elif isinstance(effcal, str):
        # if the name of the effcal file is supplied
        effcal = load_effcal(cfg, effcal)
        
    configs['effcal'] = effcal

    histo, bins = plot.get_data(calibrate)
    #title, legend, labels = plot.get_plot_labels()

    if histo.ndim == 1:
        write_histo((bins[0], histo), data_path=out_path, name=out_name, saveall=saveall)
    else:
        write_map((bins, histo), data_path=out_path, name=out_name, saveall=saveall)
    
    write_meta(configs, data_path=out_path, name=out_name)


def write_phd(plot: plot.Plot, out_path: Union[str, Path], out_name: str,
              effcal: Optional[Union[str, dict]] = None,
              coll_start: Optional[dt.datetime] = None,
              coll_time: Optional[dt.datetime] = None,
              quantity: Optional[float]=None) -> None:
    """
    Write a given plot as a phd file. The full setup and path information is saved along as json file with
    the same name. Collection information and efficiency calibration can be supplied as input. Only 1d plots 
    can be saved in phd format.

    :param plot:        A limonade Plot object to be written. The Plot object is used to get access to full
                        metadata of the measurement, including data paths and time slices.
    :param path:        The output path. If None, the data path will be used.
    :param effcal:      Efficiency calibration for the measurement. Either None (for default) or a dictionary
                        containing the efficiency calibration for the given cannel.
    :param coll_start:  Start datetime of sample collection.
    :param coll_time:   Collection time in seconds.
    :param quantity:    The amount collected, either in kg or m^3 or 1 (default with None)

    :return:        None
    """
    
    out_path = Path(out_path)

    # get full metadata
    configs = old_config(plot.get_plot_info())

    # plot_info
    plot_info = configs.plot['plot_cfg']
    
    # check dims and get channel
    if len(plot_info['axes']) > 1:
        raise TypeError('No phd for 2d plots')
    channel = plot_info['axes'][0]['channel']

    # TEMPORARY FIX
    # until config is changed from namespace to plain dictionary, we need to fix loaded config dict by expanding
    # the top level to a namespace. We'll be using limonade.utils.old_config(config) to do it.

    # handle efficiency calibration
    if effcal is None:
        # load default effcal
        effcal = load_effcal(configs)
    elif isinstance(effcal, str):
        # if the name of the effcal file is supplied
        effcal = load_effcal(configs, effcal)

    # produce values for all input variables. 
    try:
        nbins = configs.det['histo_size']
    except KeyError:
        # default for phd is 8192
        nbins = 2**13
    histo = np.zeros((nbins,))

    # time_slice = configs['time_slice']

    # set or invent collection time and ref time. This is difficult, as it is not a part of the 
    # default metadata. We set the defaults if configuration does not exist.

    if coll_start is None:
        # check metadata for collection times. If either is missing, we will fall back to default.
        try:
            print('Checking metadata for collection info.')
            coll_start = configs.metadata[channel]['collection_start']
            print('Found collection start', coll_start, type(coll_start))
            coll_stop = configs.metadata[channel]['collection_stop']
            print('Found collection stop', coll_stop, type(coll_stop))
        except KeyError:
            print('No collection info in metadata!')
            coll_start = configs.metadata[channel]['start'] - dt.timedelta(minutes=10.)
            coll_stop = coll_start + dt.timedelta(minutes=5.)
            # update metadata
            for ch in range(len(configs.metadata)):
                configs.metadata[ch]['collection_start'] = coll_start
                configs.metadata[ch]['collection_stop'] = coll_stop
            print('Invented collection start', coll_start, type(coll_start))
            print('invented collection stop', coll_stop, type(coll_stop))
    else:
        # coll_start and coll_time given as input
        coll_stop = coll_start + dt.timedelta(seconds=coll_time)

    if not isinstance(coll_start, dt.datetime):
            raise TypeError('Coll_start has to be of type datetime!')

    if quantity is None:
        try:
            quantity = configs.metadata[channel]['quantity']
        except KeyError:
            quantity = 1.0
            # update metadata
            for ch in range(len(configs.metadata)):
                configs.metadata[ch]['quantity'] = quantity

    # The phd starts from first channel, no matter what are the threshold limits. Otherwise the calibrations
    # would not apply. Also care has to be taken to not overshoot the maximum bins of the histogram nbins.
    bin_size = plot_info['axes'][0]['bin_width']  # channels per bin in the phd
    cal = configs.cal['energy'][channel].copy()
    #roi = plot_info['axes'][0]['range']  # roi is given in calibrated units. Need to uncalibrate.

    h2, bins = plot.get_data(calibrate=False)  # in uncalibrated data the bins is channels.

    # max_ch = ipoly2(roi[1], *cal)
    max_ch = bins[0][-1]
    bin_multi = 1
    while max_ch//bin_size > nbins:  # automatically increase bin width to fit histogram within nbins
        bin_size *= 2  # next bit depth
        bin_multi += 1  # next bit depth
        print('Need to increase bin width to fit the spectrum within {} bins!'.format(nbins))
        plot_info['axes'][0]['bin_width'] = bin_size  # this is marked to the metadata, but has no effect on the plot
    print('Bin width is ', bin_size)
    #, here, obviously, we need to rebin the data if bin_multi is greater than 1
    # This makes no bloody sense!
    for step in range(bin_multi - 1):
        # The point is to sum adjacent bins together
        # Need to check if the original number of bins is odd
        t1 = h2[0::2]
        t2 = h2[1::2]
        if t1.shape[0] == t2.shape[0]:
            h2 = t1 + t2
        else:
            h2 = t1
            h2[:-1] = h2[:-1] + t2

    # phd starts from bin zero. This requires some work
    minbin = int(bins[0][0]//bin_multi)  # //bin_size)  # start bin of the data
    datamax = int(minbin + h2.shape[0])
    histo[minbin:datamax] = h2

    # make 3 fake points with the calibration function
    E_peaks = []
    for E in [20, 200, 2000]:
        peak_ch = ipoly2(E, *cal)/bin_size
        E_peaks.append((E, peak_ch, 0.01))

    R_peaks = []
    for E in [20, 200, 2000]:
        # naive resolution estimate for germanium
        F = 0.13
        Eg = 2.9e-3
        peak_w = 2.35*np.sqrt(F*Eg/E) * E
        R_peaks.append((E, peak_w, 0.01))

    P_eff = effcal['efficiency'][channel]['peakeff']

    T_eff = effcal['efficiency'][channel]['totaleff']

    
    with (out_path / (out_name + '.phd')).open('w') as fd:

        # ==============the headers==============
        # headers contain the metadata that is needed for a minimal working phd file. This is detector name and data
        # taking info such as start date/time, duration, and live time plus optional info on sample, such as
        # collection time and quantity.
        header = _phd_get_header(configs.det['name'],
                                 configs.metadata[channel]['start'],
                                 configs.metadata[channel]['total_time'],
                                 configs.metadata[channel]['live_time'],
                                 coll_start, coll_stop, quantity)
        fd.write(header)

        # ==============The setups==============
        # The setups contain calibrations for energy, peak shape, peak efficiency and total efficiency
        setups = _phd_get_setups(E_peaks, R_peaks, P_eff, T_eff)
        fd.write(setups)

        # ==============Last the beef==============
        histogram = _phd_get_histo(bins[0], histo)
        fd.write(histogram)

        fd.write('STOP\n\n\n')
    
    write_meta(misc.sanitize_for_json(configs), data_path=out_path, name=out_name)


def _phd_get_header(det_name: str, start: dt.datetime, total: float, live: float,
               coll_start: dt.datetime, coll_stop: dt.datetime, quantity: float) -> str:
    header_str = ''
    header_str += 'BEGIN IMS2.0\n'
    header_str += 'MSG_TYPE DATA\n'
    header_str += 'MSG_ID 00000000\n'
    header_str += 'DATA_TYPE SAMPLEPHD\n'
    header_str += '#Header 3\n'
    header_str += '{}   {}       P W0                FULL\n'.format(det_name, det_name)
    header_str += '12931U\n'
    header_str += 'G04_G04-2019/01/25-13:40:41_243                                 0\n'

    ref_date = coll_start + (coll_stop - coll_start)/2
    header_str += '{}\n'.format(ref_date.strftime('%Y/%m/%d %H:%M:%S'))
    header_str += '#Comment\n'

    header_str += 'A PHD from {} data\n'.format(det_name)

    header_str += '#Collection\n'
    header_str += '{} {} {}\n'.format(coll_start.strftime('%Y/%m/%d %H:%M:%S.{}').format(coll_start.microsecond // 100000),
                            coll_stop.strftime('%Y/%m/%d %H:%M:%S.{}').format(coll_stop.microsecond // 100000),
                            quantity)
    header_str += '#Acquisition\n'
    header_str += '{}\t{:.7f} {:.7f}\n'.format(start.strftime('%Y/%m/%d %H:%M:%S'),
                                               total,
                                               live)
    return header_str


def _phd_get_setups(e_peaks, r_peaks, p_eff, t_eff):
    setup_str = ''

    setup_str += '#g_Energy\n'
    for peak in e_peaks:
        setup_str += '{}   {}   {}\n'.format(*peak)

    setup_str += '#g_Resolution\n'
    for peak in r_peaks:
        setup_str += '{}   {}   {}\n'.format(*peak)

    setup_str += '#g_Efficiency\n'

    if p_eff is None:  # skip if peak efficiency is not present
        pass
    else:
        for eff in p_eff:
            setup_str += '{}   {}   {}\n'.format(eff[0], eff[1], eff[2])

    setup_str += '#TotalEff\n'

    if t_eff is None:
        pass
    else:
        for eff in t_eff:
            setup_str += '{}   {}   {}\n'.format(eff[0], eff[1], eff[2])

    return setup_str


def _phd_get_histo(bins, histo):
    nbins = histo.shape[0]
    histo_str = ''
    histo_str += '#g_Spectrum\n'

    # TODO: Find out what the 2700 means!
    histo_str += '{}   {}\n'.format(nbins, 2700)
    for row in range(1, nbins - 5, 5):
        histo_str += '{}   {}   {}   {}   {}   {}\n'.format(row,
                                                        histo[row - 1],
                                                        histo[row],
                                                        histo[row + 1],
                                                        histo[row + 2],
                                                        histo[row + 3])
    row += 5
    if row < nbins:
        histo_str += '{}   '.format(row)
        for col in range(row, nbins + 1):
            histo_str += '{}   '.format(histo[col - 1])
        histo_str += '\n'

    return histo_str