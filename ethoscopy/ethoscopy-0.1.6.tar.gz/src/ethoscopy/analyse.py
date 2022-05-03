import pandas as pd
import numpy as np 
import warnings
import copy
from math import floor

from ethoscopy.misc.rle import rle

def max_velocity_detector(data, 
                        time_window_length,
                        velocity_correction_coef = 3e-3,
                        masking_duration = 6,
                        optional_columns = 'has_interacted',
                        raw = False
                        ):
    """ 
    Max_velocity_detector is the default movement classification for real-time ethoscope experiments.
    It is benchmarked against human-generated ground truth.

    Params:
    @data = pandas dataframe, containing behavioural variables of a single animal (no id)    
    @time_window_length = int, the period of time the data is binned and sampled to 
    @velocity_correction_coef = float, a coefficient to correct the velocity data (change for different length tubes), default is 3e-3
    @masking_duration = int, number of seconds during which any movement is ignored (velocity is set to 0) after a stimulus is delivered (a.k.a. interaction), 
    for beam_cross column, default is 6
    @optional_columns = string, columns other than ['t', 'x', 'velocity'] that you want included post analysis, default is 'has_interacted'
    @raw = bool, if True the returned datafram will contain mean values per window length for all variables from the ethoscope

    returns a pandas dataframe object with columns such as 'moving' and 'beam_cross'
    """
    
    if len(data.index) < 100:
        return None

    if raw == False:
        needed_columns =  ['t', 'x','xy_dist_log10x1000']
    else:
        needed_columns = ['t', 'x', 'y', 'w', 'h', 'phi', 'xy_dist_log10x1000']

    dt = prep_data_motion_detector(data,
                                needed_columns = needed_columns,
                                time_window_length = time_window_length,
                                optional_columns = optional_columns)

    dt['deltaT'] = dt.t.diff()
    dt['dist'] = 10 ** (dt.xy_dist_log10x1000 / 1000)
    dt['velocity'] = dt.dist / velocity_correction_coef

    dt['beam_cross'] = abs(np.sign(0.5 - dt['x']).diff())
    dt['beam_cross'] = np.where(dt['beam_cross'] == 2.0, True, False)

    if 'has_interacted' not in dt.columns:
        if masking_duration > 0:
            masking_duration = 0
        dt['has_interacted'] = 0

    dt['interaction_id'] = dt['has_interacted'].cumsum()
    dt['mask'] = dt.groupby('interaction_id')['t'].apply(lambda x: pd.Series(np.where(x < (x.min() + masking_duration), True, False), index=x.index))
    dt.loc[(dt.mask == True) & (dt.interaction_id != 0), 'velocity'] = 0

    dt['beam_cross'] = dt['beam_cross'] & ~dt['mask']
    dt = dt.drop(columns = ['interaction_id', 'mask'])

    if raw == False:
        d_small = dt.groupby('t_round').agg(
        x = pd.NamedAgg(column='x', aggfunc='mean'),
        max_velocity = pd.NamedAgg(column='velocity', aggfunc='max'),
        mean_velocity = pd.NamedAgg(column='velocity', aggfunc='mean'),
        max_distance = pd.NamedAgg(column='dist', aggfunc='max'),
        mean_distance = pd.NamedAgg(column='dist', aggfunc='mean'),
        interactions = pd.NamedAgg(column='has_interacted', aggfunc='sum'),
        beam_crosses = pd.NamedAgg(column='beam_cross', aggfunc= 'sum')
        )
    else:
        d_small = dt.groupby('t_round').agg(
        x = pd.NamedAgg(column='x', aggfunc='mean'),
        y = pd.NamedAgg(column='y', aggfunc='mean'),
        w = pd.NamedAgg(column='w', aggfunc='mean'),
        h = pd.NamedAgg(column='h', aggfunc='mean'),
        phi = pd.NamedAgg(column='phi', aggfunc='mean'),
        max_velocity = pd.NamedAgg(column='velocity', aggfunc='max'),
        mean_velocity = pd.NamedAgg(column='velocity', aggfunc='mean'),
        interactions = pd.NamedAgg(column='has_interacted', aggfunc='sum'),
        beam_crosses = pd.NamedAgg(column='beam_cross', aggfunc= 'sum')
        )

    d_small['moving'] = np.where(d_small['max_velocity'] > 1, True, False)
    d_small['micro'] = np.where((d_small['max_velocity'] > 1) & (d_small['max_velocity'] < 2.5), True, False)
    d_small['walk'] = np.where(d_small['max_velocity'] > 2.5, True, False)
    d_small.rename_axis('t', inplace = True)
    d_small.reset_index(level=0, inplace=True)

    return d_small

def prep_data_motion_detector(data,
                            needed_columns,
                            time_window_length = 10,
                            optional_columns = None 
                            ):
    """ 
    This function bins all points of the time series column into a specified window.
    Also checks optional columns provided in max_velocity_detector are present.
    
    Params:
    @data = pandas dataframe, dataframe as entered into the max_velocity_detector function
    @needed_columns = string, columns to be kept and the function enacted upon
    @time_window_length = int, the period of time the data is binned and sampled to, default is 10
    @optional_columns = string, columns other than ['t', 'x', 'xy_dist_log10x1000'] that you want included post analysis, default is None
    
    returns the same object as entered into the function
    """
    
    if all(elem in data.columns.values for elem in needed_columns) is not True:
        warnings.warn('data from ethoscope should have columns named {}!'.format(needed_columns))
        exit()

    # check optional columns input are column headings
    if optional_columns != None:
    
        if isinstance(optional_columns, str):
            check_optional_columns = set(data.columns.tolist()).intersection(list([optional_columns]))
            needed_columns = list(set(list(check_optional_columns) + needed_columns)) 
        else:
            check_optional_columns = set(data.columns.tolist()).intersection(optional_columns)
            needed_columns = list(set(list(check_optional_columns) + needed_columns))

    dc = copy.deepcopy(data[needed_columns])
    dc['t_round'] = dc['t'].map(lambda t: time_window_length * floor(t / time_window_length)) 
    
    def curate_sparse_roi_data(data,
                            window = 60,
                            min_p = 20
                            ):
        """ 
        Remove rows from table when there are not enough data points per the given window

        Params:
        @data =  pandas dataframe, dataframe containing ethoscope raw data with column 't' containing time series data
        @window = int, the size of the window to search for minimum points, default is 60
        @min_p = int, the minimum number of data points needed in a given window for it not to be removed, default is 20

        returns the same object as entered into the function
        """
        data['t_w'] = data['t'].map(lambda t: window * floor(t / window))
        data['n_points'] = data.groupby(['t_w'])['t_w'].transform('count')
        data = data[data.n_points > min_p]
        data.drop(columns = ['t_w', 'n_points'], inplace = True)

        return data

    dc = curate_sparse_roi_data(dc)

    return dc

def sleep_annotation(data, 
                    time_window_length = 10,
                    min_time_immobile = 300,
                    motion_detector_FUN = max_velocity_detector,
                    masking_duration = 6
                    ):
    """ 
    This function first uses a motion classifier to decide whether an animal is moving during a given time window.
    Then, it defines sleep as contiguous immobility for a minimum duration.
    
    Params:
    @data = pandas dataframe, dataframe containing behavioural variable from many or one multiple animals
    @time_window_length = int, the period of time the data is binned and sampled to, default is 10
    @min_time_immobile = int, immobility bouts longer or equal to this value are considered as asleep, default is 300 (i.e 5 mins)
    @motion_detector_FUN = function, the function to curate raw ethoscope data into velocity measurements, default is max_velocity_detector
    @masking_duration, int, number of seconds during which any movement is ignored (velocity is set to 0) after a stimulus is delivered (a.k.a. interaction),
    for beam_cross column, default is 6

    returns a pandas dataframe containing columns 'moving' and 'asleep'
    """

    if len(data.index) < 100:
        return None
    
    d_small = motion_detector_FUN(data, time_window_length, masking_duration = masking_duration)

    if len(d_small.index) < 100:
        return None

    time_map = pd.Series(range(d_small.t.iloc[0], 
                        d_small.t.iloc[-1] + time_window_length, 
                        time_window_length
                        ), name = 't')

    missing_values = time_map[~time_map.isin(d_small['t'].tolist())]
    d_small = d_small.merge(time_map, how = 'right', on = 't', copy = False).sort_values(by=['t'])
    d_small['is_interpolated'] = np.where(d_small['t'].isin(missing_values), True, False)
    d_small['moving'] = np.where(d_small['is_interpolated'] == True, False, d_small['moving'])

    def sleep_contiguous(moving, fs, min_valid_time = 300):
        """ 
        Checks if contiguous bouts of immobility are greater than the minimum valid time given

        Params:
        @moving = pandas series, series object comtaining the movement data of individual flies
        @fs = int, sampling frequency (Hz) to scale minimum length to time in seconds
        @min_valid_time = min amount immobile time that counts as sleep, default is 300 (i.e 5 mins) 
        
        returns a list object to be added to a pandas dataframe
        """
        min_len = fs * min_valid_time
        r_sleep =  rle(np.logical_not(moving)) 
        valid_runs = r_sleep[2] >= min_len 
        r_sleep_mod = valid_runs & r_sleep[0]
        r_small = []
        for c, i in enumerate(r_sleep_mod):
            r_small += ([i] * r_sleep[2][c])

        return r_small

    d_small['asleep'] = sleep_contiguous(d_small['moving'], 1/time_window_length, min_valid_time = min_time_immobile)
    
    return d_small

def puff_mago(data, response_window = 10, velocity_correction_coef = 3e-3):
    """
    Puff_mago finds interaction times from raw ethoscope data to detect responses in a given window.
    This function will only return data from around interaction times and not whole movement data from the experiment.

    Params:
    @data = pandas dataframe, dataframe containing behavioural variable from many or one multiple animals 
    @response_window = int, the period of time (seconds) after stimulus to check for a response (movement), default is 10 seconds
    @velocity_correction_coef = float, a coefficient to correct the velocity data (change for different length tubes), default is 3e-3
    
    returns  a pandas dataframe object with columns such as 'interaction_t' and 'has_responded'
    """

    # check for has_interaction column, as is removed during loading of roi if all false
    if any('has_interacted' in ele for ele in data.columns.tolist()) is False:
        return None

    data['deltaT'] = data.t.diff()
    data['dist'] = 10 ** (data.xy_dist_log10x1000 / 1000)
    data['velocity'] = data.dist / velocity_correction_coef
    data.drop(columns = ['deltaT', 'dist'], inplace = True)

    #isolate interaction times
    interaction_dt = data['t'][(data['has_interacted'] == 1) | (data['has_interacted'] == 2)].to_frame()
    interaction_dt.rename(columns = {'t' : 'int_t'}, inplace = True)

    #check some interactions took place, return none if empty
    if len(interaction_dt.index) < 1:
        return None

    interaction_dt['start'] = interaction_dt.int_t
    interaction_dt['end'] = interaction_dt.int_t + response_window

    ints = data.t.values
    starts = interaction_dt.start.values 
    ends = interaction_dt.end.values  

    i, j = np.where((ints[:, None] >= starts) & (ints[:, None] <= ends))
    df = pd.DataFrame(
        np.column_stack([data.values[i], interaction_dt.values[j]]),
        columns= data.columns.append(interaction_dt.columns)
    )
    df['t_rel'] = df.t - df.int_t
    df.rename(columns = {'int_t' : 'interaction_t'}, inplace = True)
    df['has_responded'] = np.where((df['t_rel'] > 0) & (df['velocity'] > 1), True, False)
    df['has_walked'] = np.where((df['t_rel'] > 0) & (df['velocity'] > 2.5), True, False)
    df.drop(columns = ['xy_dist_log10x1000', 'start', 'end'], inplace = True)
    
    # filter by response_window ahead of interaction time and find any postive response, return new df with only interaction time == 0 rows with response
    df['t'] = np.floor(df['t'])
    start_list = np.floor(interaction_dt['int_t'].to_numpy()).astype(int)
    end_list = start_list + response_window

    response_df = pd.DataFrame()

    for i,q in zip(start_list, end_list):

        ls = list(range(i, q+1))
        boolean_series = df.t.isin(ls)
        filtered_df = df[boolean_series]

        if any(filtered_df['has_responded']):
            # response_row = filtered_df[filtered_df['has_responded'] == True].iloc[0]
            # interaction_id = filtered_df[filtered_df['t_rel'] == 0]['has_interacted'].tolist()
            # response_row['has_interacted'] = interaction_id[0]
            # for when you want the data from when the movement occured
            response_row = filtered_df[filtered_df['t_rel'] == 0]
            response_row['has_responded'] = True
            trel_row = filtered_df[filtered_df['has_responded'] == True].iloc[0]
            response_row['t_rel'] = trel_row['t_rel']
            response_df = response_df.append(response_row)
        else:
            response_df = response_df.append(filtered_df[filtered_df['t_rel'] == 0])

    return response_df

def find_motifs(data, window = 300, velocity_correction_coef = 3e-3):
    """
    Find_motifs is a modification of puff_mago. It only takes data with a populated has_interacted column.
    The function will take a response window (in seconds) to find the variables recorded by the ethoscope in this window prior to an 
    interaction taking place. Each run is given a unique ID per fly, however it is not unique to other flies. To do so, combine the 
    fly ID with run ID after.

    Params:
    @data = pandas dataframe, dataframe containing behavioural variable from many or one multiple animals 
    @window = int, the period of time (seconds) prior to the stimulus you want data retrieved for, default is 300
    @velocity_correction_coef = float, a coefficient to correct the velocity data (change for different length tubes), default is 3e-3
    
    returns  a pandas dataframe object with columns such as 't_count' and 'has_responded'
    """

    # check for has_interaction column, will be moved in prior download if all interactions are false
    if any('has_interacted' in ele for ele in data.columns.tolist()) is False:
        return None

    data['deltaT'] = data.t.diff()
    data['dist'] = 10 ** (data.xy_dist_log10x1000 / 1000)
    data['velocity'] = data.dist / velocity_correction_coef
    data.drop(columns = ['deltaT', 'dist'], inplace = True)

    #isolate interaction times
    interaction_dt = data['t'][data['has_interacted'] == 1].to_frame()
    interaction_dt.rename(columns = {'t' : 'int_t'}, inplace = True)

    #check some interactions took place, return none if empty
    if len(interaction_dt.index) < 1:
        return None

    interaction_dt['start'] = interaction_dt.int_t - window
    interaction_dt['end'] = interaction_dt.int_t + 10

    ints = data.t.values
    starts = interaction_dt.start.values 
    ends = interaction_dt.end.values  

    i, j = np.where((ints[:, None] >= starts) & (ints[:, None] <= ends))
    df = pd.DataFrame(
        np.column_stack([data.values[i], interaction_dt.values[j]]),
        columns = data.columns.append(interaction_dt.columns)
    )

    df['t_rel'] = df.t - df.int_t
    df.rename(columns = {'int_t' : 'interaction_t'}, inplace = True)
    df['has_responded'] = np.where((df['t_rel'] > 0) & (df['velocity'] > 1), True, False)
    df['has_walked'] = np.where((df['t_rel'] > 0) & (df['velocity'] > 2.5), True, False)
    df.drop(columns = ['start', 'end'], inplace = True)
    
    # filter by window ahead of interaction time and find any postive response, return new df with only interaction time == 0 rows with response
    df['t'] = np.floor(df['t'])
    start_list = np.floor(interaction_dt['start'].to_numpy()).astype(int)
    end_list = np.ceil(interaction_dt['end'].to_numpy()).astype(int)

    response_df = pd.DataFrame()

    def format_window(response):
        if response is True:
            r = 1
        else:
            r = 0

        motif_df = filtered_df[filtered_df['t_rel'] <= 0]
        motif_df['has_responded'] = np.where(motif_df['t_rel'] == 0, response, motif_df['has_responded']) 
        cols = motif_df.columns.tolist()
        motif_df[cols] = motif_df[cols].apply(pd.to_numeric, errors='coerce', axis=1)
        d_small = motif_df.groupby('t').agg(**{
                        't' : ('t', 'mean'),
                        'x' : ('x', 'mean'),
                        'y' : ('y', 'mean'),
                        'w' : ('w', 'mean'),
                        'h' : ('h', 'mean'),
                        'phi' : ('phi', 'mean'),
                        'xy_dist_log10x1000' : ('xy_dist_log10x1000', 'mean'),
                        'velocity' : ('velocity', 'mean'),
                        'has_responded' : ('has_responded', 'mean')
                })
        t_range = list(range(0, len(d_small['t'] + 1)))
        t_range.reverse()
        d_small['t_count'] = t_range
        if len(d_small) != window + 1:
            return None
        else:
            d_small.drop(columns = ['has_responded'],  inplace=True)
            d_small['response'] = [response] * len(d_small)
            id = f'{c}_{r}'
            d_small['run_id'] = [id] * len(d_small)
            return d_small

    for c, (i,q) in enumerate(zip(start_list, end_list)):

        filtered_df = df[df.t.isin(list(range(i, q + 1)))]
        response_data = filtered_df[filtered_df['t_rel'] >= 0]

        if any(response_data['has_responded']):
            formatted_small = format_window(response = True)
            if formatted_small is not None:
                response_df = response_df.append(formatted_small)

        else:
            formatted_small = format_window(response = False)
            if formatted_small is not None:
                response_df = response_df.append(formatted_small)

    return response_df

def isolate_activity_lengths(data, intervals, window, inactive = True, velocity_correction_coef = 3e-3):
    """
    Isolate activity lengths is a loading function that will find consecutive runs of inactivity or activity and segment mement them into same sized windows
    at intervals stated by the user. This function

    Params:
    @data = pandas dataframe, a dataframe object as provided from the read_single_roi fucntion with a column of time 't' in seconds
    @intervals = list of ints, a list with the timestamps you want the window to work back from, must be in minutes
    @inactive = bool, whether to search for runs of activity or inactivity
    @velocity_correction_coef - float, coeffient to find the velocity over time

    returns a pandas dataframe with every run according the the requirements and all data values
    """
    assert(isinstance(intervals, list))
    assert(all(isinstance(item, int) for item in intervals))

    data['deltaT'] = data.t.diff()
    data['dist'] = 10 ** (data.xy_dist_log10x1000 / 1000)
    data['velocity'] = data.dist / velocity_correction_coef
    data.drop(columns = ['deltaT', 'dist'], inplace = True)
    data['t'] = np.floor(data['t'])
    data = data.groupby('t').agg(**{
                'x' : ('x', 'mean'),
                'y' : ('y', 'mean'),
                'w' : ('w', 'mean'),
                'h' : ('h', 'mean'),
                'phi' : ('phi', 'mean'),
                'xy_dist_log10x1000' : ('xy_dist_log10x1000', 'max'),
                'velocity' : ('velocity', 'max')
        })
    data.reset_index(inplace = True)
    data['moving'] = np.where(data['velocity'] > 1, 1, 0)

    def find_inactivity(data, inactive = inactive):
                if inactive == True:
                    elem = 0
                else:
                    elem = 1
                inactive_count = []
                data_list = []
                counter = 1
                for c, q in enumerate(data):
                    if c == 0 and q != elem:
                        inactive_count.append(np.NaN)
                        data_list.append(q)

                    elif c == 0 and q == elem:
                        inactive_count.append(counter)
                        data_list.append(q)
                        counter += 1

                    else:
                        if q == elem:
                            inactive_count.append(counter)
                            data_list.append(q)
                            counter += 1

                        else:
                            inactive_count.append(np.NaN)
                            data_list.append(q)
                            counter = 1

                return inactive_count
    
    data['inactive_count'] =  find_inactivity(data['moving'].to_numpy())
    data = data[data['inactive_count'] <= max(intervals) * 60]

    inactivity_df = pd.DataFrame()

    for interval in intervals:
        #isolate interaction times
        interaction_dt = data['t'][data['inactive_count'] == interval*60].to_frame()
        interaction_dt.rename(columns = {'t' : 'int_t'}, inplace = True)

        #check some interactions took place, return none if empty
        if len(interaction_dt.index) < 1:
            return None

        interaction_dt['start'] = interaction_dt.int_t - (window-1)
        interaction_dt['end'] = interaction_dt.int_t
        
        ints = data.t.values
        starts = interaction_dt.start.values 
        ends = interaction_dt.end.values  

        i, j = np.where((ints[:, None] >= starts) & (ints[:, None] <= ends))
        
        df = pd.DataFrame(
            np.column_stack([data.values[i], interaction_dt.values[j]]),
            columns = data.columns.append(interaction_dt.columns)
        )
        df.drop(columns = ['end', 'int_t', 'moving', 'inactive_count'], inplace = True)

        gb = df.groupby('start').size()
        filt_gb = gb[gb == window]
        filt_df = df[df['start'].isin(filt_gb.index.tolist())]
        inactivity_df = pd.concat([inactivity_df, filt_df], ignore_index = False)
                

    return inactivity_df