from collections import namedtuple
import datetime
from decimal import Decimal
import io
from itertools import product
import platform
from types import SimpleNamespace

import dateutil.tz

import numpy as np
from numpy import ma
from cycler import cycler
import pytest

import matplotlib
import matplotlib as mpl
from matplotlib.testing.decorators import (
    image_comparison, check_figures_equal, remove_ticks_and_titles)
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
from matplotlib.figure import Figure
import matplotlib.font_manager as mfont_manager
import matplotlib.markers as mmarkers
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.transforms as mtransforms
from numpy.testing import (
    assert_allclose, assert_array_equal, assert_array_almost_equal)
from matplotlib import rc_context
from matplotlib.cbook import MatplotlibDeprecationWarning

# Note: Some test cases are run twice: once normally and once with labeled data
#       These two must be defined in the same test function or need to have
#       different baseline images to prevent race conditions when pytest runs
#       the tests with multiple threads.


def test_get_labels():
    fig, ax = plt.subplots()
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    assert ax.get_xlabel() == 'x label'
    assert ax.get_ylabel() == 'y label'


@check_figures_equal()
def test_label_loc_vertical(fig_test, fig_ref):
    ax = fig_test.subplots()
    sc = ax.scatter([1, 2], [1, 2], c=[1, 2], label='scatter')
    ax.legend()
    ax.set_ylabel('Y Label', loc='top')
    ax.set_xlabel('X Label', loc='right')
    cbar = fig_test.colorbar(sc)
    cbar.set_label("Z Label", loc='top')

    ax = fig_ref.subplots()
    sc = ax.scatter([1, 2], [1, 2], c=[1, 2], label='scatter')
    ax.legend()
    ax.set_ylabel('Y Label', y=1, ha='right')
    ax.set_xlabel('X Label', x=1, ha='right')
    cbar = fig_ref.colorbar(sc)
    cbar.set_label("Z Label", y=1, ha='right')


@check_figures_equal()
def test_label_loc_horizontal(fig_test, fig_ref):
    ax = fig_test.subplots()
    sc = ax.scatter([1, 2], [1, 2], c=[1, 2], label='scatter')
    ax.legend()
    ax.set_ylabel('Y Label', loc='bottom')
    ax.set_xlabel('X Label', loc='left')
    cbar = fig_test.colorbar(sc, orientation='horizontal')
    cbar.set_label("Z Label", loc='left')

    ax = fig_ref.subplots()
    sc = ax.scatter([1, 2], [1, 2], c=[1, 2], label='scatter')
    ax.legend()
    ax.set_ylabel('Y Label', y=0, ha='left')
    ax.set_xlabel('X Label', x=0, ha='left')
    cbar = fig_ref.colorbar(sc, orientation='horizontal')
    cbar.set_label("Z Label", x=0, ha='left')


@check_figures_equal()
def test_label_loc_rc(fig_test, fig_ref):
    with matplotlib.rc_context({"xaxis.labellocation": "right",
                                "yaxis.labellocation": "top"}):
        ax = fig_test.subplots()
        sc = ax.scatter([1, 2], [1, 2], c=[1, 2], label='scatter')
        ax.legend()
        ax.set_ylabel('Y Label')
        ax.set_xlabel('X Label')
        cbar = fig_test.colorbar(sc, orientation='horizontal')
        cbar.set_label("Z Label")

    ax = fig_ref.subplots()
    sc = ax.scatter([1, 2], [1, 2], c=[1, 2], label='scatter')
    ax.legend()
    ax.set_ylabel('Y Label', y=1, ha='right')
    ax.set_xlabel('X Label', x=1, ha='right')
    cbar = fig_ref.colorbar(sc, orientation='horizontal')
    cbar.set_label("Z Label", x=1, ha='right')


def test_label_shift():
    fig, ax = plt.subplots()

    # Test label re-centering on x-axis
    ax.set_xlabel("Test label", loc="left")
    ax.set_xlabel("Test label", loc="center")
    assert ax.xaxis.get_label().get_horizontalalignment() == "center"
    ax.set_xlabel("Test label", loc="right")
    assert ax.xaxis.get_label().get_horizontalalignment() == "right"
    ax.set_xlabel("Test label", loc="center")
    assert ax.xaxis.get_label().get_horizontalalignment() == "center"

    # Test label re-centering on y-axis
    ax.set_ylabel("Test label", loc="top")
    ax.set_ylabel("Test label", loc="center")
    assert ax.yaxis.get_label().get_horizontalalignment() == "center"
    ax.set_ylabel("Test label", loc="bottom")
    assert ax.yaxis.get_label().get_horizontalalignment() == "left"
    ax.set_ylabel("Test label", loc="center")
    assert ax.yaxis.get_label().get_horizontalalignment() == "center"


@check_figures_equal(extensions=["png"])
def test_acorr(fig_test, fig_ref):
    np.random.seed(19680801)
    Nx = 512
    x = np.random.normal(0, 1, Nx).cumsum()
    maxlags = Nx-1

    ax_test = fig_test.subplots()
    ax_test.acorr(x, maxlags=maxlags)

    ax_ref = fig_ref.subplots()
    # Normalized autocorrelation
    norm_auto_corr = np.correlate(x, x, mode="full")/np.dot(x, x)
    lags = np.arange(-maxlags, maxlags+1)
    norm_auto_corr = norm_auto_corr[Nx-1-maxlags:Nx+maxlags]
    ax_ref.vlines(lags, [0], norm_auto_corr)
    ax_ref.axhline(y=0, xmin=0, xmax=1)


@check_figures_equal(extensions=["png"])
def test_spy(fig_test, fig_ref):
    np.random.seed(19680801)
    a = np.ones(32 * 32)
    a[:16 * 32] = 0
    np.random.shuffle(a)
    a = a.reshape((32, 32))

    axs_test = fig_test.subplots(2)
    axs_test[0].spy(a)
    axs_test[1].spy(a, marker=".", origin="lower")

    axs_ref = fig_ref.subplots(2)
    axs_ref[0].imshow(a, cmap="gray_r", interpolation="nearest")
    axs_ref[0].xaxis.tick_top()
    axs_ref[1].plot(*np.nonzero(a)[::-1], ".", markersize=10)
    axs_ref[1].set(
        aspect=1, xlim=axs_ref[0].get_xlim(), ylim=axs_ref[0].get_ylim()[::-1])
    for ax in axs_ref:
        ax.xaxis.set_ticks_position("both")


def test_spy_invalid_kwargs():
    fig, ax = plt.subplots()
    for unsupported_kw in [{'interpolation': 'nearest'},
                           {'marker': 'o', 'linestyle': 'solid'}]:
        with pytest.raises(TypeError):
            ax.spy(np.eye(3, 3), **unsupported_kw)


@check_figures_equal(extensions=["png"])
def test_matshow(fig_test, fig_ref):
    mpl.style.use("mpl20")
    a = np.random.rand(32, 32)
    fig_test.add_subplot().matshow(a)
    ax_ref = fig_ref.add_subplot()
    ax_ref.imshow(a)
    ax_ref.xaxis.tick_top()
    ax_ref.xaxis.set_ticks_position('both')


@image_comparison(['formatter_ticker_001',
                   'formatter_ticker_002',
                   'formatter_ticker_003',
                   'formatter_ticker_004',
                   'formatter_ticker_005',
                   ])
def test_formatter_ticker():
    import matplotlib.testing.jpl_units as units
    units.register()

    # This should affect the tick size.  (Tests issue #543)
    matplotlib.rcParams['lines.markeredgewidth'] = 30

    # This essentially test to see if user specified labels get overwritten
    # by the auto labeler functionality of the axes.
    xdata = [x*units.sec for x in range(10)]
    ydata1 = [(1.5*y - 0.5)*units.km for y in range(10)]
    ydata2 = [(1.75*y - 1.0)*units.km for y in range(10)]

    ax = plt.figure().subplots()
    ax.set_xlabel("x-label 001")

    ax = plt.figure().subplots()
    ax.set_xlabel("x-label 001")
    ax.plot(xdata, ydata1, color='blue', xunits="sec")

    ax = plt.figure().subplots()
    ax.set_xlabel("x-label 001")
    ax.plot(xdata, ydata1, color='blue', xunits="sec")
    ax.set_xlabel("x-label 003")

    ax = plt.figure().subplots()
    ax.plot(xdata, ydata1, color='blue', xunits="sec")
    ax.plot(xdata, ydata2, color='green', xunits="hour")
    ax.set_xlabel("x-label 004")

    # See SF bug 2846058
    # https://sourceforge.net/tracker/?func=detail&aid=2846058&group_id=80706&atid=560720
    ax = plt.figure().subplots()
    ax.plot(xdata, ydata1, color='blue', xunits="sec")
    ax.plot(xdata, ydata2, color='green', xunits="hour")
    ax.set_xlabel("x-label 005")
    ax.autoscale_view()


def test_funcformatter_auto_formatter():
    def _formfunc(x, pos):
        return ''

    ax = plt.figure().subplots()

    assert ax.xaxis.isDefault_majfmt
    assert ax.xaxis.isDefault_minfmt
    assert ax.yaxis.isDefault_majfmt
    assert ax.yaxis.isDefault_minfmt

    ax.xaxis.set_major_formatter(_formfunc)

    assert not ax.xaxis.isDefault_majfmt
    assert ax.xaxis.isDefault_minfmt
    assert ax.yaxis.isDefault_majfmt
    assert ax.yaxis.isDefault_minfmt

    targ_funcformatter = mticker.FuncFormatter(_formfunc)

    assert isinstance(ax.xaxis.get_major_formatter(),
                      mticker.FuncFormatter)

    assert ax.xaxis.get_major_formatter().func == targ_funcformatter.func


def test_strmethodformatter_auto_formatter():
    formstr = '{x}_{pos}'

    ax = plt.figure().subplots()

    assert ax.xaxis.isDefault_majfmt
    assert ax.xaxis.isDefault_minfmt
    assert ax.yaxis.isDefault_majfmt
    assert ax.yaxis.isDefault_minfmt

    ax.yaxis.set_minor_formatter(formstr)

    assert ax.xaxis.isDefault_majfmt
    assert ax.xaxis.isDefault_minfmt
    assert ax.yaxis.isDefault_majfmt
    assert not ax.yaxis.isDefault_minfmt

    targ_strformatter = mticker.StrMethodFormatter(formstr)

    assert isinstance(ax.yaxis.get_minor_formatter(),
                      mticker.StrMethodFormatter)

    assert ax.yaxis.get_minor_formatter().fmt == targ_strformatter.fmt


@image_comparison(["twin_axis_locators_formatters"])
def test_twin_axis_locators_formatters():
    vals = np.linspace(0, 1, num=5, endpoint=True)
    locs = np.sin(np.pi * vals / 2.0)

    majl = plt.FixedLocator(locs)
    minl = plt.FixedLocator([0.1, 0.2, 0.3])

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot([0.1, 100], [0, 1])
    ax1.yaxis.set_major_locator(majl)
    ax1.yaxis.set_minor_locator(minl)
    ax1.yaxis.set_major_formatter(plt.FormatStrFormatter('%08.2lf'))
    ax1.yaxis.set_minor_formatter(plt.FixedFormatter(['tricks', 'mind',
                                                      'jedi']))

    ax1.xaxis.set_major_locator(plt.LinearLocator())
    ax1.xaxis.set_minor_locator(plt.FixedLocator([15, 35, 55, 75]))
    ax1.xaxis.set_major_formatter(plt.FormatStrFormatter('%05.2lf'))
    ax1.xaxis.set_minor_formatter(plt.FixedFormatter(['c', '3', 'p', 'o']))
    ax1.twiny()
    ax1.twinx()


def test_twinx_cla():
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    ax3 = ax2.twiny()
    plt.draw()
    assert not ax2.xaxis.get_visible()
    assert not ax2.patch.get_visible()
    ax2.cla()
    ax3.cla()

    assert not ax2.xaxis.get_visible()
    assert not ax2.patch.get_visible()
    assert ax2.yaxis.get_visible()

    assert ax3.xaxis.get_visible()
    assert not ax3.patch.get_visible()
    assert not ax3.yaxis.get_visible()

    assert ax.xaxis.get_visible()
    assert ax.patch.get_visible()
    assert ax.yaxis.get_visible()


@pytest.mark.parametrize('twin', ('x', 'y'))
@check_figures_equal(extensions=['png'], tol=0.19)
def test_twin_logscale(fig_test, fig_ref, twin):
    twin_func = f'twin{twin}'  # test twinx or twiny
    set_scale = f'set_{twin}scale'
    x = np.arange(1, 100)

    # Change scale after twinning.
    ax_test = fig_test.add_subplot(2, 1, 1)
    ax_twin = getattr(ax_test, twin_func)()
    getattr(ax_test, set_scale)('log')
    ax_twin.plot(x, x)

    # Twin after changing scale.
    ax_test = fig_test.add_subplot(2, 1, 2)
    getattr(ax_test, set_scale)('log')
    ax_twin = getattr(ax_test, twin_func)()
    ax_twin.plot(x, x)

    for i in [1, 2]:
        ax_ref = fig_ref.add_subplot(2, 1, i)
        getattr(ax_ref, set_scale)('log')
        ax_ref.plot(x, x)

        # This is a hack because twinned Axes double-draw the frame.
        # Remove this when that is fixed.
        Path = matplotlib.path.Path
        fig_ref.add_artist(
            matplotlib.patches.PathPatch(
                Path([[0, 0], [0, 1],
                      [0, 1], [1, 1],
                      [1, 1], [1, 0],
                      [1, 0], [0, 0]],
                     [Path.MOVETO, Path.LINETO] * 4),
                transform=ax_ref.transAxes,
                facecolor='none',
                edgecolor=mpl.rcParams['axes.edgecolor'],
                linewidth=mpl.rcParams['axes.linewidth'],
                capstyle='projecting'))

    remove_ticks_and_titles(fig_test)
    remove_ticks_and_titles(fig_ref)


@image_comparison(['twin_autoscale.png'])
def test_twinx_axis_scales():
    x = np.array([0, 0.5, 1])
    y = 0.5 * x
    x2 = np.array([0, 1, 2])
    y2 = 2 * x2

    fig = plt.figure()
    ax = fig.add_axes((0, 0, 1, 1), autoscalex_on=False, autoscaley_on=False)
    ax.plot(x, y, color='blue', lw=10)

    ax2 = plt.twinx(ax)
    ax2.plot(x2, y2, 'r--', lw=5)

    ax.margins(0, 0)
    ax2.margins(0, 0)


def test_twin_inherit_autoscale_setting():
    fig, ax = plt.subplots()
    ax_x_on = ax.twinx()
    ax.set_autoscalex_on(False)
    ax_x_off = ax.twinx()

    assert ax_x_on.get_autoscalex_on()
    assert not ax_x_off.get_autoscalex_on()

    ax_y_on = ax.twiny()
    ax.set_autoscaley_on(False)
    ax_y_off = ax.twiny()

    assert ax_y_on.get_autoscaley_on()
    assert not ax_y_off.get_autoscaley_on()


def test_inverted_cla():
    # GitHub PR #5450. Setting autoscale should reset
    # axes to be non-inverted.
    # plotting an image, then 1d graph, axis is now down
    fig = plt.figure(0)
    ax = fig.gca()
    # 1. test that a new axis is not inverted per default
    assert not ax.xaxis_inverted()
    assert not ax.yaxis_inverted()
    img = np.random.random((100, 100))
    ax.imshow(img)
    # 2. test that a image axis is inverted
    assert not ax.xaxis_inverted()
    assert ax.yaxis_inverted()
    # 3. test that clearing and plotting a line, axes are
    # not inverted
    ax.cla()
    x = np.linspace(0, 2*np.pi, 100)
    ax.plot(x, np.cos(x))
    assert not ax.xaxis_inverted()
    assert not ax.yaxis_inverted()

    # 4. autoscaling should not bring back axes to normal
    ax.cla()
    ax.imshow(img)
    plt.autoscale()
    assert not ax.xaxis_inverted()
    assert ax.yaxis_inverted()

    # 5. two shared axes. Inverting the master axis should invert the shared
    # axes; clearing the master axis should bring axes in shared
    # axes back to normal.
    ax0 = plt.subplot(211)
    ax1 = plt.subplot(212, sharey=ax0)
    ax0.yaxis.set_inverted(True)
    assert ax1.yaxis_inverted()
    ax1.plot(x, np.cos(x))
    ax0.cla()
    assert not ax1.yaxis_inverted()
    ax1.cla()
    # 6. clearing the nonmaster should not touch limits
    ax0.imshow(img)
    ax1.plot(x, np.cos(x))
    ax1.cla()
    assert ax.yaxis_inverted()

    # clean up
    plt.close(fig)


@check_figures_equal(extensions=["png"])
def test_minorticks_on_rcParams_both(fig_test, fig_ref):
    with matplotlib.rc_context({"xtick.minor.visible": True,
                                "ytick.minor.visible": True}):
        ax_test = fig_test.subplots()
        ax_test.plot([0, 1], [0, 1])
    ax_ref = fig_ref.subplots()
    ax_ref.plot([0, 1], [0, 1])
    ax_ref.minorticks_on()


@image_comparison(["autoscale_tiny_range"], remove_text=True)
def test_autoscale_tiny_range():
    # github pull #904
    fig, axs = plt.subplots(2, 2)
    for i, ax in enumerate(axs.flat):
        y1 = 10**(-11 - i)
        ax.plot([0, 1], [1, 1 + y1])


@mpl.style.context('default')
def test_autoscale_tight():
    fig, ax = plt.subplots(1, 1)
    ax.plot([1, 2, 3, 4])
    ax.autoscale(enable=True, axis='x', tight=False)
    ax.autoscale(enable=True, axis='y', tight=True)
    assert_allclose(ax.get_xlim(), (-0.15, 3.15))
    assert_allclose(ax.get_ylim(), (1.0, 4.0))

    # Check that autoscale is on
    assert ax.get_autoscalex_on()
    assert ax.get_autoscaley_on()
    assert ax.get_autoscale_on()
    # Set enable to None
    ax.autoscale(enable=None)
    # Same limits
    assert_allclose(ax.get_xlim(), (-0.15, 3.15))
    assert_allclose(ax.get_ylim(), (1.0, 4.0))
    # autoscale still on
    assert ax.get_autoscalex_on()
    assert ax.get_autoscaley_on()
    assert ax.get_autoscale_on()


@mpl.style.context('default')
def test_autoscale_log_shared():
    # related to github #7587
    # array starts at zero to trigger _minpos handling
    x = np.arange(100, dtype=float)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.loglog(x, x)
    ax2.semilogx(x, x)
    ax1.autoscale(tight=True)
    ax2.autoscale(tight=True)
    plt.draw()
    lims = (x[1], x[-1])
    assert_allclose(ax1.get_xlim(), lims)
    assert_allclose(ax1.get_ylim(), lims)
    assert_allclose(ax2.get_xlim(), lims)
    assert_allclose(ax2.get_ylim(), (x[0], x[-1]))


@mpl.style.context('default')
def test_use_sticky_edges():
    fig, ax = plt.subplots()
    ax.imshow([[0, 1], [2, 3]], origin='lower')
    assert_allclose(ax.get_xlim(), (-0.5, 1.5))
    assert_allclose(ax.get_ylim(), (-0.5, 1.5))
    ax.use_sticky_edges = False
    ax.autoscale()
    xlim = (-0.5 - 2 * ax._xmargin, 1.5 + 2 * ax._xmargin)
    ylim = (-0.5 - 2 * ax._ymargin, 1.5 + 2 * ax._ymargin)
    assert_allclose(ax.get_xlim(), xlim)
    assert_allclose(ax.get_ylim(), ylim)
    # Make sure it is reversible:
    ax.use_sticky_edges = True
    ax.autoscale()
    assert_allclose(ax.get_xlim(), (-0.5, 1.5))
    assert_allclose(ax.get_ylim(), (-0.5, 1.5))


@check_figures_equal(extensions=["png"])
def test_sticky_shared_axes(fig_test, fig_ref):
    # Check that sticky edges work whether they are set in an axes that is a
    # "master" in a share, or an axes that is a "follower".
    Z = np.arange(15).reshape(3, 5)

    ax0 = fig_test.add_subplot(211)
    ax1 = fig_test.add_subplot(212, sharex=ax0)
    ax1.pcolormesh(Z)

    ax0 = fig_ref.add_subplot(212)
    ax1 = fig_ref.add_subplot(211, sharex=ax0)
    ax0.pcolormesh(Z)


@image_comparison(['offset_points'], remove_text=True)
def test_basic_annotate():
    # Setup some data
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2.0*np.pi * t)

    # Offset Points

    fig = plt.figure()
    ax = fig.add_subplot(autoscale_on=False, xlim=(-1, 5), ylim=(-3, 5))
    line, = ax.plot(t, s, lw=3, color='purple')

    ax.annotate('local max', xy=(3, 1), xycoords='data',
                xytext=(3, 3), textcoords='offset points')


@image_comparison(['arrow_simple.png'], remove_text=True)
def test_arrow_simple():
    # Simple image test for ax.arrow
    # kwargs that take discrete values
    length_includes_head = (True, False)
    shape = ('full', 'left', 'right')
    head_starts_at_zero = (True, False)
    # Create outer product of values
    kwargs = product(length_includes_head, shape, head_starts_at_zero)

    fig, axs = plt.subplots(3, 4)
    for i, (ax, kwarg) in enumerate(zip(axs.flat, kwargs)):
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        # Unpack kwargs
        (length_includes_head, shape, head_starts_at_zero) = kwarg
        theta = 2 * np.pi * i / 12
        # Draw arrow
        ax.arrow(0, 0, np.sin(theta), np.cos(theta),
                 width=theta/100,
                 length_includes_head=length_includes_head,
                 shape=shape,
                 head_starts_at_zero=head_starts_at_zero,
                 head_width=theta / 10,
                 head_length=theta / 10)


def test_arrow_empty():
    _, ax = plt.subplots()
    # Create an empty FancyArrow
    ax.arrow(0, 0, 0, 0, head_length=0)


def test_arrow_in_view():
    _, ax = plt.subplots()
    ax.arrow(1, 1, 1, 1)
    assert ax.get_xlim() == (0.8, 2.2)
    assert ax.get_ylim() == (0.8, 2.2)


def test_annotate_default_arrow():
    # Check that we can make an annotation arrow with only default properties.
    fig, ax = plt.subplots()
    ann = ax.annotate("foo", (0, 1), xytext=(2, 3))
    assert ann.arrow_patch is None
    ann = ax.annotate("foo", (0, 1), xytext=(2, 3), arrowprops={})
    assert ann.arrow_patch is not None


@image_comparison(['fill_units.png'], savefig_kwarg={'dpi': 60})
def test_fill_units():
    import matplotlib.testing.jpl_units as units
    units.register()

    # generate some data
    t = units.Epoch("ET", dt=datetime.datetime(2009, 4, 27))
    value = 10.0 * units.deg
    day = units.Duration("ET", 24.0 * 60.0 * 60.0)
    dt = np.arange('2009-04-27', '2009-04-29', dtype='datetime64[D]')
    dtn = mdates.date2num(dt)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    ax1.plot([t], [value], yunits='deg', color='red')
    ind = [0, 0, 1, 1]
    ax1.fill(dtn[ind], [0.0, 0.0, 90.0, 0.0], 'b')

    ax2.plot([t], [value], yunits='deg', color='red')
    ax2.fill([t, t, t + day, t + day],
             [0.0, 0.0, 90.0, 0.0], 'b')

    ax3.plot([t], [value], yunits='deg', color='red')
    ax3.fill(dtn[ind],
             [0 * units.deg, 0 * units.deg, 90 * units.deg, 0 * units.deg],
             'b')

    ax4.plot([t], [value], yunits='deg', color='red')
    ax4.fill([t, t, t + day, t + day],
             [0 * units.deg, 0 * units.deg, 90 * units.deg, 0 * units.deg],
             facecolor="blue")
    fig.autofmt_xdate()


def test_plot_format_kwarg_redundant():
    with pytest.warns(UserWarning, match="marker .* redundantly defined"):
        plt.plot([0], [0], 'o', marker='x')
    with pytest.warns(UserWarning, match="linestyle .* redundantly defined"):
        plt.plot([0], [0], '-', linestyle='--')
    with pytest.warns(UserWarning, match="color .* redundantly defined"):
        plt.plot([0], [0], 'r', color='blue')
    # smoke-test: should not warn
    plt.errorbar([0], [0], fmt='none', color='blue')


@check_figures_equal(extensions=["png"])
def test_errorbar_dashes(fig_test, fig_ref):
    x = [1, 2, 3, 4]
    y = np.sin(x)

    ax_ref = fig_ref.gca()
    ax_test = fig_test.gca()

    line, *_ = ax_ref.errorbar(x, y, xerr=np.abs(y), yerr=np.abs(y))
    line.set_dashes([2, 2])

    ax_test.errorbar(x, y, xerr=np.abs(y), yerr=np.abs(y), dashes=[2, 2])


@image_comparison(['single_point', 'single_point'])
def test_single_point():
    # Issue #1796: don't let lines.marker affect the grid
    matplotlib.rcParams['lines.marker'] = 'o'
    matplotlib.rcParams['axes.grid'] = True

    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot([0], [0], 'o')
    ax2.plot([1], [1], 'o')

    # Reuse testcase from above for a labeled data test
    data = {'a': [0], 'b': [1]}

    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot('a', 'a', 'o', data=data)
    ax2.plot('b', 'b', 'o', data=data)


@image_comparison(['single_date.png'], style='mpl20')
def test_single_date():

    # use former defaults to match existing baseline image
    plt.rcParams['axes.formatter.limits'] = -7, 7
    dt = mdates.date2num(np.datetime64('0000-12-31'))

    time1 = [721964.0]
    data1 = [-65.54]

    fig, ax = plt.subplots(2, 1)
    ax[0].plot_date(time1 + dt, data1, 'o', color='r')
    ax[1].plot(time1, data1, 'o', color='r')


@check_figures_equal(extensions=["png"])
def test_shaped_data(fig_test, fig_ref):
    row = np.arange(10).reshape((1, -1))
    col = np.arange(0, 100, 10).reshape((-1, 1))

    axs = fig_test.subplots(2)
    axs[0].plot(row)  # Actually plots nothing (columns are single points).
    axs[1].plot(col)  # Same as plotting 1d.

    axs = fig_ref.subplots(2)
    # xlim from the implicit "x=0", ylim from the row datalim.
    axs[0].set(xlim=(-.06, .06), ylim=(0, 9))
    axs[1].plot(col.ravel())


def test_structured_data():
    # support for structured data
    pts = np.array([(1, 1), (2, 2)], dtype=[("ones", float), ("twos", float)])

    # this should not read second name as a format and raise ValueError
    axs = plt.figure().subplots(2)
    axs[0].plot("ones", "twos", data=pts)
    axs[1].plot("ones", "twos", "r", data=pts)


@image_comparison(['aitoff_proj'], extensions=["png"],
                  remove_text=True, style='mpl20')
def test_aitoff_proj():
    """
    Test aitoff projection ref.:
    https://github.com/matplotlib/matplotlib/pull/14451
    """
    x = np.linspace(-np.pi, np.pi, 20)
    y = np.linspace(-np.pi / 2, np.pi / 2, 20)
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(8, 4.2),
                           subplot_kw=dict(projection="aitoff"))
    ax.grid()
    ax.plot(X.flat, Y.flat, 'o', markersize=4)


@image_comparison(['axvspan_epoch'])
def test_axvspan_epoch():
    import matplotlib.testing.jpl_units as units
    units.register()

    # generate some data
    t0 = units.Epoch("ET", dt=datetime.datetime(2009, 1, 20))
    tf = units.Epoch("ET", dt=datetime.datetime(2009, 1, 21))
    dt = units.Duration("ET", units.day.convert("sec"))

    ax = plt.gca()
    ax.axvspan(t0, tf, facecolor="blue", alpha=0.25)
    ax.set_xlim(t0 - 5.0*dt, tf + 5.0*dt)


@image_comparison(['axhspan_epoch'], tol=0.02)
def test_axhspan_epoch():
    import matplotlib.testing.jpl_units as units
    units.register()

    # generate some data
    t0 = units.Epoch("ET", dt=datetime.datetime(2009, 1, 20))
    tf = units.Epoch("ET", dt=datetime.datetime(2009, 1, 21))
    dt = units.Duration("ET", units.day.convert("sec"))

    ax = plt.gca()
    ax.axhspan(t0, tf, facecolor="blue", alpha=0.25)
    ax.set_ylim(t0 - 5.0*dt, tf + 5.0*dt)


@image_comparison(['hexbin_extent.png', 'hexbin_extent.png'], remove_text=True)
def test_hexbin_extent():
    # this test exposes sf bug 2856228
    fig, ax = plt.subplots()
    data = (np.arange(2000) / 2000).reshape((2, 1000))
    x, y = data

    ax.hexbin(x, y, extent=[.1, .3, .6, .7])

    # Reuse testcase from above for a labeled data test
    data = {"x": x, "y": y}

    fig, ax = plt.subplots()
    ax.hexbin("x", "y", extent=[.1, .3, .6, .7], data=data)


@image_comparison(['hexbin_empty.png'], remove_text=True)
def test_hexbin_empty():
    # From #3886: creating hexbin from empty dataset raises ValueError
    ax = plt.gca()
    ax.hexbin([], [])


def test_hexbin_pickable():
    # From #1973: Test that picking a hexbin collection works
    fig, ax = plt.subplots()
    data = (np.arange(200) / 200).reshape((2, 100))
    x, y = data
    hb = ax.hexbin(x, y, extent=[.1, .3, .6, .7], picker=-1)
    mouse_event = SimpleNamespace(x=400, y=300)
    assert hb.contains(mouse_event)[0]


@image_comparison(['hexbin_log.png'], style='mpl20')
def test_hexbin_log():
    # Issue #1636 (and also test log scaled colorbar)

    # Remove this line when this test image is regenerated.
    plt.rcParams['pcolormesh.snap'] = False

    np.random.seed(19680801)
    n = 100000
    x = np.random.standard_normal(n)
    y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
    y = np.power(2, y * 0.5)

    fig, ax = plt.subplots()
    h = ax.hexbin(x, y, yscale='log', bins='log',
                  marginals=True, reduce_C_function=np.sum)
    plt.colorbar(h)


def test_hexbin_log_clim():
    x, y = np.arange(200).reshape((2, 100))
    fig, ax = plt.subplots()
    h = ax.hexbin(x, y, bins='log', vmin=2, vmax=100)
    assert h.get_clim() == (2, 100)


def test_inverted_limits():
    # Test gh:1553
    # Calling invert_xaxis prior to plotting should not disable autoscaling
    # while still maintaining the inverted direction
    fig, ax = plt.subplots()
    ax.invert_xaxis()
    ax.plot([-5, -3, 2, 4], [1, 2, -3, 5])

    assert ax.get_xlim() == (4, -5)
    assert ax.get_ylim() == (-3, 5)
    plt.close()

    fig, ax = plt.subplots()
    ax.invert_yaxis()
    ax.plot([-5, -3, 2, 4], [1, 2, -3, 5])

    assert ax.get_xlim() == (-5, 4)
    assert ax.get_ylim() == (5, -3)

    # Test inverting nonlinear axes.
    fig, ax = plt.subplots()
    ax.set_yscale("log")
    ax.set_ylim(10, 1)
    assert ax.get_ylim() == (10, 1)


@image_comparison(['nonfinite_limits'])
def test_nonfinite_limits():
    x = np.arange(0., np.e, 0.01)
    # silence divide by zero warning from log(0)
    with np.errstate(divide='ignore'):
        y = np.log(x)
    x[len(x)//2] = np.nan
    fig, ax = plt.subplots()
    ax.plot(x, y)


@mpl.style.context('default')
@pytest.mark.parametrize('plot_fun',
                         ['scatter', 'plot', 'fill_between'])
@check_figures_equal(extensions=["png"])
def test_limits_empty_data(plot_fun, fig_test, fig_ref):
    # Check that plotting empty data doesn't change autoscaling of dates
    x = np.arange("2010-01-01", "2011-01-01", dtype="datetime64[D]")

    ax_test = fig_test.subplots()
    ax_ref = fig_ref.subplots()

    getattr(ax_test, plot_fun)([], [])

    for ax in [ax_test, ax_ref]:
        getattr(ax, plot_fun)(x, range(len(x)), color='C0')


@image_comparison(['imshow', 'imshow'], remove_text=True, style='mpl20')
def test_imshow():
    # use former defaults to match existing baseline image
    matplotlib.rcParams['image.interpolation'] = 'nearest'
    # Create a NxN image
    N = 100
    (x, y) = np.indices((N, N))
    x -= N//2
    y -= N//2
    r = np.sqrt(x**2+y**2-x*y)

    # Create a contour plot at N/4 and extract both the clip path and transform
    fig, ax = plt.subplots()
    ax.imshow(r)

    # Reuse testcase from above for a labeled data test
    data = {"r": r}
    fig, ax = plt.subplots()
    ax.imshow("r", data=data)


@image_comparison(['imshow_clip'], style='mpl20')
def test_imshow_clip():
    # As originally reported by Gellule Xg <gellule.xg@free.fr>
    # use former defaults to match existing baseline image
    matplotlib.rcParams['image.interpolation'] = 'nearest'

    # Create a NxN image
    N = 100
    (x, y) = np.indices((N, N))
    x -= N//2
    y -= N//2
    r = np.sqrt(x**2+y**2-x*y)

    # Create a contour plot at N/4 and extract both the clip path and transform
    fig, ax = plt.subplots()

    c = ax.contour(r, [N/4])
    x = c.collections[0]
    clip_path = x.get_paths()[0]
    clip_transform = x.get_transform()

    clip_path = mtransforms.TransformedPath(clip_path, clip_transform)

    # Plot the image clipped by the contour
    ax.imshow(r, clip_path=clip_path)


def test_imshow_norm_vminvmax():
    """Parameters vmin, vmax should error if norm is given."""
    a = [[1, 2], [3, 4]]
    ax = plt.axes()
    with pytest.raises(ValueError,
                       match="Passing parameters norm and vmin/vmax "
                             "simultaneously is not supported."):
        ax.imshow(a, norm=mcolors.Normalize(-10, 10), vmin=0, vmax=5)


@image_comparison(['polycollection_joinstyle'], remove_text=True)
def test_polycollection_joinstyle():
    # Bug #2890979 reported by Matthew West
    fig, ax = plt.subplots()
    verts = np.array([[1, 1], [1, 2], [2, 2], [2, 1]])
    c = mpl.collections.PolyCollection([verts], linewidths=40)
    ax.add_collection(c)
    ax.set_xbound(0, 3)
    ax.set_ybound(0, 3)


@pytest.mark.parametrize(
    'x, y1, y2', [
        (np.zeros((2, 2)), 3, 3),
        (np.arange(0.0, 2, 0.02), np.zeros((2, 2)), 3),
        (np.arange(0.0, 2, 0.02), 3, np.zeros((2, 2)))
    ], ids=[
        '2d_x_input',
        '2d_y1_input',
        '2d_y2_input'
    ]
)
def test_fill_between_input(x, y1, y2):
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        ax.fill_between(x, y1, y2)


@pytest.mark.parametrize(
    'y, x1, x2', [
        (np.zeros((2, 2)), 3, 3),
        (np.arange(0.0, 2, 0.02), np.zeros((2, 2)), 3),
        (np.arange(0.0, 2, 0.02), 3, np.zeros((2, 2)))
    ], ids=[
        '2d_y_input',
        '2d_x1_input',
        '2d_x2_input'
    ]
)
def test_fill_betweenx_input(y, x1, x2):
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        ax.fill_betweenx(y, x1, x2)


@image_comparison(['fill_between_interpolate'], remove_text=True)
def test_fill_between_interpolate():
    x = np.arange(0.0, 2, 0.02)
    y1 = np.sin(2*np.pi*x)
    y2 = 1.2*np.sin(4*np.pi*x)

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(x, y1, x, y2, color='black')
    ax1.fill_between(x, y1, y2, where=y2 >= y1, facecolor='white', hatch='/',
                     interpolate=True)
    ax1.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red',
                     interpolate=True)

    # Test support for masked arrays.
    y2 = np.ma.masked_greater(y2, 1.0)
    # Test that plotting works for masked arrays with the first element masked
    y2[0] = np.ma.masked
    ax2.plot(x, y1, x, y2, color='black')
    ax2.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green',
                     interpolate=True)
    ax2.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red',
                     interpolate=True)


@image_comparison(['fill_between_interpolate_decreasing'],
                  style='mpl20', remove_text=True)
def test_fill_between_interpolate_decreasing():
    p = np.array([724.3, 700, 655])
    t = np.array([9.4, 7, 2.2])
    prof = np.array([7.9, 6.6, 3.8])

    fig, ax = plt.subplots(figsize=(9, 9))

    ax.plot(t, p, 'tab:red')
    ax.plot(prof, p, 'k')

    ax.fill_betweenx(p, t, prof, where=prof < t,
                     facecolor='blue', interpolate=True, alpha=0.4)
    ax.fill_betweenx(p, t, prof, where=prof > t,
                     facecolor='red', interpolate=True, alpha=0.4)

    ax.set_xlim(0, 30)
    ax.set_ylim(800, 600)


@image_comparison(['fill_between_interpolate_nan'], remove_text=True)
def test_fill_between_interpolate_nan():
    # Tests fix for issue #18986.
    x = np.arange(10)
    y1 = np.asarray([8, 18, np.nan, 18, 8, 18, 24, 18, 8, 18])
    y2 = np.asarray([18, 11, 8, 11, 18, 26, 32, 30, np.nan, np.nan])

    # NumPy <1.19 issues warning 'invalid value encountered in greater_equal'
    # for comparisons that include nan.
    with np.errstate(invalid='ignore'):
        greater2 = y2 >= y1
        greater1 = y1 >= y2

    fig, ax = plt.subplots()

    ax.plot(x, y1, c='k')
    ax.plot(x, y2, c='b')
    ax.fill_between(x, y1, y2, where=greater2, facecolor="green",
                    interpolate=True, alpha=0.5)
    ax.fill_between(x, y1, y2, where=greater1, facecolor="red",
                    interpolate=True, alpha=0.5)


# test_symlog and test_symlog2 used to have baseline images in all three
# formats, but the png and svg baselines got invalidated by the removal of
# minor tick overstriking.
@image_comparison(['symlog.pdf'])
def test_symlog():
    x = np.array([0, 1, 2, 4, 6, 9, 12, 24])
    y = np.array([1000000, 500000, 100000, 100, 5, 0, 0, 0])

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_yscale('symlog')
    ax.set_xscale('linear')
    ax.set_ylim(-1, 10000000)


@image_comparison(['symlog2.pdf'], remove_text=True)
def test_symlog2():
    # Numbers from -50 to 50, with 0.1 as step
    x = np.arange(-50, 50, 0.001)

    fig, axs = plt.subplots(5, 1)
    for ax, linthresh in zip(axs, [20., 2., 1., 0.1, 0.01]):
        ax.plot(x, x)
        ax.set_xscale('symlog', linthresh=linthresh)
        ax.grid(True)
    axs[-1].set_ylim(-0.1, 0.1)


def test_pcolorargs_5205():
    # Smoketest to catch issue found in gh:5205
    x = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]
    y = [-1.5, -1.25, -1.0, -0.75, -0.5, -0.25, 0,
         0.25, 0.5, 0.75, 1.0, 1.25, 1.5]
    X, Y = np.meshgrid(x, y)
    Z = np.hypot(X, Y)

    plt.pcolor(Z)
    plt.pcolor(list(Z))
    plt.pcolor(x, y, Z[:-1, :-1])
    plt.pcolor(X, Y, list(Z[:-1, :-1]))


@image_comparison(['pcolormesh'], remove_text=True)
def test_pcolormesh():
    # Remove this line when this test image is regenerated.
    plt.rcParams['pcolormesh.snap'] = False

    n = 12
    x = np.linspace(-1.5, 1.5, n)
    y = np.linspace(-1.5, 1.5, n*2)
    X, Y = np.meshgrid(x, y)
    Qx = np.cos(Y) - np.cos(X)
    Qz = np.sin(Y) + np.sin(X)
    Qx = (Qx + 1.1)
    Z = np.hypot(X, Y) / 5
    Z = (Z - Z.min()) / Z.ptp()

    # The color array can include masked values:
    Zm = ma.masked_where(np.abs(Qz) < 0.5 * np.max(Qz), Z)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.pcolormesh(Qx, Qz, Z[:-1, :-1], lw=0.5, edgecolors='k')
    ax2.pcolormesh(Qx, Qz, Z[:-1, :-1], lw=2, edgecolors=['b', 'w'])
    ax3.pcolormesh(Qx, Qz, Z, shading="gouraud")


@image_comparison(['pcolormesh_alpha'], extensions=["png", "pdf"],
                  remove_text=True)
def test_pcolormesh_alpha():
    # Remove this line when this test image is regenerated.
    plt.rcParams['pcolormesh.snap'] = False

    n = 12
    X, Y = np.meshgrid(
        np.linspace(-1.5, 1.5, n),
        np.linspace(-1.5, 1.5, n*2)
    )
    Qx = X
    Qy = Y + np.sin(X)
    Z = np.hypot(X, Y) / 5
    Z = (Z - Z.min()) / Z.ptp()
    vir = plt.get_cmap("viridis", 16)
    # make another colormap with varying alpha
    colors = vir(np.arange(16))
    colors[:, 3] = 0.5 + 0.5*np.sin(np.arange(16))
    cmap = mcolors.ListedColormap(colors)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    for ax in ax1, ax2, ax3, ax4:
        ax.add_patch(mpatches.Rectangle(
            (0, -1.5), 1.5, 3, facecolor=[.7, .1, .1, .5], zorder=0
        ))
    # ax1, ax2: constant alpha
    ax1.pcolormesh(Qx, Qy, Z[:-1, :-1], cmap=vir, alpha=0.4,
                   shading='flat', zorder=1)
    ax2.pcolormesh(Qx, Qy, Z, cmap=vir, alpha=0.4, shading='gouraud', zorder=1)
    # ax3, ax4: alpha from colormap
    ax3.pcolormesh(Qx, Qy, Z[:-1, :-1], cmap=cmap, shading='flat', zorder=1)
    ax4.pcolormesh(Qx, Qy, Z, cmap=cmap, shading='gouraud', zorder=1)


@image_comparison(['pcolormesh_datetime_axis.png'],
                  remove_text=False, style='mpl20')
def test_pcolormesh_datetime_axis():
    # Remove this line when this test image is regenerated.
    plt.rcParams['pcolormesh.snap'] = False

    fig = plt.figure()
    fig.subplots_adjust(hspace=0.4, top=0.98, bottom=.15)
    base = datetime.datetime(2013, 1, 1)
    x = np.array([base + datetime.timedelta(days=d) for d in range(21)])
    y = np.arange(21)
    z1, z2 = np.meshgrid(np.arange(20), np.arange(20))
    z = z1 * z2
    plt.subplot(221)
    plt.pcolormesh(x[:-1], y[:-1], z[:-1, :-1])
    plt.subplot(222)
    plt.pcolormesh(x, y, z)
    x = np.repeat(x[np.newaxis], 21, axis=0)
    y = np.repeat(y[:, np.newaxis], 21, axis=1)
    plt.subplot(223)
    plt.pcolormesh(x[:-1, :-1], y[:-1, :-1], z[:-1, :-1])
    plt.subplot(224)
    plt.pcolormesh(x, y, z)
    for ax in fig.get_axes():
        for label in ax.get_xticklabels():
            label.set_ha('right')
            label.set_rotation(30)


@image_comparison(['pcolor_datetime_axis.png'],
                  remove_text=False, style='mpl20')
def test_pcolor_datetime_axis():
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.4, top=0.98, bottom=.15)
    base = datetime.datetime(2013, 1, 1)
    x = np.array([base + datetime.timedelta(days=d) for d in range(21)])
    y = np.arange(21)
    z1, z2 = np.meshgrid(np.arange(20), np.arange(20))
    z = z1 * z2
    plt.subplot(221)
    plt.pcolor(x[:-1], y[:-1], z[:-1, :-1])
    plt.subplot(222)
    plt.pcolor(x, y, z)
    x = np.repeat(x[np.newaxis], 21, axis=0)
    y = np.repeat(y[:, np.newaxis], 21, axis=1)
    plt.subplot(223)
    plt.pcolor(x[:-1, :-1], y[:-1, :-1], z[:-1, :-1])
    plt.subplot(224)
    plt.pcolor(x, y, z)
    for ax in fig.get_axes():
        for label in ax.get_xticklabels():
            label.set_ha('right')
            label.set_rotation(30)


def test_pcolorargs():
    n = 12
    x = np.linspace(-1.5, 1.5, n)
    y = np.linspace(-1.5, 1.5, n*2)
    X, Y = np.meshgrid(x, y)
    Z = np.hypot(X, Y) / 5

    _, ax = plt.subplots()
    with pytest.raises(TypeError):
        ax.pcolormesh(y, x, Z)
    with pytest.raises(TypeError):
        ax.pcolormesh(X, Y, Z.T)
    with pytest.raises(TypeError):
        ax.pcolormesh(x, y, Z[:-1, :-1], shading="gouraud")
    with pytest.raises(TypeError):
        ax.pcolormesh(X, Y, Z[:-1, :-1], shading="gouraud")
    x[0] = np.NaN
    with pytest.raises(ValueError):
        ax.pcolormesh(x, y, Z[:-1, :-1])
    with np.errstate(invalid='ignore'):
        x = np.ma.array(x, mask=(x < 0))
    with pytest.raises(ValueError):
        ax.pcolormesh(x, y, Z[:-1, :-1])
    # Expect a warning with non-increasing coordinates
    x = [359, 0, 1]
    y = [-10, 10]
    X, Y = np.meshgrid(x, y)
    Z = np.zeros(X.shape)
    with pytest.warns(UserWarning,
                      match='are not monotonically increasing or decreasing'):
        ax.pcolormesh(X, Y, Z, shading='auto')


@check_figures_equal(extensions=["png"])
def test_pcolornearest(fig_test, fig_ref):
    ax = fig_test.subplots()
    x = np.arange(0, 10)
    y = np.arange(0, 3)
    np.random.seed(19680801)
    Z = np.random.randn(2, 9)
    ax.pcolormesh(x, y, Z, shading='flat')

    ax = fig_ref.subplots()
    # specify the centers
    x2 = x[:-1] + np.diff(x) / 2
    y2 = y[:-1] + np.diff(y) / 2
    ax.pcolormesh(x2, y2, Z, shading='nearest')


@check_figures_equal(extensions=["png"])
def test_pcolornearestunits(fig_test, fig_ref):
    ax = fig_test.subplots()
    x = [datetime.datetime.fromtimestamp(x * 3600) for x in range(10)]
    y = np.arange(0, 3)
    np.random.seed(19680801)
    Z = np.random.randn(2, 9)
    ax.pcolormesh(x, y, Z, shading='flat')

    ax = fig_ref.subplots()
    # specify the centers
    x2 = [datetime.datetime.fromtimestamp((x + 0.5) * 3600) for x in range(9)]
    y2 = y[:-1] + np.diff(y) / 2
    ax.pcolormesh(x2, y2, Z, shading='nearest')


def test_pcolorflaterror():
    fig, ax = plt.subplots()
    x = np.arange(0, 9)
    y = np.arange(0, 3)
    np.random.seed(19680801)
    Z = np.random.randn(3, 9)
    with pytest.raises(TypeError, match='Dimensions of C'):
        ax.pcolormesh(x, y, Z, shading='flat')


@pytest.mark.parametrize('snap', [False, True])
@check_figures_equal(extensions=["png"])
def test_pcolorauto(fig_test, fig_ref, snap):
    ax = fig_test.subplots()
    x = np.arange(0, 10)
    y = np.arange(0, 4)
    np.random.seed(19680801)
    Z = np.random.randn(3, 9)
    # this is the same as flat; note that auto is default
    ax.pcolormesh(x, y, Z, snap=snap)

    ax = fig_ref.subplots()
    # specify the centers
    x2 = x[:-1] + np.diff(x) / 2
    y2 = y[:-1] + np.diff(y) / 2
    # this is same as nearest:
    ax.pcolormesh(x2, y2, Z, snap=snap)


@image_comparison(['canonical'])
def test_canonical():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])


@image_comparison(['arc_angles.png'], remove_text=True, style='default')
def test_arc_angles():
    # Ellipse parameters
    w = 2
    h = 1
    centre = (0.2, 0.5)
    scale = 2

    fig, axs = plt.subplots(3, 3)
    for i, ax in enumerate(axs.flat):
        theta2 = i * 360 / 9
        theta1 = theta2 - 45

        ax.add_patch(mpatches.Ellipse(centre, w, h, alpha=0.3))
        ax.add_patch(mpatches.Arc(centre, w, h, theta1=theta1, theta2=theta2))
        # Straight lines intersecting start and end of arc
        ax.plot([scale * np.cos(np.deg2rad(theta1)) + centre[0],
                 centre[0],
                 scale * np.cos(np.deg2rad(theta2)) + centre[0]],
                [scale * np.sin(np.deg2rad(theta1)) + centre[1],
                 centre[1],
                 scale * np.sin(np.deg2rad(theta2)) + centre[1]])

        ax.set_xlim(-scale, scale)
        ax.set_ylim(-scale, scale)

        # This looks the same, but it triggers a different code path when it
        # gets large enough.
        w *= 10
        h *= 10
        centre = (centre[0] * 10, centre[1] * 10)
        scale *= 10


@image_comparison(['arc_ellipse'], remove_text=True)
def test_arc_ellipse():
    xcenter, ycenter = 0.38, 0.52
    width, height = 1e-1, 3e-1
    angle = -30

    theta = np.deg2rad(np.arange(360))
    x = width / 2. * np.cos(theta)
    y = height / 2. * np.sin(theta)

    rtheta = np.deg2rad(angle)
    R = np.array([
        [np.cos(rtheta), -np.sin(rtheta)],
        [np.sin(rtheta), np.cos(rtheta)]])

    x, y = np.dot(R, np.array([x, y]))
    x += xcenter
    y += ycenter

    fig = plt.figure()
    ax = fig.add_subplot(211, aspect='auto')
    ax.fill(x, y, alpha=0.2, facecolor='yellow', edgecolor='yellow',
            linewidth=1, zorder=1)

    e1 = mpatches.Arc((xcenter, ycenter), width, height,
                      angle=angle, linewidth=2, fill=False, zorder=2)

    ax.add_patch(e1)

    ax = fig.add_subplot(212, aspect='equal')
    ax.fill(x, y, alpha=0.2, facecolor='green', edgecolor='green', zorder=1)
    e2 = mpatches.Arc((xcenter, ycenter), width, height,
                      angle=angle, linewidth=2, fill=False, zorder=2)

    ax.add_patch(e2)


def test_marker_as_markerstyle():
    fix, ax = plt.subplots()
    m = mmarkers.MarkerStyle('o')
    ax.plot([1, 2, 3], [3, 2, 1], marker=m)
    ax.scatter([1, 2, 3], [4, 3, 2], marker=m)
    ax.errorbar([1, 2, 3], [5, 4, 3], marker=m)


@image_comparison(['markevery'], remove_text=True)
def test_markevery():
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * np.sqrt(x/10 + 0.5)

    # check marker only plot
    fig, ax = plt.subplots()
    ax.plot(x, y, 'o', label='default')
    ax.plot(x, y, 'd', markevery=None, label='mark all')
    ax.plot(x, y, 's', markevery=10, label='mark every 10')
    ax.plot(x, y, '+', markevery=(5, 20), label='mark every 5 starting at 10')
    ax.legend()


@image_comparison(['markevery_line'], remove_text=True, tol=0.005)
def test_markevery_line():
    # TODO: a slight change in rendering between Inkscape versions may explain
    # why one had to introduce a small non-zero tolerance for the SVG test
    # to pass. One may try to remove this hack once Travis' Inkscape version
    # is modern enough. FWIW, no failure with 0.92.3 on my computer (#11358).
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * np.sqrt(x/10 + 0.5)

    # check line/marker combos
    fig, ax = plt.subplots()
    ax.plot(x, y, '-o', label='default')
    ax.plot(x, y, '-d', markevery=None, label='mark all')
    ax.plot(x, y, '-s', markevery=10, label='mark every 10')
    ax.plot(x, y, '-+', markevery=(5, 20), label='mark every 5 starting at 10')
    ax.legend()


@image_comparison(['markevery_linear_scales'], remove_text=True, tol=0.001)
def test_markevery_linear_scales():
    cases = [None,
             8,
             (30, 8),
             [16, 24, 30], [0, -1],
             slice(100, 200, 3),
             0.1, 0.3, 1.5,
             (0.0, 0.1), (0.45, 0.1)]

    cols = 3
    gs = matplotlib.gridspec.GridSpec(len(cases) // cols + 1, cols)

    delta = 0.11
    x = np.linspace(0, 10 - 2 * delta, 200) + delta
    y = np.sin(x) + 1.0 + delta

    for i, case in enumerate(cases):
        row = (i // cols)
        col = i % cols
        plt.subplot(gs[row, col])
        plt.title('markevery=%s' % str(case))
        plt.plot(x, y, 'o', ls='-', ms=4,  markevery=case)


@image_comparison(['markevery_linear_scales_zoomed'], remove_text=True)
def test_markevery_linear_scales_zoomed():
    cases = [None,
             8,
             (30, 8),
             [16, 24, 30], [0, -1],
             slice(100, 200, 3),
             0.1, 0.3, 1.5,
             (0.0, 0.1), (0.45, 0.1)]

    cols = 3
    gs = matplotlib.gridspec.GridSpec(len(cases) // cols + 1, cols)

    delta = 0.11
    x = np.linspace(0, 10 - 2 * delta, 200) + delta
    y = np.sin(x) + 1.0 + delta

    for i, case in enumerate(cases):
        row = (i // cols)
        col = i % cols
        plt.subplot(gs[row, col])
        plt.title('markevery=%s' % str(case))
        plt.plot(x, y, 'o', ls='-', ms=4,  markevery=case)
        plt.xlim((6, 6.7))
        plt.ylim((1.1, 1.7))


@image_comparison(['markevery_log_scales'], remove_text=True)
def test_markevery_log_scales():
    cases = [None,
             8,
             (30, 8),
             [16, 24, 30], [0, -1],
             slice(100, 200, 3),
             0.1, 0.3, 1.5,
             (0.0, 0.1), (0.45, 0.1)]

    cols = 3
    gs = matplotlib.gridspec.GridSpec(len(cases) // cols + 1, cols)

    delta = 0.11
    x = np.linspace(0, 10 - 2 * delta, 200) + delta
    y = np.sin(x) + 1.0 + delta

    for i, case in enumerate(cases):
        row = (i // cols)
        col = i % cols
        plt.subplot(gs[row, col])
        plt.title('markevery=%s' % str(case))
        plt.xscale('log')
        plt.yscale('log')
        plt.plot(x, y, 'o', ls='-', ms=4,  markevery=case)


@image_comparison(['markevery_polar'], style='default', remove_text=True)
def test_markevery_polar():
    cases = [None,
             8,
             (30, 8),
             [16, 24, 30], [0, -1],
             slice(100, 200, 3),
             0.1, 0.3, 1.5,
             (0.0, 0.1), (0.45, 0.1)]

    cols = 3
    gs = matplotlib.gridspec.GridSpec(len(cases) // cols + 1, cols)

    r = np.linspace(0, 3.0, 200)
    theta = 2 * np.pi * r

    for i, case in enumerate(cases):
        row = (i // cols)
        col = i % cols
        plt.subplot(gs[row, col], polar=True)
        plt.title('markevery=%s' % str(case))
        plt.plot(theta, r, 'o', ls='-', ms=4,  markevery=case)


@image_comparison(['marker_edges'], remove_text=True)
def test_marker_edges():
    x = np.linspace(0, 1, 10)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), 'y.', ms=30.0, mew=0, mec='r')
    ax.plot(x+0.1, np.sin(x), 'y.', ms=30.0, mew=1, mec='r')
    ax.plot(x+0.2, np.sin(x), 'y.', ms=30.0, mew=2, mec='b')


@image_comparison(['bar_tick_label_single.png', 'bar_tick_label_single.png'])
def test_bar_tick_label_single():
    # From 2516: plot bar with array of string labels for x axis
    ax = plt.gca()
    ax.bar(0, 1, align='edge', tick_label='0')

    # Reuse testcase from above for a labeled data test
    data = {"a": 0, "b": 1}
    fig, ax = plt.subplots()
    ax = plt.gca()
    ax.bar("a", "b", align='edge', tick_label='0', data=data)


def test_nan_bar_values():
    fig, ax = plt.subplots()
    ax.bar([0, 1], [np.nan, 4])


def test_bar_ticklabel_fail():
    fig, ax = plt.subplots()
    ax.bar([], [])


@image_comparison(['bar_tick_label_multiple.png'])
def test_bar_tick_label_multiple():
    # From 2516: plot bar with array of string labels for x axis
    ax = plt.gca()
    ax.bar([1, 2.5], [1, 2], width=[0.2, 0.5], tick_label=['a', 'b'],
           align='center')


@image_comparison(['bar_tick_label_multiple_old_label_alignment.png'])
def test_bar_tick_label_multiple_old_alignment():
    # Test that the alignment for class is backward compatible
    matplotlib.rcParams["ytick.alignment"] = "center"
    ax = plt.gca()
    ax.bar([1, 2.5], [1, 2], width=[0.2, 0.5], tick_label=['a', 'b'],
           align='center')


@check_figures_equal(extensions=["png"])
def test_bar_decimal_center(fig_test, fig_ref):
    ax = fig_test.subplots()
    x0 = [1.5, 8.4, 5.3, 4.2]
    y0 = [1.1, 2.2, 3.3, 4.4]
    x = [Decimal(x) for x in x0]
    y = [Decimal(y) for y in y0]
    # Test image - vertical, align-center bar chart with Decimal() input
    ax.bar(x, y, align='center')
    # Reference image
    ax = fig_ref.subplots()
    ax.bar(x0, y0, align='center')


@check_figures_equal(extensions=["png"])
def test_barh_decimal_center(fig_test, fig_ref):
    ax = fig_test.subplots()
    x0 = [1.5, 8.4, 5.3, 4.2]
    y0 = [1.1, 2.2, 3.3, 4.4]
    x = [Decimal(x) for x in x0]
    y = [Decimal(y) for y in y0]
    # Test image - horizontal, align-center bar chart with Decimal() input
    ax.barh(x, y, height=[0.5, 0.5, 1, 1], align='center')
    # Reference image
    ax = fig_ref.subplots()
    ax.barh(x0, y0, height=[0.5, 0.5, 1, 1], align='center')


@check_figures_equal(extensions=["png"])
def test_bar_decimal_width(fig_test, fig_ref):
    x = [1.5, 8.4, 5.3, 4.2]
    y = [1.1, 2.2, 3.3, 4.4]
    w0 = [0.7, 1.45, 1, 2]
    w = [Decimal(i) for i in w0]
    # Test image - vertical bar chart with Decimal() width
    ax = fig_test.subplots()
    ax.bar(x, y, width=w, align='center')
    # Reference image
    ax = fig_ref.subplots()
    ax.bar(x, y, width=w0, align='center')


@check_figures_equal(extensions=["png"])
def test_barh_decimal_height(fig_test, fig_ref):
    x = [1.5, 8.4, 5.3, 4.2]
    y = [1.1, 2.2, 3.3, 4.4]
    h0 = [0.7, 1.45, 1, 2]
    h = [Decimal(i) for i in h0]
    # Test image - horizontal bar chart with Decimal() height
    ax = fig_test.subplots()
    ax.barh(x, y, height=h, align='center')
    # Reference image
    ax = fig_ref.subplots()
    ax.barh(x, y, height=h0, align='center')


def test_bar_color_none_alpha():
    ax = plt.gca()
    rects = ax.bar([1, 2], [2, 4], alpha=0.3, color='none', edgecolor='r')
    for rect in rects:
        assert rect.get_facecolor() == (0, 0, 0, 0)
        assert rect.get_edgecolor() == (1, 0, 0, 0.3)


def test_bar_edgecolor_none_alpha():
    ax = plt.gca()
    rects = ax.bar([1, 2], [2, 4], alpha=0.3, color='r', edgecolor='none')
    for rect in rects:
        assert rect.get_facecolor() == (1, 0, 0, 0.3)
        assert rect.get_edgecolor() == (0, 0, 0, 0)


@image_comparison(['barh_tick_label.png'])
def test_barh_tick_label():
    # From 2516: plot barh with array of string labels for y axis
    ax = plt.gca()
    ax.barh([1, 2.5], [1, 2], height=[0.2, 0.5], tick_label=['a', 'b'],
            align='center')


def test_bar_timedelta():
    """Smoketest that bar can handle width and height in delta units."""
    fig, ax = plt.subplots()
    ax.bar(datetime.datetime(2018, 1, 1), 1.,
           width=datetime.timedelta(hours=3))
    ax.bar(datetime.datetime(2018, 1, 1), 1.,
           xerr=datetime.timedelta(hours=2),
           width=datetime.timedelta(hours=3))
    fig, ax = plt.subplots()
    ax.barh(datetime.datetime(2018, 1, 1), 1,
            height=datetime.timedelta(hours=3))
    ax.barh(datetime.datetime(2018, 1, 1), 1,
            height=datetime.timedelta(hours=3),
            yerr=datetime.timedelta(hours=2))
    fig, ax = plt.subplots()
    ax.barh([datetime.datetime(2018, 1, 1), datetime.datetime(2018, 1, 1)],
            np.array([1, 1.5]),
            height=datetime.timedelta(hours=3))
    ax.barh([datetime.datetime(2018, 1, 1), datetime.datetime(2018, 1, 1)],
            np.array([1, 1.5]),
            height=[datetime.timedelta(hours=t) for t in [1, 2]])
    ax.broken_barh([(datetime.datetime(2018, 1, 1),
                     datetime.timedelta(hours=1))],
                   (10, 20))


def test_boxplot_dates_pandas(pd):
    # smoke test for boxplot and dates in pandas
    data = np.random.rand(5, 2)
    years = pd.date_range('1/1/2000',
                          periods=2, freq=pd.DateOffset(years=1)).year
    plt.figure()
    plt.boxplot(data, positions=years)


def test_pcolor_regression(pd):
    from pandas.plotting import (
        register_matplotlib_converters,
        deregister_matplotlib_converters,
    )

    fig = plt.figure()
    ax = fig.add_subplot(111)

    times = [datetime.datetime(2021, 1, 1)]
    while len(times) < 7:
        times.append(times[-1] + datetime.timedelta(seconds=120))

    y_vals = np.arange(5)

    time_axis, y_axis = np.meshgrid(times, y_vals)
    shape = (len(y_vals) - 1, len(times) - 1)
    z_data = np.arange(shape[0] * shape[1])

    z_data.shape = shape
    try:
        register_matplotlib_converters()

        im = ax.pcolormesh(time_axis, y_axis, z_data)
        # make sure this does not raise!
        fig.canvas.draw()
    finally:
        deregister_matplotlib_converters()


def test_bar_pandas(pd):
    # Smoke test for pandas
    df = pd.DataFrame(
        {'year': [2018, 2018, 2018],
         'month': [1, 1, 1],
         'day': [1, 2, 3],
         'value': [1, 2, 3]})
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])

    monthly = df[['date', 'value']].groupby(['date']).sum()
    dates = monthly.index
    forecast = monthly['value']
    baseline = monthly['value']

    fig, ax = plt.subplots()
    ax.bar(dates, forecast, width=10, align='center')
    ax.plot(dates, baseline, color='orange', lw=4)


def test_bar_pandas_indexed(pd):
    # Smoke test for indexed pandas
    df = pd.DataFrame({"x": [1., 2., 3.], "width": [.2, .4, .6]},
                      index=[1, 2, 3])
    fig, ax = plt.subplots()
    ax.bar(df.x, 1., width=df.width)


@mpl.style.context('default')
@check_figures_equal()
def test_bar_hatches(fig_test, fig_ref):
    ax_test = fig_test.subplots()
    ax_ref = fig_ref.subplots()

    x = [1, 2]
    y = [2, 3]
    hatches = ['x', 'o']
    for i in range(2):
        ax_ref.bar(x[i], y[i], color='C0', hatch=hatches[i])

    ax_test.bar(x, y, hatch=hatches)


def test_pandas_minimal_plot(pd):
    # smoke test that series and index objcets do not warn
    for x in [pd.Series([1, 2], dtype="float64"),
              pd.Series([1, 2], dtype="Float64")]:
        plt.plot(x, x)
        plt.plot(x.index, x)
        plt.plot(x)
        plt.plot(x.index)
    df = pd.DataFrame({'col': [1, 2, 3]})
    plt.plot(df)
    plt.plot(df, df)


@image_comparison(['hist_log'], remove_text=True)
def test_hist_log():
    data0 = np.linspace(0, 1, 200)**3
    data = np.concatenate([1 - data0, 1 + data0])
    fig, ax = plt.subplots()
    ax.hist(data, fill=False, log=True)


@check_figures_equal(extensions=["png"])
def test_hist_log_2(fig_test, fig_ref):
    axs_test = fig_test.subplots(2, 3)
    axs_ref = fig_ref.subplots(2, 3)
    for i, histtype in enumerate(["bar", "step", "stepfilled"]):
        # Set log scale, then call hist().
        axs_test[0, i].set_yscale("log")
        axs_test[0, i].hist(1, 1, histtype=histtype)
        # Call hist(), then set log scale.
        axs_test[1, i].hist(1, 1, histtype=histtype)
        axs_test[1, i].set_yscale("log")
        # Use hist(..., log=True).
        for ax in axs_ref[:, i]:
            ax.hist(1, 1, log=True, histtype=histtype)


def test_hist_log_barstacked():
    fig, axs = plt.subplots(2)
    axs[0].hist([[0], [0, 1]], 2, histtype="barstacked")
    axs[0].set_yscale("log")
    axs[1].hist([0, 0, 1], 2, histtype="barstacked")
    axs[1].set_yscale("log")
    fig.canvas.draw()
    assert axs[0].get_ylim() == axs[1].get_ylim()


@image_comparison(['hist_bar_empty.png'], remove_text=True)
def test_hist_bar_empty():
    # From #3886: creating hist from empty dataset raises ValueError
    ax = plt.gca()
    ax.hist([], histtype='bar')


@image_comparison(['hist_step_empty.png'], remove_text=True)
def test_hist_step_empty():
    # From #3886: creating hist from empty dataset raises ValueError
    ax = plt.gca()
    ax.hist([], histtype='step')


@image_comparison(['hist_step_filled.png'], remove_text=True)
def test_hist_step_filled():
    np.random.seed(0)
    x = np.random.randn(1000, 3)
    n_bins = 10

    kwargs = [{'fill': True}, {'fill': False}, {'fill': None}, {}]*2
    types = ['step']*4+['stepfilled']*4
    fig, axs = plt.subplots(nrows=2, ncols=4)

    for kg, _type, ax in zip(kwargs, types, axs.flat):
        ax.hist(x, n_bins, histtype=_type, stacked=True, **kg)
        ax.set_title('%s/%s' % (kg, _type))
        ax.set_ylim(bottom=-50)

    patches = axs[0, 0].patches
    assert all(p.get_facecolor() == p.get_edgecolor() for p in patches)


@image_comparison(['hist_density.png'])
def test_hist_density():
    np.random.seed(19680801)
    data = np.random.standard_normal(2000)
    fig, ax = plt.subplots()
    ax.hist(data, density=True)


def test_hist_unequal_bins_density():
    # Test correct behavior of normalized histogram with unequal bins
    # https://github.com/matplotlib/matplotlib/issues/9557
    rng = np.random.RandomState(57483)
    t = rng.randn(100)
    bins = [-3, -1, -0.5, 0, 1, 5]
    mpl_heights, _, _ = plt.hist(t, bins=bins, density=True)
    np_heights, _ = np.histogram(t, bins=bins, density=True)
    assert_allclose(mpl_heights, np_heights)


def test_hist_datetime_datasets():
    data = [[datetime.datetime(2017, 1, 1), datetime.datetime(2017, 1, 1)],
            [datetime.datetime(2017, 1, 1), datetime.datetime(2017, 1, 2)]]
    fig, ax = plt.subplots()
    ax.hist(data, stacked=True)
    ax.hist(data, stacked=False)


@pytest.mark.parametrize("bins_preprocess",
                         [mpl.dates.date2num,
                          lambda bins: bins,
                          lambda bins: np.asarray(bins).astype('datetime64')],
                         ids=['date2num', 'datetime.datetime',
                              'np.datetime64'])
def test_hist_datetime_datasets_bins(bins_preprocess):
    data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11),
             datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)],
            [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5),
             datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]

    date_edges = [datetime.datetime(2019, 1, 1), datetime.datetime(2019, 2, 1),
                  datetime.datetime(2019, 3, 1)]

    fig, ax = plt.subplots()
    _, bins, _ = ax.hist(data, bins=bins_preprocess(date_edges), stacked=True)
    np.testing.assert_allclose(bins, mpl.dates.date2num(date_edges))

    _, bins, _ = ax.hist(data, bins=bins_preprocess(date_edges), stacked=False)
    np.testing.assert_allclose(bins, mpl.dates.date2num(date_edges))


@pytest.mark.parametrize('data, expected_number_of_hists',
                         [([], 1),
                          ([[]], 1),
                          ([[], []], 2)])
def test_hist_with_empty_input(data, expected_number_of_hists):
    hists, _, _ = plt.hist(data)
    hists = np.asarray(hists)

    if hists.ndim == 1:
        assert 1 == expected_number_of_hists
    else:
        assert hists.shape[0] == expected_number_of_hists


@pytest.mark.parametrize("histtype, zorder",
                         [("bar", mpl.patches.Patch.zorder),
                          ("step", mpl.lines.Line2D.zorder),
                          ("stepfilled", mpl.patches.Patch.zorder)])
def test_hist_zorder(histtype, zorder):
    ax = plt.figure().add_subplot()
    ax.hist([1, 2], histtype=histtype)
    assert ax.patches
    for patch in ax.patches:
        assert patch.get_zorder() == zorder


@check_figures_equal(extensions=['png'])
def test_stairs(fig_test, fig_ref):
    import matplotlib.lines as mlines
    y = np.array([6, 14, 32, 37, 48, 32, 21,  4])  # hist
    x = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9.])  # bins

    test_axes = fig_test.subplots(3, 2).flatten()
    test_axes[0].stairs(y, x, baseline=None)
    test_axes[1].stairs(y, x, baseline=None, orientation='horizontal')
    test_axes[2].stairs(y, x)
    test_axes[3].stairs(y, x, orientation='horizontal')
    test_axes[4].stairs(y, x)
    test_axes[4].semilogy()
    test_axes[5].stairs(y, x, orientation='horizontal')
    test_axes[5].semilogx()

    # defaults of `PathPatch` to be used for all following Line2D
    style = {'solid_joinstyle': 'miter', 'solid_capstyle': 'butt'}

    ref_axes = fig_ref.subplots(3, 2).flatten()
    ref_axes[0].plot(x, np.append(y, y[-1]), drawstyle='steps-post', **style)
    ref_axes[1].plot(np.append(y[0], y), x, drawstyle='steps-post', **style)

    ref_axes[2].plot(x, np.append(y, y[-1]), drawstyle='steps-post', **style)
    ref_axes[2].add_line(mlines.Line2D([x[0], x[0]], [0, y[0]], **style))
    ref_axes[2].add_line(mlines.Line2D([x[-1], x[-1]], [0, y[-1]], **style))
    ref_axes[2].set_ylim(0, None)

    ref_axes[3].plot(np.append(y[0], y), x, drawstyle='steps-post', **style)
    ref_axes[3].add_line(mlines.Line2D([0, y[0]], [x[0], x[0]], **style))
    ref_axes[3].add_line(mlines.Line2D([0, y[-1]], [x[-1], x[-1]], **style))
    ref_axes[3].set_xlim(0, None)

    ref_axes[4].plot(x, np.append(y, y[-1]), drawstyle='steps-post', **style)
    ref_axes[4].add_line(mlines.Line2D([x[0], x[0]], [0, y[0]], **style))
    ref_axes[4].add_line(mlines.Line2D([x[-1], x[-1]], [0, y[-1]], **style))
    ref_axes[4].semilogy()

    ref_axes[5].plot(np.append(y[0], y), x, drawstyle='steps-post', **style)
    ref_axes[5].add_line(mlines.Line2D([0, y[0]], [x[0], x[0]], **style))
    ref_axes[5].add_line(mlines.Line2D([0, y[-1]], [x[-1], x[-1]], **style))
    ref_axes[5].semilogx()


@check_figures_equal(extensions=['png'])
def test_stairs_fill(fig_test, fig_ref):
    h, bins = [1, 2, 3, 4, 2], [0, 1, 2, 3, 4, 5]
    bs = -2
    # Test
    test_axes = fig_test.subplots(2, 2).flatten()
    test_axes[0].stairs(h, bins, fill=True)
    test_axes[1].stairs(h, bins, orientation='horizontal', fill=True)
    test_axes[2].stairs(h, bins, baseline=bs, fill=True)
    test_axes[3].stairs(h, bins, baseline=bs, orientation='horizontal',
                        fill=True)

    # # Ref
    ref_axes = fig_ref.subplots(2, 2).flatten()
    ref_axes[0].fill_between(bins, np.append(h, h[-1]), step='post', lw=0)
    ref_axes[0].set_ylim(0, None)
    ref_axes[1].fill_betweenx(bins, np.append(h, h[-1]), step='post', lw=0)
    ref_axes[1].set_xlim(0, None)
    ref_axes[2].fill_between(bins, np.append(h, h[-1]),
                             np.ones(len(h)+1)*bs, step='post', lw=0)
    ref_axes[2].set_ylim(bs, None)
    ref_axes[3].fill_betweenx(bins, np.append(h, h[-1]),
                              np.ones(len(h)+1)*bs, step='post', lw=0)
    ref_axes[3].set_xlim(bs, None)


@check_figures_equal(extensions=['png'])
def test_stairs_update(fig_test, fig_ref):
    # fixed ylim because stairs() does autoscale, but updating data does not
    ylim = -3, 4
    # Test
    test_ax = fig_test.add_subplot()
    h = test_ax.stairs([1, 2, 3])
    test_ax.set_ylim(ylim)
    h.set_data([3, 2, 1])
    h.set_data(edges=np.arange(4)+2)
    h.set_data([1, 2, 1], np.arange(4)/2)
    h.set_data([1, 2, 3])
    h.set_data(None, np.arange(4))
    assert np.allclose(h.get_data()[0], np.arange(1, 4))
    assert np.allclose(h.get_data()[1], np.arange(4))
    h.set_data(baseline=-2)
    assert h.get_data().baseline == -2

    # Ref
    ref_ax = fig_ref.add_subplot()
    h = ref_ax.stairs([1, 2, 3], baseline=-2)
    ref_ax.set_ylim(ylim)


@check_figures_equal(extensions=['png'])
def test_stairs_baseline_0(fig_test, fig_ref):
    # Test
    test_ax = fig_test.add_subplot()
    test_ax.stairs([5, 6, 7], baseline=None)

    # Ref
    ref_ax = fig_ref.add_subplot()
    style = {'solid_joinstyle': 'miter', 'solid_capstyle': 'butt'}
    ref_ax.plot(range(4), [5, 6, 7, 7], drawstyle='steps-post', **style)
    ref_ax.set_ylim(0, None)


def test_stairs_empty():
    ax = plt.figure().add_subplot()
    ax.stairs([], [42])
    assert ax.get_xlim() == (39, 45)
    assert ax.get_ylim() == (-0.06, 0.06)


def test_stairs_invalid_nan():
    with pytest.raises(ValueError, match='Nan values in "edges"'):
        plt.stairs([1, 2], [0, np.nan, 1])


def test_stairs_invalid_mismatch():
    with pytest.raises(ValueError, match='Size mismatch'):
        plt.stairs([1, 2], [0, 1])


def test_stairs_invalid_update():
    h = plt.stairs([1, 2], [0, 1, 2])
    with pytest.raises(ValueError, match='Nan values in "edges"'):
        h.set_data(edges=[1, np.nan, 2])


def test_stairs_invalid_update2():
    h = plt.stairs([1, 2], [0, 1, 2])
    with pytest.raises(ValueError, match='Size mismatch'):
        h.set_data(edges=np.arange(5))


@image_comparison(['test_stairs_options.png'], remove_text=True)
def test_stairs_options():
    x, y = np.array([1, 2, 3, 4, 5]), np.array([1, 2, 3, 4]).astype(float)
    yn = y.copy()
    yn[1] = np.nan

    fig, ax = plt.subplots()
    ax.stairs(y*3, x, color='green', fill=True, label="A")
    ax.stairs(y, x*3-3, color='red', fill=True,
              orientation='horizontal', label="B")
    ax.stairs(yn, x, color='orange', ls='--', lw=2, label="C")
    ax.stairs(yn/3, x*3-2, ls='--', lw=2, baseline=0.5,
              orientation='horizontal', label="D")
    ax.stairs(y[::-1]*3+13, x-1, color='red', ls='--', lw=2, baseline=None,
              label="E")
    ax.stairs(y[::-1]*3+14, x, baseline=26,
              color='purple', ls='--', lw=2, label="F")
    ax.stairs(yn[::-1]*3+15, x+1, baseline=np.linspace(27, 25, len(y)),
              color='blue', ls='--', label="G", fill=True)
    ax.stairs(y[:-1][::-1]*2+11, x[:-1]+0.5, color='black', ls='--', lw=2,
              baseline=12, hatch='//', label="H")
    ax.legend(loc=0)


@image_comparison(['test_stairs_datetime.png'])
def test_stairs_datetime():
    f, ax = plt.subplots(constrained_layout=True)
    ax.stairs(np.arange(36),
              np.arange(np.datetime64('2001-12-27'),
                        np.datetime64('2002-02-02')))
    plt.xticks(rotation=30)


@check_figures_equal(extensions=['png'])
def test_stairs_edge_handling(fig_test, fig_ref):
    # Test
    test_ax = fig_test.add_subplot()
    test_ax.stairs([1, 2, 3], color='red', fill=True)

    # Ref
    ref_ax = fig_ref.add_subplot()
    st = ref_ax.stairs([1, 2, 3], fill=True)
    st.set_color('red')


def contour_dat():
    x = np.linspace(-3, 5, 150)
    y = np.linspace(-3, 5, 120)
    z = np.cos(x) + np.sin(y[:, np.newaxis])
    return x, y, z


@image_comparison(['contour_hatching'], remove_text=True, style='mpl20')
def test_contour_hatching():
    x, y, z = contour_dat()
    fig, ax = plt.subplots()
    ax.contourf(x, y, z, 7, hatches=['/', '\\', '//', '-'],
                cmap=plt.get_cmap('gray'),
                extend='both', alpha=0.5)


@image_comparison(['contour_colorbar'], style='mpl20')
def test_contour_colorbar():
    x, y, z = contour_dat()

    fig, ax = plt.subplots()
    cs = ax.contourf(x, y, z, levels=np.arange(-1.8, 1.801, 0.2),
                     cmap=plt.get_cmap('RdBu'),
                     vmin=-0.6,
                     vmax=0.6,
                     extend='both')
    cs1 = ax.contour(x, y, z, levels=np.arange(-2.2, -0.599, 0.2),
                     colors=['y'],
                     linestyles='solid',
                     linewidths=2)
    cs2 = ax.contour(x, y, z, levels=np.arange(0.6, 2.2, 0.2),
                     colors=['c'],
                     linewidths=2)
    cbar = fig.colorbar(cs, ax=ax)
    cbar.add_lines(cs1)
    cbar.add_lines(cs2, erase=False)


@image_comparison(['hist2d', 'hist2d'], remove_text=True, style='mpl20')
def test_hist2d():
    # Remove this line when this test image is regenerated.
    plt.rcParams['pcolormesh.snap'] = False

    np.random.seed(0)
    # make it not symmetric in case we switch x and y axis
    x = np.random.randn(100)*2+5
    y = np.random.randn(100)-2
    fig, ax = plt.subplots()
    ax.hist2d(x, y, bins=10, rasterized=True)

    # Reuse testcase from above for a labeled data test
    data = {"x": x, "y": y}
    fig, ax = plt.subplots()
    ax.hist2d("x", "y", bins=10, data=data, rasterized=True)


@image_comparison(['hist2d_transpose'], remove_text=True, style='mpl20')
def test_hist2d_transpose():
    # Remove this line when this test image is regenerated.
    plt.rcParams['pcolormesh.snap'] = False

    np.random.seed(0)
    # make sure the output from np.histogram is transposed before
    # passing to pcolorfast
    x = np.array([5]*100)
    y = np.random.randn(100)-2
    fig, ax = plt.subplots()
    ax.hist2d(x, y, bins=10, rasterized=True)


def test_hist2d_density():
    x, y = np.random.random((2, 100))
    ax = plt.figure().subplots()
    for obj in [ax, plt]:
        obj.hist2d(x, y, density=True)


class TestScatter:
    @image_comparison(['scatter'], style='mpl20', remove_text=True)
    def test_scatter_plot(self):
        data = {"x": np.array([3, 4, 2, 6]), "y": np.array([2, 5, 2, 3]),
                "c": ['r', 'y', 'b', 'lime'], "s": [24, 15, 19, 29],
                "c2": ['0.5', '0.6', '0.7', '0.8']}

        fig, ax = plt.subplots()
        ax.scatter(data["x"] - 1., data["y"] - 1., c=data["c"], s=data["s"])
        ax.scatter(data["x"] + 1., data["y"] + 1., c=data["c2"], s=data["s"])
        ax.scatter("x", "y", c="c", s="s", data=data)

    @image_comparison(['scatter_marker.png'], remove_text=True)
    def test_scatter_marker(self):
        fig, (ax0, ax1, ax2) = plt.subplots(ncols=3)
        ax0.scatter([3, 4, 2, 6], [2, 5, 2, 3],
                    c=[(1, 0, 0), 'y', 'b', 'lime'],
                    s=[60, 50, 40, 30],
                    edgecolors=['k', 'r', 'g', 'b'],
                    marker='s')
        ax1.scatter([3, 4, 2, 6], [2, 5, 2, 3],
                    c=[(1, 0, 0), 'y', 'b', 'lime'],
                    s=[60, 50, 40, 30],
                    edgecolors=['k', 'r', 'g', 'b'],
                    marker=mmarkers.MarkerStyle('o', fillstyle='top'))
        # unit area ellipse
        rx, ry = 3, 1
        area = rx * ry * np.pi
        theta = np.linspace(0, 2 * np.pi, 21)
        verts = np.column_stack([np.cos(theta) * rx / area,
                                 np.sin(theta) * ry / area])
        ax2.scatter([3, 4, 2, 6], [2, 5, 2, 3],
                    c=[(1, 0, 0), 'y', 'b', 'lime'],
                    s=[60, 50, 40, 30],
                    edgecolors=['k', 'r', 'g', 'b'],
                    marker=verts)

    @image_comparison(['scatter_2D'], remove_text=True, extensions=['png'])
    def test_scatter_2D(self):
        x = np.arange(3)
        y = np.arange(2)
        x, y = np.meshgrid(x, y)
        z = x + y
        fig, ax = plt.subplots()
        ax.scatter(x, y, c=z, s=200, edgecolors='face')

    @check_figures_equal(extensions=["png"])
    def test_scatter_decimal(self, fig_test, fig_ref):
        x0 = np.array([1.5, 8.4, 5.3, 4.2])
        y0 = np.array([1.1, 2.2, 3.3, 4.4])
        x = np.array([Decimal(i) for i in x0])
        y = np.array([Decimal(i) for i in y0])
        c = ['r', 'y', 'b', 'lime']
        s = [24, 15, 19, 29]
        # Test image - scatter plot with Decimal() input
        ax = fig_test.subplots()
        ax.scatter(x, y, c=c, s=s)
        # Reference image
        ax = fig_ref.subplots()
        ax.scatter(x0, y0, c=c, s=s)

    def test_scatter_color(self):
        # Try to catch cases where 'c' kwarg should have been used.
        with pytest.raises(ValueError):
            plt.scatter([1, 2], [1, 2], color=[0.1, 0.2])
        with pytest.raises(ValueError):
            plt.scatter([1, 2, 3], [1, 2, 3], color=[1, 2, 3])

    def test_scatter_unfilled(self):
        coll = plt.scatter([0, 1, 2], [1, 3, 2], c=['0.1', '0.3', '0.5'],
                           marker=mmarkers.MarkerStyle('o', fillstyle='none'),
                           linewidths=[1.1, 1.2, 1.3])
        assert coll.get_facecolors().shape == (0, 4)  # no facecolors
        assert_array_equal(coll.get_edgecolors(), [[0.1, 0.1, 0.1, 1],
                                                   [0.3, 0.3, 0.3, 1],
                                                   [0.5, 0.5, 0.5, 1]])
        assert_array_equal(coll.get_linewidths(), [1.1, 1.2, 1.3])

    @mpl.style.context('default')
    def test_scatter_unfillable(self):
        coll = plt.scatter([0, 1, 2], [1, 3, 2], c=['0.1', '0.3', '0.5'],
                           marker='x',
                           linewidths=[1.1, 1.2, 1.3])
        assert_array_equal(coll.get_facecolors(), coll.get_edgecolors())
        assert_array_equal(coll.get_edgecolors(), [[0.1, 0.1, 0.1, 1],
                                                   [0.3, 0.3, 0.3, 1],
                                                   [0.5, 0.5, 0.5, 1]])
        assert_array_equal(coll.get_linewidths(), [1.1, 1.2, 1.3])

    def test_scatter_size_arg_size(self):
        x = np.arange(4)
        with pytest.raises(ValueError, match='same size as x and y'):
            plt.scatter(x, x, x[1:])
        with pytest.raises(ValueError, match='same size as x and y'):
            plt.scatter(x[1:], x[1:], x)
        with pytest.raises(ValueError, match='float array-like'):
            plt.scatter(x, x, 'foo')

    def test_scatter_edgecolor_RGB(self):
        # Github issue 19066
        coll = plt.scatter([1, 2, 3], [1, np.nan, np.nan],
                            edgecolor=(1, 0, 0))
        assert mcolors.same_color(coll.get_edgecolor(), (1, 0, 0))
        coll = plt.scatter([1, 2, 3, 4], [1, np.nan, np.nan, 1],
                            edgecolor=(1, 0, 0, 1))
        assert mcolors.same_color(coll.get_edgecolor(), (1, 0, 0, 1))

    @check_figures_equal(extensions=["png"])
    def test_scatter_invalid_color(self, fig_test, fig_ref):
        ax = fig_test.subplots()
        cmap = plt.get_cmap("viridis", 16)
        cmap.set_bad("k", 1)
        # Set a nonuniform size to prevent the last call to `scatter` (plotting
        # the invalid points separately in fig_ref) from using the marker
        # stamping fast path, which would result in slightly offset markers.
        ax.scatter(range(4), range(4),
                   c=[1, np.nan, 2, np.nan], s=[1, 2, 3, 4],
                   cmap=cmap, plotnonfinite=True)
        ax = fig_ref.subplots()
        cmap = plt.get_cmap("viridis", 16)
        ax.scatter([0, 2], [0, 2], c=[1, 2], s=[1, 3], cmap=cmap)
        ax.scatter([1, 3], [1, 3], s=[2, 4], color="k")

    @check_figures_equal(extensions=["png"])
    def test_scatter_no_invalid_color(self, fig_test, fig_ref):
        # With plotninfinite=False we plot only 2 points.
        ax = fig_test.subplots()
        cmap = plt.get_cmap("viridis", 16)
        cmap.set_bad("k", 1)
        ax.scatter(range(4), range(4),
                   c=[1, np.nan, 2, np.nan], s=[1, 2, 3, 4],
                   cmap=cmap, plotnonfinite=False)
        ax = fig_ref.subplots()
        ax.scatter([0, 2], [0, 2], c=[1, 2], s=[1, 3], cmap=cmap)

    def test_scatter_norm_vminvmax(self):
        """Parameters vmin, vmax should error if norm is given."""
        x = [1, 2, 3]
        ax = plt.axes()
        with pytest.raises(ValueError,
                           match="Passing parameters norm and vmin/vmax "
                                 "simultaneously is not supported."):
            ax.scatter(x, x, c=x, norm=mcolors.Normalize(-10, 10),
                       vmin=0, vmax=5)

    @check_figures_equal(extensions=["png"])
    def test_scatter_single_point(self, fig_test, fig_ref):
        ax = fig_test.subplots()
        ax.scatter(1, 1, c=1)
        ax = fig_ref.subplots()
        ax.scatter([1], [1], c=[1])

    @check_figures_equal(extensions=["png"])
    def test_scatter_different_shapes(self, fig_test, fig_ref):
        x = np.arange(10)
        ax = fig_test.subplots()
        ax.scatter(x, x.reshape(2, 5), c=x.reshape(5, 2))
        ax = fig_ref.subplots()
        ax.scatter(x.reshape(5, 2), x, c=x.reshape(2, 5))

    # Parameters for *test_scatter_c*. NB: assuming that the
    # scatter plot will have 4 elements. The tuple scheme is:
    # (*c* parameter case, exception regexp key or None if no exception)
    params_test_scatter_c = [
        # single string:
        ('0.5', None),
        # Single letter-sequences
        (["rgby"], "conversion"),
        # Special cases
        ("red", None),
        ("none", None),
        (None, None),
        (["r", "g", "b", "none"], None),
        # Non-valid color spec (FWIW, 'jaune' means yellow in French)
        ("jaune", "conversion"),
        (["jaune"], "conversion"),  # wrong type before wrong size
        (["jaune"]*4, "conversion"),
        # Value-mapping like
        ([0.5]*3, None),  # should emit a warning for user's eyes though
        ([0.5]*4, None),  # NB: no warning as matching size allows mapping
        ([0.5]*5, "shape"),
        # list of strings:
        (['0.5', '0.4', '0.6', '0.7'], None),
        (['0.5', 'red', '0.6', 'C5'], None),
        (['0.5', 0.5, '0.6', 'C5'], "conversion"),
        # RGB values
        ([[1, 0, 0]], None),
        ([[1, 0, 0]]*3, "shape"),
        ([[1, 0, 0]]*4, None),
        ([[1, 0, 0]]*5, "shape"),
        # RGBA values
        ([[1, 0, 0, 0.5]], None),
        ([[1, 0, 0, 0.5]]*3, "shape"),
        ([[1, 0, 0, 0.5]]*4, None),
        ([[1, 0, 0, 0.5]]*5, "shape"),
        # Mix of valid color specs
        ([[1, 0, 0, 0.5]]*3 + [[1, 0, 0]], None),
        ([[1, 0, 0, 0.5], "red", "0.0"], "shape"),
        ([[1, 0, 0, 0.5], "red", "0.0", "C5"], None),
        ([[1, 0, 0, 0.5], "red", "0.0", "C5", [0, 1, 0]], "shape"),
        # Mix of valid and non valid color specs
        ([[1, 0, 0, 0.5], "red", "jaune"], "conversion"),
        ([[1, 0, 0, 0.5], "red", "0.0", "jaune"], "conversion"),
        ([[1, 0, 0, 0.5], "red", "0.0", "C5", "jaune"], "conversion"),
    ]

    @pytest.mark.parametrize('c_case, re_key', params_test_scatter_c)
    def test_scatter_c(self, c_case, re_key):
        def get_next_color():
            return 'blue'  # currently unused

        xsize = 4
        # Additional checking of *c* (introduced in #11383).
        REGEXP = {
            "shape": "^'c' argument has [0-9]+ elements",  # shape mismatch
            "conversion": "^'c' argument must be a color",  # bad vals
            }

        if re_key is None:
            mpl.axes.Axes._parse_scatter_color_args(
                c=c_case, edgecolors="black", kwargs={}, xsize=xsize,
                get_next_color_func=get_next_color)
        else:
            with pytest.raises(ValueError, match=REGEXP[re_key]):
                mpl.axes.Axes._parse_scatter_color_args(
                    c=c_case, edgecolors="black", kwargs={}, xsize=xsize,
                    get_next_color_func=get_next_color)

    @mpl.style.context('default')
    @check_figures_equal(extensions=["png"])
    def test_scatter_single_color_c(self, fig_test, fig_ref):
        rgb = [[1, 0.5, 0.05]]
        rgba = [[1, 0.5, 0.05, .5]]

        # set via color kwarg
        ax_ref = fig_ref.subplots()
        ax_ref.scatter(np.ones(3), range(3), color=rgb)
        ax_ref.scatter(np.ones(4)*2, range(4), color=rgba)

        # set via broadcasting via c
        ax_test = fig_test.subplots()
        ax_test.scatter(np.ones(3), range(3), c=rgb)
        ax_test.scatter(np.ones(4)*2, range(4), c=rgba)

    def test_scatter_linewidths(self):
        x = np.arange(5)

        fig, ax = plt.subplots()
        for i in range(3):
            pc = ax.scatter(x, np.full(5, i), c=f'C{i}', marker='x', s=100,
                            linewidths=i + 1)
            assert pc.get_linewidths() == i + 1

        pc = ax.scatter(x, np.full(5, 3), c='C3', marker='x', s=100,
                        linewidths=[*range(1, 5), None])
        assert_array_equal(pc.get_linewidths(),
                           [*range(1, 5), mpl.rcParams['lines.linewidth']])


def _params(c=None, xsize=2, *, edgecolors=None, **kwargs):
    return (c, edgecolors, kwargs if kwargs is not None else {}, xsize)
_result = namedtuple('_result', 'c, colors')


@pytest.mark.parametrize(
    'params, expected_result',
    [(_params(),
      _result(c='b', colors=np.array([[0, 0, 1, 1]]))),
     (_params(c='r'),
      _result(c='r', colors=np.array([[1, 0, 0, 1]]))),
     (_params(c='r', colors='b'),
      _result(c='r', colors=np.array([[1, 0, 0, 1]]))),
     # color
     (_params(color='b'),
      _result(c='b', colors=np.array([[0, 0, 1, 1]]))),
     (_params(color=['b', 'g']),
      _result(c=['b', 'g'], colors=np.array([[0, 0, 1, 1], [0, .5, 0, 1]]))),
     ])
def test_parse_scatter_color_args(params, expected_result):
    def get_next_color():
        return 'blue'  # currently unused

    c, colors, _edgecolors = mpl.axes.Axes._parse_scatter_color_args(
        *params, get_next_color_func=get_next_color)
    assert c == expected_result.c
    assert_allclose(colors, expected_result.colors)

del _params
del _result


@pytest.mark.parametrize(
    'kwargs, expected_edgecolors',
    [(dict(), None),
     (dict(c='b'), None),
     (dict(edgecolors='r'), 'r'),
     (dict(edgecolors=['r', 'g']), ['r', 'g']),
     (dict(edgecolor='r'), 'r'),
     (dict(edgecolors='face'), 'face'),
     (dict(edgecolors='none'), 'none'),
     (dict(edgecolor='r', edgecolors='g'), 'r'),
     (dict(c='b', edgecolor='r', edgecolors='g'), 'r'),
     (dict(color='r'), 'r'),
     (dict(color='r', edgecolor='g'), 'g'),
     ])
def test_parse_scatter_color_args_edgecolors(kwargs, expected_edgecolors):
    def get_next_color():
        return 'blue'  # currently unused

    c = kwargs.pop('c', None)
    edgecolors = kwargs.pop('edgecolors', None)
    _, _, result_edgecolors = \
        mpl.axes.Axes._parse_scatter_color_args(
            c, edgecolors, kwargs, xsize=2, get_next_color_func=get_next_color)
    assert result_edgecolors == expected_edgecolors


def test_parse_scatter_color_args_error():
    def get_next_color():
        return 'blue'  # currently unused

    with pytest.raises(ValueError,
                       match="RGBA values should be within 0-1 range"):
        c = np.array([[0.1, 0.2, 0.7], [0.2, 0.4, 1.4]])  # value > 1
        mpl.axes.Axes._parse_scatter_color_args(
            c, None, kwargs={}, xsize=2, get_next_color_func=get_next_color)


def test_as_mpl_axes_api():
    # tests the _as_mpl_axes api
    from matplotlib.projections.polar import PolarAxes

    class Polar:
        def __init__(self):
            self.theta_offset = 0

        def _as_mpl_axes(self):
            # implement the matplotlib axes interface
            return PolarAxes, {'theta_offset': self.theta_offset}

    prj = Polar()
    prj2 = Polar()
    prj2.theta_offset = np.pi
    prj3 = Polar()

    # testing axes creation with plt.axes
    ax = plt.axes([0, 0, 1, 1], projection=prj)
    assert type(ax) == PolarAxes
    with pytest.warns(
            MatplotlibDeprecationWarning,
            match=r'Calling gca\(\) with keyword arguments was deprecated'):
        ax_via_gca = plt.gca(projection=prj)
    assert ax_via_gca is ax
    plt.close()

    # testing axes creation with gca
    with pytest.warns(
            MatplotlibDeprecationWarning,
            match=r'Calling gca\(\) with keyword arguments was deprecated'):
        ax = plt.gca(projection=prj)
    assert type(ax) == mpl.axes._subplots.subplot_class_factory(PolarAxes)
    with pytest.warns(
            MatplotlibDeprecationWarning,
            match=r'Calling gca\(\) with keyword arguments was deprecated'):
        ax_via_gca = plt.gca(projection=prj)
    assert ax_via_gca is ax
    # try getting the axes given a different polar projection
    with pytest.warns(
            MatplotlibDeprecationWarning,
            match=r'Calling gca\(\) with keyword arguments was deprecated'):
        ax_via_gca = plt.gca(projection=prj2)
    assert ax_via_gca is ax
    assert ax.get_theta_offset() == 0
    # try getting the axes given an == (not is) polar projection
    with pytest.warns(
            MatplotlibDeprecationWarning,
            match=r'Calling gca\(\) with keyword arguments was deprecated'):
        ax_via_gca = plt.gca(projection=prj3)
    assert ax_via_gca is ax
    plt.close()

    # testing axes creation with subplot
    ax = plt.subplot(121, projection=prj)
    assert type(ax) == mpl.axes._subplots.subplot_class_factory(PolarAxes)
    plt.close()


def test_pyplot_axes():
    # test focusing of Axes in other Figure
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    plt.sca(ax1)
    assert ax1 is plt.gca()
    assert fig1 is plt.gcf()
    plt.close(fig1)
    plt.close(fig2)


@image_comparison(['log_scales'])
def test_log_scales():
    fig, ax = plt.subplots()
    ax.plot(np.log(np.linspace(0.1, 100)))
    ax.set_yscale('log', base=5.5)
    ax.invert_yaxis()
    ax.set_xscale('log', base=9.0)


def test_log_scales_no_data():
    _, ax = plt.subplots()
    ax.set(xscale="log", yscale="log")
    ax.xaxis.set_major_locator(mticker.MultipleLocator(1))
    assert ax.get_xlim() == ax.get_ylim() == (1, 10)


def test_log_scales_invalid():
    fig, ax = plt.subplots()
    ax.set_xscale('log')
    with pytest.warns(UserWarning, match='Attempted to set non-positive'):
        ax.set_xlim(-1, 10)
    ax.set_yscale('log')
    with pytest.warns(UserWarning, match='Attempted to set non-positive'):
        ax.set_ylim(-1, 10)


@image_comparison(['stackplot_test_image', 'stackplot_test_image'])
def test_stackplot():
    fig = plt.figure()
    x = np.linspace(0, 10, 10)
    y1 = 1.0 * x
    y2 = 2.0 * x + 1
    y3 = 3.0 * x + 2
    ax = fig.add_subplot(1, 1, 1)
    ax.stackplot(x, y1, y2, y3)
    ax.set_xlim((0, 10))
    ax.set_ylim((0, 70))

    # Reuse testcase from above for a labeled data test
    data = {"x": x, "y1": y1, "y2": y2, "y3": y3}
    fig, ax = plt.subplots()
    ax.stackplot("x", "y1", "y2", "y3", data=data)
    ax.set_xlim((0, 10))
    ax.set_ylim((0, 70))


@image_comparison(['stackplot_test_baseline'], remove_text=True)
def test_stackplot_baseline():
    np.random.seed(0)

    def layers(n, m):
        a = np.zeros((m, n))
        for i in range(n):
            for j in range(5):
                x = 1 / (.1 + np.random.random())
                y = 2 * np.random.random() - .5
                z = 10 / (.1 + np.random.random())
                a[:, i] += x * np.exp(-((np.arange(m) / m - y) * z) ** 2)
        return a

    d = layers(3, 100)
    d[50, :] = 0  # test for fixed weighted wiggle (issue #6313)

    fig, axs = plt.subplots(2, 2)

    axs[0, 0].stackplot(range(100), d.T, baseline='zero')
    axs[0, 1].stackplot(range(100), d.T, baseline='sym')
    axs[1, 0].stackplot(range(100), d.T, baseline='wiggle')
    axs[1, 1].stackplot(range(100), d.T, baseline='weighted_wiggle')


def _bxp_test_helper(
        stats_kwargs={}, transform_stats=lambda s: s, bxp_kwargs={}):
    np.random.seed(937)
    logstats = mpl.cbook.boxplot_stats(
        np.random.lognormal(mean=1.25, sigma=1., size=(37, 4)), **stats_kwargs)
    fig, ax = plt.subplots()
    if bxp_kwargs.get('vert', True):
        ax.set_yscale('log')
    else:
        ax.set_xscale('log')
    # Work around baseline images generate back when bxp did not respect the
    # boxplot.boxprops.linewidth rcParam when patch_artist is False.
    if not bxp_kwargs.get('patch_artist', False):
        mpl.rcParams['boxplot.boxprops.linewidth'] = \
            mpl.rcParams['lines.linewidth']
    ax.bxp(transform_stats(logstats), **bxp_kwargs)


@image_comparison(['bxp_baseline.png'],
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_baseline():
    _bxp_test_helper()


@image_comparison(['bxp_rangewhis.png'],
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_rangewhis():
    _bxp_test_helper(stats_kwargs=dict(whis=[0, 100]))


@image_comparison(['bxp_percentilewhis.png'],
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_percentilewhis():
    _bxp_test_helper(stats_kwargs=dict(whis=[5, 95]))


@image_comparison(['bxp_with_xlabels.png'],
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_with_xlabels():
    def transform(stats):
        for s, label in zip(stats, list('ABCD')):
            s['label'] = label
        return stats

    _bxp_test_helper(transform_stats=transform)


@image_comparison(['bxp_horizontal.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default',
                  tol=0.1)
def test_bxp_horizontal():
    _bxp_test_helper(bxp_kwargs=dict(vert=False))


@image_comparison(['bxp_with_ylabels.png'],
                  savefig_kwarg={'dpi': 40},
                  style='default',
                  tol=0.1)
def test_bxp_with_ylabels():
    def transform(stats):
        for s, label in zip(stats, list('ABCD')):
            s['label'] = label
        return stats

    _bxp_test_helper(transform_stats=transform, bxp_kwargs=dict(vert=False))


@image_comparison(['bxp_patchartist.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_patchartist():
    _bxp_test_helper(bxp_kwargs=dict(patch_artist=True))


@image_comparison(['bxp_custompatchartist.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 100},
                  style='default')
def test_bxp_custompatchartist():
    _bxp_test_helper(bxp_kwargs=dict(
        patch_artist=True,
        boxprops=dict(facecolor='yellow', edgecolor='green', ls=':')))


@image_comparison(['bxp_customoutlier.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_customoutlier():
    _bxp_test_helper(bxp_kwargs=dict(
        flierprops=dict(linestyle='none', marker='d', mfc='g')))


@image_comparison(['bxp_withmean_custompoint.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_showcustommean():
    _bxp_test_helper(bxp_kwargs=dict(
        showmeans=True,
        meanprops=dict(linestyle='none', marker='d', mfc='green'),
    ))


@image_comparison(['bxp_custombox.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_custombox():
    _bxp_test_helper(bxp_kwargs=dict(
        boxprops=dict(linestyle='--', color='b', lw=3)))


@image_comparison(['bxp_custommedian.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_custommedian():
    _bxp_test_helper(bxp_kwargs=dict(
        medianprops=dict(linestyle='--', color='b', lw=3)))


@image_comparison(['bxp_customcap.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_customcap():
    _bxp_test_helper(bxp_kwargs=dict(
        capprops=dict(linestyle='--', color='g', lw=3)))


@image_comparison(['bxp_customwhisker.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_customwhisker():
    _bxp_test_helper(bxp_kwargs=dict(
        whiskerprops=dict(linestyle='-', color='m', lw=3)))


@image_comparison(['bxp_withnotch.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_shownotches():
    _bxp_test_helper(bxp_kwargs=dict(shownotches=True))


@image_comparison(['bxp_nocaps.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_nocaps():
    _bxp_test_helper(bxp_kwargs=dict(showcaps=False))


@image_comparison(['bxp_nobox.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_nobox():
    _bxp_test_helper(bxp_kwargs=dict(showbox=False))


@image_comparison(['bxp_no_flier_stats.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_no_flier_stats():
    def transform(stats):
        for s in stats:
            s.pop('fliers', None)
        return stats

    _bxp_test_helper(transform_stats=transform,
                     bxp_kwargs=dict(showfliers=False))


@image_comparison(['bxp_withmean_point.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_showmean():
    _bxp_test_helper(bxp_kwargs=dict(showmeans=True, meanline=False))


@image_comparison(['bxp_withmean_line.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_showmeanasline():
    _bxp_test_helper(bxp_kwargs=dict(showmeans=True, meanline=True))


@image_comparison(['bxp_scalarwidth.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_scalarwidth():
    _bxp_test_helper(bxp_kwargs=dict(widths=.25))


@image_comparison(['bxp_customwidths.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_customwidths():
    _bxp_test_helper(bxp_kwargs=dict(widths=[0.10, 0.25, 0.65, 0.85]))


@image_comparison(['bxp_custompositions.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_bxp_custompositions():
    _bxp_test_helper(bxp_kwargs=dict(positions=[1, 5, 6, 7]))


def test_bxp_bad_widths():
    with pytest.raises(ValueError):
        _bxp_test_helper(bxp_kwargs=dict(widths=[1]))


def test_bxp_bad_positions():
    with pytest.raises(ValueError):
        _bxp_test_helper(bxp_kwargs=dict(positions=[2, 3]))


@image_comparison(['boxplot', 'boxplot'], tol=1.28, style='default')
def test_boxplot():
    # Randomness used for bootstrapping.
    np.random.seed(937)

    x = np.linspace(-7, 7, 140)
    x = np.hstack([-25, x, 25])
    fig, ax = plt.subplots()

    ax.boxplot([x, x], bootstrap=10000, notch=1)
    ax.set_ylim((-30, 30))

    # Reuse testcase from above for a labeled data test
    data = {"x": [x, x]}
    fig, ax = plt.subplots()
    ax.boxplot("x", bootstrap=10000, notch=1, data=data)
    ax.set_ylim((-30, 30))


@image_comparison(['boxplot_sym2.png'], remove_text=True, style='default')
def test_boxplot_sym2():
    # Randomness used for bootstrapping.
    np.random.seed(937)

    x = np.linspace(-7, 7, 140)
    x = np.hstack([-25, x, 25])
    fig, [ax1, ax2] = plt.subplots(1, 2)

    ax1.boxplot([x, x], bootstrap=10000, sym='^')
    ax1.set_ylim((-30, 30))

    ax2.boxplot([x, x], bootstrap=10000, sym='g')
    ax2.set_ylim((-30, 30))


@image_comparison(['boxplot_sym.png'],
                  remove_text=True,
                  savefig_kwarg={'dpi': 40},
                  style='default')
def test_boxplot_sym():
    x = np.linspace(-7, 7, 140)
    x = np.hstack([-25, x, 25])
    fig, ax = plt.subplots()

    ax.boxplot([x, x], sym='gs')
    ax.set_ylim((-30, 30))


@image_comparison(['boxplot_autorange_false_whiskers.png',
                   'boxplot_autorange_true_whiskers.png'],
                  style='default')
def test_boxplot_autorange_whiskers():
    # Randomness used for bootstrapping.
    np.random.seed(937)

    x = np.ones(140)
    x = np.hstack([0, x, 2])

    fig1, ax1 = plt.subplots()
    ax1.boxplot([x, x], bootstrap=10000, notch=1)
    ax1.set_ylim((-5, 5))

    fig2, ax2 = plt.subplots()
    ax2.boxplot([x, x], bootstrap=10000, notch=1, autorange=True)
    ax2.set_ylim((-5, 5))


def _rc_test_bxp_helper(ax, rc_dict):
    x = np.linspace(-7, 7, 140)
    x = np.hstack([-25, x, 25])
    with matplotlib.rc_context(rc_dict):
        ax.boxplot([x, x])
    return ax


@image_comparison(['boxplot_rc_parameters'],
                  savefig_kwarg={'dpi': 100}, remove_text=True,
                  tol=1, style='default')
def test_boxplot_rc_parameters():
    # Randomness used for bootstrapping.
    np.random.seed(937)

    fig, ax = plt.subplots(3)

    rc_axis0 = {
        'boxplot.notch': True,
        'boxplot.whiskers': [5, 95],
        'boxplot.bootstrap': 10000,

        'boxplot.flierprops.color': 'b',
        'boxplot.flierprops.marker': 'o',
        'boxplot.flierprops.markerfacecolor': 'g',
        'boxplot.flierprops.markeredgecolor': 'b',
        'boxplot.flierprops.markersize': 5,
        'boxplot.flierprops.linestyle': '--',
        'boxplot.flierprops.linewidth': 2.0,

        'boxplot.boxprops.color': 'r',
        'boxplot.boxprops.linewidth': 2.0,
        'boxplot.boxprops.linestyle': '--',

        'boxplot.capprops.color': 'c',
        'boxplot.capprops.linewidth': 2.0,
        'boxplot.capprops.linestyle': '--',

        'boxplot.medianprops.color': 'k',
        'boxplot.medianprops.linewidth': 2.0,
        'boxplot.medianprops.linestyle': '--',
    }

    rc_axis1 = {
        'boxplot.vertical': False,
        'boxplot.whiskers': [0, 100],
        'boxplot.patchartist': True,
    }

    rc_axis2 = {
        'boxplot.whiskers': 2.0,
        'boxplot.showcaps': False,
        'boxplot.showbox': False,
        'boxplot.showfliers': False,
        'boxplot.showmeans': True,
        'boxplot.meanline': True,

        'boxplot.meanprops.color': 'c',
        'boxplot.meanprops.linewidth': 2.0,
        'boxplot.meanprops.linestyle': '--',

        'boxplot.whiskerprops.color': 'r',
        'boxplot.whiskerprops.linewidth': 2.0,
        'boxplot.whiskerprops.linestyle': '-.',
    }
    dict_list = [rc_axis0, rc_axis1, rc_axis2]
    for axis, rc_axis in zip(ax, dict_list):
        _rc_test_bxp_helper(axis, rc_axis)

    assert (matplotlib.patches.PathPatch in
            [type(t) for t in ax[1].get_children()])


@image_comparison(['boxplot_with_CIarray.png'],
                  remove_text=True, savefig_kwarg={'dpi': 40}, style='default')
def test_boxplot_with_CIarray():
    # Randomness used for bootstrapping.
    np.random.seed(937)

    x = np.linspace(-7, 7, 140)
    x = np.hstack([-25, x, 25])
    fig, ax = plt.subplots()
    CIs = np.array([[-1.5, 3.], [-1., 3.5]])

    # show a boxplot with Matplotlib medians and confidence intervals, and
    # another with manual values
    ax.boxplot([x, x], bootstrap=10000, usermedians=[None, 1.0],
               conf_intervals=CIs, notch=1)
    ax.set_ylim((-30, 30))


@image_comparison(['boxplot_no_inverted_whisker.png'],
                  remove_text=True, savefig_kwarg={'dpi': 40}, style='default')
def test_boxplot_no_weird_whisker():
    x = np.array([3, 9000, 150, 88, 350, 200000, 1400, 960],
                 dtype=np.float64)
    ax1 = plt.axes()
    ax1.boxplot(x)
    ax1.set_yscale('log')
    ax1.yaxis.grid(False, which='minor')
    ax1.xaxis.grid(False)


def test_boxplot_bad_medians():
    x = np.linspace(-7, 7, 140)
    x = np.hstack([-25, x, 25])
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        ax.boxplot(x, usermedians=[1, 2])
    with pytest.raises(ValueError):
        ax.boxplot([x, x], usermedians=[[1, 2], [1, 2]])


def test_boxplot_bad_ci():
    x = np.linspace(-7, 7, 140)
    x = np.hstack([-25, x, 25])
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        ax.boxplot([x, x], conf_intervals=[[1, 2]])
    with pytest.raises(ValueError):
        ax.boxplot([x, x], conf_intervals=[[1, 2], [1]])


def test_boxplot_zorder():
    x = np.arange(10)
    fix, ax = plt.subplots()
    assert ax.boxplot(x)['boxes'][0].get_zorder() == 2
    assert ax.boxplot(x, zorder=10)['boxes'][0].get_zorder() == 10


def test_boxplot_marker_behavior():
    plt.rcParams['lines.marker'] = 's'
    plt.rcParams['boxplot.flierprops.marker'] = 'o'
    plt.rcParams['boxplot.meanprops.marker'] = '^'
    fig, ax = plt.subplots()
    test_data = np.arange(100)
    test_data[-1] = 150  # a flier point
    bxp_handle = ax.boxplot(test_data, showmeans=True)
    for bxp_lines in ['whiskers', 'caps', 'boxes', 'medians']:
        for each_line in bxp_handle[bxp_lines]:
            # Ensure that the rcParams['lines.marker'] is overridden by ''
            assert each_line.get_marker() == ''

    # Ensure that markers for fliers and means aren't overridden with ''
    assert bxp_handle['fliers'][0].get_marker() == 'o'
    assert bxp_handle['means'][0].get_marker() == '^'


@image_comparison(['boxplot_mod_artists_after_plotting.png'],
                  remove_text=True, savefig_kwarg={'dpi': 40}, style='default')
def test_boxplot_mod_artist_after_plotting():
    x = [0.15, 0.11, 0.06, 0.06, 0.12, 0.56, -0.56]
    fig, ax = plt.subplots()
    bp = ax.boxplot(x, sym="o")
    for key in bp:
        for obj in bp[key]:
            obj.set_color('green')


@image_comparison(['violinplot_vert_baseline.png',
                   'violinplot_vert_baseline.png'])
def test_vert_violinplot_baseline():
    # First 9 digits of frac(sqrt(2))
    np.random.seed(414213562)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax = plt.axes()
    ax.violinplot(data, positions=range(4), showmeans=0, showextrema=0,
                  showmedians=0)

    # Reuse testcase from above for a labeled data test
    data = {"d": data}
    fig, ax = plt.subplots()
    ax.violinplot("d", positions=range(4), showmeans=0, showextrema=0,
                  showmedians=0, data=data)


@image_comparison(['violinplot_vert_showmeans.png'])
def test_vert_violinplot_showmeans():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(3))
    np.random.seed(732050807)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), showmeans=1, showextrema=0,
                  showmedians=0)


@image_comparison(['violinplot_vert_showextrema.png'])
def test_vert_violinplot_showextrema():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(5))
    np.random.seed(236067977)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), showmeans=0, showextrema=1,
                  showmedians=0)


@image_comparison(['violinplot_vert_showmedians.png'])
def test_vert_violinplot_showmedians():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(7))
    np.random.seed(645751311)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), showmeans=0, showextrema=0,
                  showmedians=1)


@image_comparison(['violinplot_vert_showall.png'])
def test_vert_violinplot_showall():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(11))
    np.random.seed(316624790)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), showmeans=1, showextrema=1,
                  showmedians=1,
                  quantiles=[[0.1, 0.9], [0.2, 0.8], [0.3, 0.7], [0.4, 0.6]])


@image_comparison(['violinplot_vert_custompoints_10.png'])
def test_vert_violinplot_custompoints_10():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(13))
    np.random.seed(605551275)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), showmeans=0, showextrema=0,
                  showmedians=0, points=10)


@image_comparison(['violinplot_vert_custompoints_200.png'])
def test_vert_violinplot_custompoints_200():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(17))
    np.random.seed(123105625)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), showmeans=0, showextrema=0,
                  showmedians=0, points=200)


@image_comparison(['violinplot_horiz_baseline.png'])
def test_horiz_violinplot_baseline():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(19))
    np.random.seed(358898943)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), vert=False, showmeans=0,
                  showextrema=0, showmedians=0)


@image_comparison(['violinplot_horiz_showmedians.png'])
def test_horiz_violinplot_showmedians():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(23))
    np.random.seed(795831523)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), vert=False, showmeans=0,
                  showextrema=0, showmedians=1)


@image_comparison(['violinplot_horiz_showmeans.png'])
def test_horiz_violinplot_showmeans():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(29))
    np.random.seed(385164807)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), vert=False, showmeans=1,
                  showextrema=0, showmedians=0)


@image_comparison(['violinplot_horiz_showextrema.png'])
def test_horiz_violinplot_showextrema():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(31))
    np.random.seed(567764362)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), vert=False, showmeans=0,
                  showextrema=1, showmedians=0)


@image_comparison(['violinplot_horiz_showall.png'])
def test_horiz_violinplot_showall():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(37))
    np.random.seed(82762530)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), vert=False, showmeans=1,
                  showextrema=1, showmedians=1,
                  quantiles=[[0.1, 0.9], [0.2, 0.8], [0.3, 0.7], [0.4, 0.6]])


@image_comparison(['violinplot_horiz_custompoints_10.png'])
def test_horiz_violinplot_custompoints_10():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(41))
    np.random.seed(403124237)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), vert=False, showmeans=0,
                  showextrema=0, showmedians=0, points=10)


@image_comparison(['violinplot_horiz_custompoints_200.png'])
def test_horiz_violinplot_custompoints_200():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(43))
    np.random.seed(557438524)
    data = [np.random.normal(size=100) for _ in range(4)]
    ax.violinplot(data, positions=range(4), vert=False, showmeans=0,
                  showextrema=0, showmedians=0, points=200)


def test_violinplot_bad_positions():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(47))
    np.random.seed(855654600)
    data = [np.random.normal(size=100) for _ in range(4)]
    with pytest.raises(ValueError):
        ax.violinplot(data, positions=range(5))


def test_violinplot_bad_widths():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(53))
    np.random.seed(280109889)
    data = [np.random.normal(size=100) for _ in range(4)]
    with pytest.raises(ValueError):
        ax.violinplot(data, positions=range(4), widths=[1, 2, 3])


def test_violinplot_bad_quantiles():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(73))
    np.random.seed(544003745)
    data = [np.random.normal(size=100)]

    # Different size quantile list and plots
    with pytest.raises(ValueError):
        ax.violinplot(data, quantiles=[[0.1, 0.2], [0.5, 0.7]])


def test_violinplot_outofrange_quantiles():
    ax = plt.axes()
    # First 9 digits of frac(sqrt(79))
    np.random.seed(888194417)
    data = [np.random.normal(size=100)]

    # Quantile value above 100
    with pytest.raises(ValueError):
        ax.violinplot(data, quantiles=[[0.1, 0.2, 0.3, 1.05]])

    # Quantile value below 0
    with pytest.raises(ValueError):
        ax.violinplot(data, quantiles=[[-0.05, 0.2, 0.3, 0.75]])


@check_figures_equal(extensions=["png"])
def test_violinplot_single_list_quantiles(fig_test, fig_ref):
    # Ensures quantile list for 1D can be passed in as single list
    # First 9 digits of frac(sqrt(83))
    np.random.seed(110433579)
    data = [np.random.normal(size=100)]

    # Test image
    ax = fig_test.subplots()
    ax.violinplot(data, quantiles=[0.1, 0.3, 0.9])

    # Reference image
    ax = fig_ref.subplots()
    ax.violinplot(data, quantiles=[[0.1, 0.3, 0.9]])


@check_figures_equal(extensions=["png"])
def test_violinplot_pandas_series(fig_test, fig_ref, pd):
    np.random.seed(110433579)
    s1 = pd.Series(np.random.normal(size=7), index=[9, 8, 7, 6, 5, 4, 3])
    s2 = pd.Series(np.random.normal(size=9), index=list('ABCDEFGHI'))
    s3 = pd.Series(np.random.normal(size=11))
    fig_test.subplots().violinplot([s1, s2, s3])
    fig_ref.subplots().violinplot([s1.values, s2.values, s3.values])


def test_manage_xticks():
    _, ax = plt.subplots()
    ax.set_xlim(0, 4)
    old_xlim = ax.get_xlim()
    np.random.seed(0)
    y1 = np.random.normal(10, 3, 20)
    y2 = np.random.normal(3, 1, 20)
    ax.boxplot([y1, y2], positions=[1, 2], manage_ticks=False)
    new_xlim = ax.get_xlim()
    assert_array_equal(old_xlim, new_xlim)


def test_boxplot_not_single():
    fig, ax = plt.subplots()
    ax.boxplot(np.random.rand(100), positions=[3])
    ax.boxplot(np.random.rand(100), positions=[5])
    fig.canvas.draw()
    assert ax.get_xlim() == (2.5, 5.5)
    assert list(ax.get_xticks()) == [3, 5]
    assert [t.get_text() for t in ax.get_xticklabels()] == ["3", "5"]


def test_tick_space_size_0():
    # allow font size to be zero, which affects ticks when there is
    # no other text in the figure.
    plt.plot([0, 1], [0, 1])
    matplotlib.rcParams.update({'font.size': 0})
    b = io.BytesIO()
    plt.savefig(b, dpi=80, format='raw')


@image_comparison(['errorbar_basic', 'errorbar_mixed', 'errorbar_basic'])
def test_errorbar():
    # longdouble due to floating point rounding issues with certain
    # computer chipsets
    x = np.arange(0.1, 4, 0.5, dtype=np.longdouble)
    y = np.exp(-x)

    yerr = 0.1 + 0.2*np.sqrt(x)
    xerr = 0.1 + yerr

    # First illustrate basic pyplot interface, using defaults where possible.
    fig = plt.figure()
    ax = fig.gca()
    ax.errorbar(x, y, xerr=0.2, yerr=0.4)
    ax.set_title("Simplest errorbars, 0.2 in x, 0.4 in y")

    # Now switch to a more OO interface to exercise more features.
    fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)
    ax = axs[0, 0]
    ax.errorbar(x, y, yerr=yerr, fmt='o')
    ax.set_title('Vert. symmetric')

    # With 4 subplots, reduce the number of axis ticks to avoid crowding.
    ax.locator_params(nbins=4)

    ax = axs[0, 1]
    ax.errorbar(x, y, xerr=xerr, fmt='o', alpha=0.4)
    ax.set_title('Hor. symmetric w/ alpha')

    ax = axs[1, 0]
    ax.errorbar(x, y, yerr=[yerr, 2*yerr], xerr=[xerr, 2*xerr], fmt='--o')
    ax.set_title('H, V asymmetric')

    ax = axs[1, 1]
    ax.set_yscale('log')
    # Here we have to be careful to keep all y values positive:
    ylower = np.maximum(1e-2, y - yerr)
    yerr_lower = y - ylower

    ax.errorbar(x, y, yerr=[yerr_lower, 2*yerr], xerr=xerr,
                fmt='o', ecolor='g', capthick=2)
    ax.set_title('Mixed sym., log y')

    fig.suptitle('Variable errorbars')

    # Reuse the first testcase from above for a labeled data test
    data = {"x": x, "y": y}
    fig = plt.figure()
    ax = fig.gca()
    ax.errorbar("x", "y", xerr=0.2, yerr=0.4, data=data)
    ax.set_title("Simplest errorbars, 0.2 in x, 0.4 in y")


def test_errorbar_colorcycle():

    f, ax = plt.subplots()
    x = np.arange(10)
    y = 2*x

    e1, _, _ = ax.errorbar(x, y, c=None)
    e2, _, _ = ax.errorbar(x, 2*y, c=None)
    ln1, = ax.plot(x, 4*y)

    assert mcolors.to_rgba(e1.get_color()) == mcolors.to_rgba('C0')
    assert mcolors.to_rgba(e2.get_color()) == mcolors.to_rgba('C1')
    assert mcolors.to_rgba(ln1.get_color()) == mcolors.to_rgba('C2')


@check_figures_equal()
def test_errorbar_cycle_ecolor(fig_test, fig_ref):
    x = np.arange(0.1, 4, 0.5)
    y = [np.exp(-x+n) for n in range(4)]

    axt = fig_test.subplots()
    axr = fig_ref.subplots()

    for yi, color in zip(y, ['C0', 'C1', 'C2', 'C3']):
        axt.errorbar(x, yi, yerr=(yi * 0.25), linestyle='-',
                     marker='o', ecolor='black')
        axr.errorbar(x, yi, yerr=(yi * 0.25), linestyle='-',
                     marker='o', color=color, ecolor='black')


def test_errorbar_shape():
    fig = plt.figure()
    ax = fig.gca()

    x = np.arange(0.1, 4, 0.5)
    y = np.exp(-x)
    yerr1 = 0.1 + 0.2*np.sqrt(x)
    yerr = np.vstack((yerr1, 2*yerr1)).T
    xerr = 0.1 + yerr

    with pytest.raises(ValueError):
        ax.errorbar(x, y, yerr=yerr, fmt='o')
    with pytest.raises(ValueError):
        ax.errorbar(x, y, xerr=xerr, fmt='o')
    with pytest.raises(ValueError):
        ax.errorbar(x, y, yerr=yerr, xerr=xerr, fmt='o')


@image_comparison(['errorbar_limits'])
def test_errorbar_limits():
    x = np.arange(0.5, 5.5, 0.5)
    y = np.exp(-x)
    xerr = 0.1
    yerr = 0.2
    ls = 'dotted'

    fig, ax = plt.subplots()

    # standard error bars
    ax.errorbar(x, y, xerr=xerr, yerr=yerr, ls=ls, color='blue')

    # including upper limits
    uplims = np.zeros_like(x)
    uplims[[1, 5, 9]] = True
    ax.errorbar(x, y+0.5, xerr=xerr, yerr=yerr, uplims=uplims, ls=ls,
                color='green')

    # including lower limits
    lolims = np.zeros_like(x)
    lolims[[2, 4, 8]] = True
    ax.errorbar(x, y+1.0, xerr=xerr, yerr=yerr, lolims=lolims, ls=ls,
                color='red')

    # including upper and lower limits
    ax.errorbar(x, y+1.5, marker='o', ms=8, xerr=xerr, yerr=yerr,
                lolims=lolims, uplims=uplims, ls=ls, color='magenta')

    # including xlower and xupper limits
    xerr = 0.2
    yerr = np.full_like(x, 0.2)
    yerr[[3, 6]] = 0.3
    xlolims = lolims
    xuplims = uplims
    lolims = np.zeros_like(x)
    uplims = np.zeros_like(x)
    lolims[[6]] = True
    uplims[[3]] = True
    ax.errorbar(x, y+2.1, marker='o', ms=8, xerr=xerr, yerr=yerr,
                xlolims=xlolims, xuplims=xuplims, uplims=uplims,
                lolims=lolims, ls='none', mec='blue', capsize=0,
                color='cyan')
    ax.set_xlim((0, 5.5))
    ax.set_title('Errorbar upper and lower limits')


def test_errobar_nonefmt():
    # Check that passing 'none' as a format still plots errorbars
    x = np.arange(5)
    y = np.arange(5)

    plotline, _, barlines = plt.errorbar(x, y, xerr=1, yerr=1, fmt='none')
    assert plotline is None
    for errbar in barlines:
        assert np.all(errbar.get_color() == mcolors.to_rgba('C0'))


def test_errorbar_line_specific_kwargs():
    # Check that passing line-specific keyword arguments will not result in
    # errors.
    x = np.arange(5)
    y = np.arange(5)

    plotline, _, _ = plt.errorbar(x, y, xerr=1, yerr=1, ls='None',
                                  marker='s', fillstyle='full',
                                  drawstyle='steps-mid',
                                  dash_capstyle='round',
                                  dash_joinstyle='miter',
                                  solid_capstyle='butt',
                                  solid_joinstyle='bevel')
    assert plotline.get_fillstyle() == 'full'
    assert plotline.get_drawstyle() == 'steps-mid'


@check_figures_equal(extensions=['png'])
def test_errorbar_with_prop_cycle(fig_test, fig_ref):
    ax = fig_ref.subplots()
    ax.errorbar(x=[2, 4, 10], y=[0, 1, 2], yerr=0.5,
                ls='--', marker='s', mfc='k')
    ax.errorbar(x=[2, 4, 10], y=[2, 3, 4], yerr=0.5, color='tab:green',
                ls=':', marker='s', mfc='y')
    ax.errorbar(x=[2, 4, 10], y=[4, 5, 6], yerr=0.5, fmt='tab:blue',
                ls='-.', marker='o', mfc='c')
    ax.set_xlim(1, 11)

    _cycle = cycler(ls=['--', ':', '-.'], marker=['s', 's', 'o'],
                    mfc=['k', 'y', 'c'], color=['b', 'g', 'r'])
    plt.rc("axes", prop_cycle=_cycle)
    ax = fig_test.subplots()
    ax.errorbar(x=[2, 4, 10], y=[0, 1, 2], yerr=0.5)
    ax.errorbar(x=[2, 4, 10], y=[2, 3, 4], yerr=0.5, color='tab:green')
    ax.errorbar(x=[2, 4, 10], y=[4, 5, 6], yerr=0.5, fmt='tab:blue')
    ax.set_xlim(1, 11)


def test_errorbar_every_invalid():
    x = np.linspace(0, 1, 15)
    y = x * (1-x)
    yerr = y/6

    ax = plt.figure().subplots()

    with pytest.raises(ValueError, match='not a tuple of two integers'):
        ax.errorbar(x, y, yerr, errorevery=(1, 2, 3))
    with pytest.raises(ValueError, match='not a tuple of two integers'):
        ax.errorbar(x, y, yerr, errorevery=(1.3, 3))
    with pytest.raises(ValueError, match='not a valid NumPy fancy index'):
        ax.errorbar(x, y, yerr, errorevery=[False, True])
    with pytest.raises(ValueError, match='not a recognized value'):
        ax.errorbar(x, y, yerr, errorevery='foobar')


@check_figures_equal()
def test_errorbar_every(fig_test, fig_ref):
    x = np.linspace(0, 1, 15)
    y = x * (1-x)
    yerr = y/6

    ax_ref = fig_ref.subplots()
    ax_test = fig_test.subplots()

    for color, shift in zip('rgbk', [0, 0, 2, 7]):
        y += .02

        # Check errorevery using an explicit offset and step.
        ax_test.errorbar(x, y, yerr, errorevery=(shift, 4),
                         capsize=4, c=color)

        # Using manual errorbars
        # n.b. errorbar draws the main plot at z=2.1 by default
        ax_ref.plot(x, y, c=color, zorder=2.1)
        ax_ref.errorbar(x[shift::4], y[shift::4], yerr[shift::4],
                        capsize=4, c=color, fmt='none')

    # Check that markevery is propagated to line, without affecting errorbars.
    ax_test.errorbar(x, y + 0.1, yerr, markevery=(1, 4), capsize=4, fmt='o')
    ax_ref.plot(x[1::4], y[1::4] + 0.1, 'o', zorder=2.1)
    ax_ref.errorbar(x, y + 0.1, yerr, capsize=4, fmt='none')

    # Check that passing a slice to markevery/errorevery works.
    ax_test.errorbar(x, y + 0.2, yerr, errorevery=slice(2, None, 3),
                     markevery=slice(2, None, 3),
                     capsize=4, c='C0', fmt='o')
    ax_ref.plot(x[2::3], y[2::3] + 0.2, 'o', c='C0', zorder=2.1)
    ax_ref.errorbar(x[2::3], y[2::3] + 0.2, yerr[2::3],
                    capsize=4, c='C0', fmt='none')

    # Check that passing an iterable to markevery/errorevery works.
    ax_test.errorbar(x, y + 0.2, yerr, errorevery=[False, True, False] * 5,
                     markevery=[False, True, False] * 5,
                     capsize=4, c='C1', fmt='o')
    ax_ref.plot(x[1::3], y[1::3] + 0.2, 'o', c='C1', zorder=2.1)
    ax_ref.errorbar(x[1::3], y[1::3] + 0.2, yerr[1::3],
                    capsize=4, c='C1', fmt='none')


@pytest.mark.parametrize('elinewidth', [[1, 2, 3],
                                        np.array([1, 2, 3]),
                                        1])
def test_errorbar_linewidth_type(elinewidth):
    plt.errorbar([1, 2, 3], [1, 2, 3], yerr=[1, 2, 3], elinewidth=elinewidth)


@image_comparison(['hist_stacked_stepfilled', 'hist_stacked_stepfilled'])
def test_hist_stacked_stepfilled():
    # make some data
    d1 = np.linspace(1, 3, 20)
    d2 = np.linspace(0, 10, 50)
    fig, ax = plt.subplots()
    ax.hist((d1, d2), histtype="stepfilled", stacked=True)

    # Reuse testcase from above for a labeled data test
    data = {"x": (d1, d2)}
    fig, ax = plt.subplots()
    ax.hist("x", histtype="stepfilled", stacked=True, data=data)


@image_comparison(['hist_offset'])
def test_hist_offset():
    # make some data
    d1 = np.linspace(0, 10, 50)
    d2 = np.linspace(1, 3, 20)
    fig, ax = plt.subplots()
    ax.hist(d1, bottom=5)
    ax.hist(d2, bottom=15)


@image_comparison(['hist_step.png'], remove_text=True)
def test_hist_step():
    # make some data
    d1 = np.linspace(1, 3, 20)
    fig, ax = plt.subplots()
    ax.hist(d1, histtype="step")
    ax.set_ylim(0, 10)
    ax.set_xlim(-1, 5)


@image_comparison(['hist_step_horiz.png'])
def test_hist_step_horiz():
    # make some data
    d1 = np.linspace(0, 10, 50)
    d2 = np.linspace(1, 3, 20)
    fig, ax = plt.subplots()
    ax.hist((d1, d2), histtype="step", orientation="horizontal")


@image_comparison(['hist_stacked_weights'])
def test_hist_stacked_weighted():
    # make some data
    d1 = np.linspace(0, 10, 50)
    d2 = np.linspace(1, 3, 20)
    w1 = np.linspace(0.01, 3.5, 50)
    w2 = np.linspace(0.05, 2., 20)
    fig, ax = plt.subplots()
    ax.hist((d1, d2), weights=(w1, w2), histtype="stepfilled", stacked=True)


@pytest.mark.parametrize("use_line_collection", [True, False],
                         ids=['w/ line collection', 'w/o line collection'])
@image_comparison(['stem.png'], style='mpl20', remove_text=True)
def test_stem(use_line_collection):
    x = np.linspace(0.1, 2 * np.pi, 100)

    fig, ax = plt.subplots()
    # Label is a single space to force a legend to be drawn, but to avoid any
    # text being drawn
    ax.stem(x, np.cos(x),
            linefmt='C2-.', markerfmt='k+', basefmt='C1-.', label=' ',
            use_line_collection=use_line_collection)
    ax.legend()


def test_stem_args():
    fig, ax = plt.subplots()

    x = list(range(10))
    y = list(range(10))

    # Test the call signatures
    ax.stem(y)
    ax.stem(x, y)
    ax.stem(x, y, linefmt='r--')
    ax.stem(x, y, linefmt='r--', basefmt='b--')


def test_stem_dates():
    fig, ax = plt.subplots(1, 1)
    xs = [dateutil.parser.parse("2013-9-28 11:00:00"),
          dateutil.parser.parse("2013-9-28 12:00:00")]
    ys = [100, 200]
    ax.stem(xs, ys)


@pytest.mark.parametrize("use_line_collection", [True, False],
                         ids=['w/ line collection', 'w/o line collection'])
@image_comparison(['stem_orientation.png'], style='mpl20', remove_text=True)
def test_stem_orientation(use_line_collection):
    x = np.linspace(0.1, 2*np.pi, 50)

    fig, ax = plt.subplots()
    ax.stem(x, np.cos(x),
            linefmt='C2-.', markerfmt='kx', basefmt='C1-.',
            use_line_collection=use_line_collection, orientation='horizontal')


@image_comparison(['hist_stacked_stepfilled_alpha'])
def test_hist_stacked_stepfilled_alpha():
    # make some data
    d1 = np.linspace(1, 3, 20)
    d2 = np.linspace(0, 10, 50)
    fig, ax = plt.subplots()
    ax.hist((d1, d2), histtype="stepfilled", stacked=True, alpha=0.5)


@image_comparison(['hist_stacked_step'])
def test_hist_stacked_step():
    # make some data
    d1 = np.linspace(1, 3, 20)
    d2 = np.linspace(0, 10, 50)
    fig, ax = plt.subplots()
    ax.hist((d1, d2), histtype="step", stacked=True)


@image_comparison(['hist_stacked_normed'])
def test_hist_stacked_density():
    # make some data
    d1 = np.linspace(1, 3, 20)
    d2 = np.linspace(0, 10, 50)
    fig, ax = plt.subplots()
    ax.hist((d1, d2), stacked=True, density=True)


@image_comparison(['hist_step_bottom.png'], remove_text=True)
def test_hist_step_bottom():
    # make some data
    d1 = np.linspace(1, 3, 20)
    fig, ax = plt.subplots()
    ax.hist(d1, bottom=np.arange(10), histtype="stepfilled")


def test_hist_stepfilled_geometry():
    bins = [0, 1, 2, 3]
    data = [0, 0, 1, 1, 1, 2]
    _, _, (polygon, ) = plt.hist(data,
                                 bins=bins,
                                 histtype='stepfilled')
    xy = [[0, 0], [0, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1],
          [3, 0], [2, 0], [2, 0], [1, 0], [1, 0], [0, 0]]
    assert_array_equal(polygon.get_xy(), xy)


def test_hist_step_geometry():
    bins = [0, 1, 2, 3]
    data = [0, 0, 1, 1, 1, 2]
    _, _, (polygon, ) = plt.hist(data,
                                 bins=bins,
                                 histtype='step')
    xy = [[0, 0], [0, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [3, 0]]
    assert_array_equal(polygon.get_xy(), xy)


def test_hist_stepfilled_bottom_geometry():
    bins = [0, 1, 2, 3]
    data = [0, 0, 1, 1, 1, 2]
    _, _, (polygon, ) = plt.hist(data,
                                 bins=bins,
                                 bottom=[1, 2, 1.5],
                                 histtype='stepfilled')
    xy = [[0, 1], [0, 3], [1, 3], [1, 5], [2, 5], [2, 2.5], [3, 2.5],
          [3, 1.5], [2, 1.5], [2, 2], [1, 2], [1, 1], [0, 1]]
    assert_array_equal(polygon.get_xy(), xy)


def test_hist_step_bottom_geometry():
    bins = [0, 1, 2, 3]
    data = [0, 0, 1, 1, 1, 2]
    _, _, (polygon, ) = plt.hist(data,
                                 bins=bins,
                                 bottom=[1, 2, 1.5],
                                 histtype='step')
    xy = [[0, 1], [0, 3], [1, 3], [1, 5], [2, 5], [2, 2.5], [3, 2.5], [3, 1.5]]
    assert_array_equal(polygon.get_xy(), xy)


def test_hist_stacked_stepfilled_geometry():
    bins = [0, 1, 2, 3]
    data_1 = [0, 0, 1, 1, 1, 2]
    data_2 = [0, 1, 2]
    _, _, patches = plt.hist([data_1, data_2],
                             bins=bins,
                             stacked=True,
                             histtype='stepfilled')

    assert len(patches) == 2

    polygon,  = patches[0]
    xy = [[0, 0], [0, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1],
          [3, 0], [2, 0], [2, 0], [1, 0], [1, 0], [0, 0]]
    assert_array_equal(polygon.get_xy(), xy)

    polygon,  = patches[1]
    xy = [[0, 2], [0, 3], [1, 3], [1, 4], [2, 4], [2, 2], [3, 2],
          [3, 1], [2, 1], [2, 3], [1, 3], [1, 2], [0, 2]]
    assert_array_equal(polygon.get_xy(), xy)


def test_hist_stacked_step_geometry():
    bins = [0, 1, 2, 3]
    data_1 = [0, 0, 1, 1, 1, 2]
    data_2 = [0, 1, 2]
    _, _, patches = plt.hist([data_1, data_2],
                             bins=bins,
                             stacked=True,
                             histtype='step')

    assert len(patches) == 2

    polygon,  = patches[0]
    xy = [[0, 0], [0, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [3, 0]]
    assert_array_equal(polygon.get_xy(), xy)

    polygon,  = patches[1]
    xy = [[0, 2], [0, 3], [1, 3], [1, 4], [2, 4], [2, 2], [3, 2], [3, 1]]
    assert_array_equal(polygon.get_xy(), xy)


def test_hist_stacked_stepfilled_bottom_geometry():
    bins = [0, 1, 2, 3]
    data_1 = [0, 0, 1, 1, 1, 2]
    data_2 = [0, 1, 2]
    _, _, patches = plt.hist([data_1, data_2],
                             bins=bins,
                             stacked=True,
                             bottom=[1, 2, 1.5],
                             histtype='stepfilled')

    assert len(patches) == 2

    polygon,  = patches[0]
    xy = [[0, 1], [0, 3], [1, 3], [1, 5], [2, 5], [2, 2.5], [3, 2.5],
          [3, 1.5], [2, 1.5], [2, 2], [1, 2], [1, 1], [0, 1]]
    assert_array_equal(polygon.get_xy(), xy)

    polygon,  = patches[1]
    xy = [[0, 3], [0, 4], [1, 4], [1, 6], [2, 6], [2, 3.5], [3, 3.5],
          [3, 2.5], [2, 2.5], [2, 5], [1, 5], [1, 3], [0, 3]]
    assert_array_equal(polygon.get_xy(), xy)


def test_hist_stacked_step_bottom_geometry():
    bins = [0, 1, 2, 3]
    data_1 = [0, 0, 1, 1, 1, 2]
    data_2 = [0, 1, 2]
    _, _, patches = plt.hist([data_1, data_2],
                             bins=bins,
                             stacked=True,
                             bottom=[1, 2, 1.5],
                             histtype='step')

    assert len(patches) == 2

    polygon,  = patches[0]
    xy = [[0, 1], [0, 3], [1, 3], [1, 5], [2, 5], [2, 2.5], [3, 2.5], [3, 1.5]]
    assert_array_equal(polygon.get_xy(), xy)

    polygon,  = patches[1]
    xy = [[0, 3], [0, 4], [1, 4], [1, 6], [2, 6], [2, 3.5], [3, 3.5], [3, 2.5]]
    assert_array_equal(polygon.get_xy(), xy)


@image_comparison(['hist_stacked_bar'])
def test_hist_stacked_bar():
    # make some data
    d = [[100, 100, 100, 100, 200, 320, 450, 80, 20, 600, 310, 800],
         [20, 23, 50, 11, 100, 420], [120, 120, 120, 140, 140, 150, 180],
         [60, 60, 60, 60, 300, 300, 5, 5, 5, 5, 10, 300],
         [555, 555, 555, 30, 30, 30, 30, 30, 100, 100, 100, 100, 30, 30],
         [30, 30, 30, 30, 400, 400, 400, 400, 400, 400, 400, 400]]
    colors = [(0.5759849696758961, 1.0, 0.0), (0.0, 1.0, 0.350624650815206),
              (0.0, 1.0, 0.6549834156005998), (0.0, 0.6569064625276622, 1.0),
              (0.28302699607823545, 0.0, 1.0), (0.6849123462299822, 0.0, 1.0)]
    labels = ['green', 'orange', ' yellow', 'magenta', 'black']
    fig, ax = plt.subplots()
    ax.hist(d, bins=10, histtype='barstacked', align='mid', color=colors,
            label=labels)
    ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0), ncol=1)


def test_hist_barstacked_bottom_unchanged():
    b = np.array([10, 20])
    plt.hist([[0, 1], [0, 1]], 2, histtype="barstacked", bottom=b)
    assert b.tolist() == [10, 20]


def test_hist_emptydata():
    fig, ax = plt.subplots()
    ax.hist([[], range(10), range(10)], histtype="step")


def test_hist_labels():
    # test singleton labels OK
    fig, ax = plt.subplots()
    _, _, bars = ax.hist([0, 1], label=0)
    assert bars[0].get_label() == '0'
    _, _, bars = ax.hist([0, 1], label=[0])
    assert bars[0].get_label() == '0'
    _, _, bars = ax.hist([0, 1], label=None)
    assert bars[0].get_label() == '_nolegend_'
    _, _, bars = ax.hist([0, 1], label='0')
    assert bars[0].get_label() == '0'
    _, _, bars = ax.hist([0, 1], label='00')
    assert bars[0].get_label() == '00'


@image_comparison(['transparent_markers'], remove_text=True)
def test_transparent_markers():
    np.random.seed(0)
    data = np.random.random(50)

    fig, ax = plt.subplots()
    ax.plot(data, 'D', mfc='none', markersize=100)


@image_comparison(['rgba_markers'], remove_text=True)
def test_rgba_markers():
    fig, axs = plt.subplots(ncols=2)
    rcolors = [(1, 0, 0, 1), (1, 0, 0, 0.5)]
    bcolors = [(0, 0, 1, 1), (0, 0, 1, 0.5)]
    alphas = [None, 0.2]
    kw = dict(ms=100, mew=20)
    for i, alpha in enumerate(alphas):
        for j, rcolor in enumerate(rcolors):
            for k, bcolor in enumerate(bcolors):
                axs[i].plot(j+1, k+1, 'o', mfc=bcolor, mec=rcolor,
                            alpha=alpha, **kw)
                axs[i].plot(j+1, k+3, 'x', mec=rcolor, alpha=alpha, **kw)
    for ax in axs:
        ax.axis([-1, 4, 0, 5])


@image_comparison(['mollweide_grid'], remove_text=True)
def test_mollweide_grid():
    # test that both horizontal and vertical gridlines appear on the Mollweide
    # projection
    fig = plt.figure()
    ax = fig.add_subplot(projection='mollweide')
    ax.grid()


def test_mollweide_forward_inverse_closure():
    # test that the round-trip Mollweide forward->inverse transformation is an
    # approximate identity
    fig = plt.figure()
    ax = fig.add_subplot(projection='mollweide')

    # set up 1-degree grid in longitude, latitude
    lon = np.linspace(-np.pi, np.pi, 360)
    lat = np.linspace(-np.pi / 2.0, np.pi / 2.0, 180)
    lon, lat = np.meshgrid(lon, lat)
    ll = np.vstack((lon.flatten(), lat.flatten())).T

    # perform forward transform
    xy = ax.transProjection.transform(ll)

    # perform inverse transform
    ll2 = ax.transProjection.inverted().transform(xy)

    # compare
    np.testing.assert_array_almost_equal(ll, ll2, 3)


def test_mollweide_inverse_forward_closure():
    # test that the round-trip Mollweide inverse->forward transformation is an
    # approximate identity
    fig = plt.figure()
    ax = fig.add_subplot(projection='mollweide')

    # set up grid in x, y
    x = np.linspace(0, 1, 500)
    x, y = np.meshgrid(x, x)
    xy = np.vstack((x.flatten(), y.flatten())).T

    # perform inverse transform
    ll = ax.transProjection.inverted().transform(xy)

    # perform forward transform
    xy2 = ax.transProjection.transform(ll)

    # compare
    np.testing.assert_array_almost_equal(xy, xy2, 3)


@image_comparison(['test_alpha'], remove_text=True)
def test_alpha():
    np.random.seed(0)
    data = np.random.random(50)

    fig, ax = plt.subplots()

    # alpha=.5 markers, solid line
    ax.plot(data, '-D', color=[1, 0, 0], mfc=[1, 0, 0, .5],
            markersize=20, lw=10)

    # everything solid by kwarg
    ax.plot(data + 2, '-D', color=[1, 0, 0, .5], mfc=[1, 0, 0, .5],
            markersize=20, lw=10,
            alpha=1)

    # everything alpha=.5 by kwarg
    ax.plot(data + 4, '-D', color=[1, 0, 0], mfc=[1, 0, 0],
            markersize=20, lw=10,
            alpha=.5)

    # everything alpha=.5 by colors
    ax.plot(data + 6, '-D', color=[1, 0, 0, .5], mfc=[1, 0, 0, .5],
            markersize=20, lw=10)

    # alpha=.5 line, solid markers
    ax.plot(data + 8, '-D', color=[1, 0, 0, .5], mfc=[1, 0, 0],
            markersize=20, lw=10)


@image_comparison(['eventplot', 'eventplot'], remove_text=True)
def test_eventplot():
    np.random.seed(0)

    data1 = np.random.random([32, 20]).tolist()
    data2 = np.random.random([6, 20]).tolist()
    data = data1 + data2
    num_datasets = len(data)

    colors1 = [[0, 1, .7]] * len(data1)
    colors2 = [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1],
               [1, .75, 0],
               [1, 0, 1],
               [0, 1, 1]]
    colors = colors1 + colors2

    lineoffsets1 = 12 + np.arange(0, len(data1)) * .33
    lineoffsets2 = [-15, -3, 1, 1.5, 6, 10]
    lineoffsets = lineoffsets1.tolist() + lineoffsets2

    linelengths1 = [.33] * len(data1)
    linelengths2 = [5, 2, 1, 1, 3, 1.5]
    linelengths = linelengths1 + linelengths2

    fig = plt.figure()
    axobj = fig.add_subplot()
    colls = axobj.eventplot(data, colors=colors, lineoffsets=lineoffsets,
                            linelengths=linelengths)

    num_collections = len(colls)
    assert num_collections == num_datasets

    # Reuse testcase from above for a labeled data test
    data = {"pos": data, "c": colors, "lo": lineoffsets, "ll": linelengths}
    fig = plt.figure()
    axobj = fig.add_subplot()
    colls = axobj.eventplot("pos", colors="c", lineoffsets="lo",
                            linelengths="ll", data=data)
    num_collections = len(colls)
    assert num_collections == num_datasets


@image_comparison(['test_eventplot_defaults.png'], remove_text=True)
def test_eventplot_defaults():
    """
    test that eventplot produces the correct output given the default params
    (see bug #3728)
    """
    np.random.seed(0)

    data1 = np.random.random([32, 20]).tolist()
    data2 = np.random.random([6, 20]).tolist()
    data = data1 + data2

    fig = plt.figure()
    axobj = fig.add_subplot()
    axobj.eventplot(data)


@pytest.mark.parametrize(('colors'), [
    ('0.5',),  # string color with multiple characters: not OK before #8193 fix
    ('tab:orange', 'tab:pink', 'tab:cyan', 'bLacK'),  # case-insensitive
    ('red', (0, 1, 0), None, (1, 0, 1, 0.5)),  # a tricky case mixing types
])
def test_eventplot_colors(colors):
    """Test the *colors* parameter of eventplot. Inspired by issue #8193."""
    data = [[0], [1], [2], [3]]  # 4 successive events of different nature

    # Build the list of the expected colors
    expected = [c if c is not None else 'C0' for c in colors]
    # Convert the list into an array of RGBA values
    # NB: ['rgbk'] is not a valid argument for to_rgba_array, while 'rgbk' is.
    if len(expected) == 1:
        expected = expected[0]
    expected = np.broadcast_to(mcolors.to_rgba_array(expected), (len(data), 4))

    fig, ax = plt.subplots()
    if len(colors) == 1:  # tuple with a single string (like '0.5' or 'rgbk')
        colors = colors[0]
    collections = ax.eventplot(data, colors=colors)

    for coll, color in zip(collections, expected):
        assert_allclose(coll.get_color(), color)


@image_comparison(['test_eventplot_problem_kwargs.png'], remove_text=True)
def test_eventplot_problem_kwargs(recwarn):
    """
    test that 'singular' versions of LineCollection props raise an
    MatplotlibDeprecationWarning rather than overriding the 'plural' versions
    (e.g., to prevent 'color' from overriding 'colors', see issue #4297)
    """
    np.random.seed(0)

    data1 = np.random.random([20]).tolist()
    data2 = np.random.random([10]).tolist()
    data = [data1, data2]

    fig = plt.figure()
    axobj = fig.add_subplot()

    axobj.eventplot(data,
                    colors=['r', 'b'],
                    color=['c', 'm'],
                    linewidths=[2, 1],
                    linewidth=[1, 2],
                    linestyles=['solid', 'dashed'],
                    linestyle=['dashdot', 'dotted'])

    assert len(recwarn) == 3
    assert all(issubclass(wi.category, MatplotlibDeprecationWarning)
               for wi in recwarn)


def test_empty_eventplot():
    fig, ax = plt.subplots(1, 1)
    ax.eventplot([[]], colors=[(0.0, 0.0, 0.0, 0.0)])
    plt.draw()


@pytest.mark.parametrize('data', [[[]], [[], [0, 1]], [[0, 1], []]])
@pytest.mark.parametrize('orientation', [None, 'vertical', 'horizontal'])
def test_eventplot_orientation(data, orientation):
    """Introduced when fixing issue #6412."""
    opts = {} if orientation is None else {'orientation': orientation}
    fig, ax = plt.subplots(1, 1)
    ax.eventplot(data, **opts)
    plt.draw()


@check_figures_equal(extensions=['png'])
def test_eventplot_units_list(fig_test, fig_ref):
    # test that list of lists converted properly:
    ts_1 = [datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 2),
            datetime.datetime(2021, 1, 3)]
    ts_2 = [datetime.datetime(2021, 1, 15), datetime.datetime(2021, 1, 16)]

    ax = fig_ref.subplots()
    ax.eventplot(ts_1, lineoffsets=0)
    ax.eventplot(ts_2, lineoffsets=1)

    ax = fig_test.subplots()
    ax.eventplot([ts_1, ts_2])


@image_comparison(['marker_styles.png'], remove_text=True)
def test_marker_styles():
    fig, ax = plt.subplots()
    for y, marker in enumerate(sorted(matplotlib.markers.MarkerStyle.markers,
                                      key=lambda x: str(type(x))+str(x))):
        ax.plot((y % 2)*5 + np.arange(10)*10, np.ones(10)*10*y, linestyle='',
                marker=marker, markersize=10+y/5, label=marker)


@image_comparison(['rc_markerfill.png'])
def test_markers_fillstyle_rcparams():
    fig, ax = plt.subplots()
    x = np.arange(7)
    for idx, (style, marker) in enumerate(
            [('top', 's'), ('bottom', 'o'), ('none', '^')]):
        matplotlib.rcParams['markers.fillstyle'] = style
        ax.plot(x+idx, marker=marker)


@image_comparison(['vertex_markers.png'], remove_text=True)
def test_vertex_markers():
    data = list(range(10))
    marker_as_tuple = ((-1, -1), (1, -1), (1, 1), (-1, 1))
    marker_as_list = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    fig, ax = plt.subplots()
    ax.plot(data, linestyle='', marker=marker_as_tuple, mfc='k')
    ax.plot(data[::-1], linestyle='', marker=marker_as_list, mfc='b')
    ax.set_xlim([-1, 10])
    ax.set_ylim([-1, 10])


@image_comparison(['vline_hline_zorder', 'errorbar_zorder'],
                  tol=0 if platform.machine() == 'x86_64' else 0.02)
def test_eb_line_zorder():
    x = list(range(10))

    # First illustrate basic pyplot interface, using defaults where possible.
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(x, lw=10, zorder=5)
    ax.axhline(1, color='red', lw=10, zorder=1)
    ax.axhline(5, color='green', lw=10, zorder=10)
    ax.axvline(7, color='m', lw=10, zorder=7)
    ax.axvline(2, color='k', lw=10, zorder=3)

    ax.set_title("axvline and axhline zorder test")

    # Now switch to a more OO interface to exercise more features.
    fig = plt.figure()
    ax = fig.gca()
    x = list(range(10))
    y = np.zeros(10)
    yerr = list(range(10))
    ax.errorbar(x, y, yerr=yerr, zorder=5, lw=5, color='r')
    for j in range(10):
        ax.axhline(j, lw=5, color='k', zorder=j)
        ax.axhline(-j, lw=5, color='k', zorder=j)

    ax.set_title("errorbar zorder test")


@check_figures_equal()
def test_axline_loglog(fig_test, fig_ref):
    ax = fig_test.subplots()
    ax.set(xlim=(0.1, 10), ylim=(1e-3, 1))
    ax.loglog([.3, .6], [.3, .6], ".-")
    ax.axline((1, 1e-3), (10, 1e-2), c="k")

    ax = fig_ref.subplots()
    ax.set(xlim=(0.1, 10), ylim=(1e-3, 1))
    ax.loglog([.3, .6], [.3, .6], ".-")
    ax.loglog([1, 10], [1e-3, 1e-2], c="k")


@check_figures_equal()
def test_axline(fig_test, fig_ref):
    ax = fig_test.subplots()
    ax.set(xlim=(-1, 1), ylim=(-1, 1))
    ax.axline((0, 0), (1, 1))
    ax.axline((0, 0), (1, 0), color='C1')
    ax.axline((0, 0.5), (1, 0.5), color='C2')
    # slopes
    ax.axline((-0.7, -0.5), slope=0, color='C3')
    ax.axline((1, -0.5), slope=-0.5, color='C4')
    ax.axline((-0.5, 1), slope=float('inf'), color='C5')

    ax = fig_ref.subplots()
    ax.set(xlim=(-1, 1), ylim=(-1, 1))
    ax.plot([-1, 1], [-1, 1])
    ax.axhline(0, color='C1')
    ax.axhline(0.5, color='C2')
    # slopes
    ax.axhline(-0.5, color='C3')
    ax.plot([-1, 1], [0.5, -0.5], color='C4')
    ax.axvline(-0.5, color='C5')


@check_figures_equal()
def test_axline_transaxes(fig_test, fig_ref):
    ax = fig_test.subplots()
    ax.set(xlim=(-1, 1), ylim=(-1, 1))
    ax.axline((0, 0), slope=1, transform=ax.transAxes)
    ax.axline((1, 0.5), slope=1, color='C1', transform=ax.transAxes)
    ax.axline((0.5, 0.5), slope=0, color='C2', transform=ax.transAxes)
    ax.axline((0.5, 0), (0.5, 1), color='C3', transform=ax.transAxes)

    ax = fig_ref.subplots()
    ax.set(xlim=(-1, 1), ylim=(-1, 1))
    ax.plot([-1, 1], [-1, 1])
    ax.plot([0, 1], [-1, 0], color='C1')
    ax.plot([-1, 1], [0, 0], color='C2')
    ax.plot([0, 0], [-1, 1], color='C3')


@check_figures_equal()
def test_axline_transaxes_panzoom(fig_test, fig_ref):
    # test that it is robust against pan/zoom and
    # figure resize after plotting
    ax = fig_test.subplots()
    ax.set(xlim=(-1, 1), ylim=(-1, 1))
    ax.axline((0, 0), slope=1, transform=ax.transAxes)
    ax.axline((0.5, 0.5), slope=2, color='C1', transform=ax.transAxes)
    ax.axline((0.5, 0.5), slope=0, color='C2', transform=ax.transAxes)
    ax.set(xlim=(0, 5), ylim=(0, 10))
    fig_test.set_size_inches(3, 3)

    ax = fig_ref.subplots()
    ax.set(xlim=(0, 5), ylim=(0, 10))
    fig_ref.set_size_inches(3, 3)
    ax.plot([0, 5], [0, 5])
    ax.plot([0, 5], [0, 10], color='C1')
    ax.plot([0, 5], [5, 5], color='C2')


def test_axline_args():
    """Exactly one of *xy2* and *slope* must be specified."""
    fig, ax = plt.subplots()
    with pytest.raises(TypeError):
        ax.axline((0, 0))  # missing second parameter
    with pytest.raises(TypeError):
        ax.axline((0, 0), (1, 1), slope=1)  # redundant parameters
    ax.set_xscale('log')
    with pytest.raises(TypeError):
        ax.axline((0, 0), slope=1)
    ax.set_xscale('linear')
    ax.set_yscale('log')
    with pytest.raises(TypeError):
        ax.axline((0, 0), slope=1)
    ax.set_yscale('linear')
    with pytest.raises(ValueError):
        ax.axline((0, 0), (0, 0))  # two identical points are not allowed
        plt.draw()


@image_comparison(['vlines_basic', 'vlines_with_nan', 'vlines_masked'],
                  extensions=['png'])
def test_vlines():
    # normal
    x1 = [2, 3, 4, 5, 7]
    y1 = [2, -6, 3, 8, 2]
    fig1, ax1 = plt.subplots()
    ax1.vlines(x1, 0, y1, colors='g', linewidth=5)

    # GH #7406
    x2 = [2, 3, 4, 5, 6, 7]
    y2 = [2, -6, 3, 8, np.nan, 2]
    fig2, (ax2, ax3, ax4) = plt.subplots(nrows=3, figsize=(4, 8))
    ax2.vlines(x2, 0, y2, colors='g', linewidth=5)

    x3 = [2, 3, 4, 5, 6, 7]
    y3 = [np.nan, 2, -6, 3, 8, 2]
    ax3.vlines(x3, 0, y3, colors='r', linewidth=3, linestyle='--')

    x4 = [2, 3, 4, 5, 6, 7]
    y4 = [np.nan, 2, -6, 3, 8, np.nan]
    ax4.vlines(x4, 0, y4, colors='k', linewidth=2)

    # tweak the x-axis so we can see the lines better
    for ax in [ax1, ax2, ax3, ax4]:
        ax.set_xlim(0, 10)

    # check that the y-lims are all automatically the same
    assert ax1.get_ylim() == ax2.get_ylim()
    assert ax1.get_ylim() == ax3.get_ylim()
    assert ax1.get_ylim() == ax4.get_ylim()

    fig3, ax5 = plt.subplots()
    x5 = np.ma.masked_equal([2, 4, 6, 8, 10, 12], 8)
    ymin5 = np.ma.masked_equal([0, 1, -1, 0, 2, 1], 2)
    ymax5 = np.ma.masked_equal([13, 14, 15, 16, 17, 18], 18)
    ax5.vlines(x5, ymin5, ymax5, colors='k', linewidth=2)
    ax5.set_xlim(0, 15)


def test_vlines_default():
    fig, ax = plt.subplots()
    with mpl.rc_context({'lines.color': 'red'}):
        lines = ax.vlines(0.5, 0, 1)
        assert mpl.colors.same_color(lines.get_color(), 'red')


@image_comparison(['hlines_basic', 'hlines_with_nan', 'hlines_masked'],
                  extensions=['png'])
def test_hlines():
    # normal
    y1 = [2, 3, 4, 5, 7]
    x1 = [2, -6, 3, 8, 2]
    fig1, ax1 = plt.subplots()
    ax1.hlines(y1, 0, x1, colors='g', linewidth=5)

    # GH #7406
    y2 = [2, 3, 4, 5, 6, 7]
    x2 = [2, -6, 3, 8, np.nan, 2]
    fig2, (ax2, ax3, ax4) = plt.subplots(nrows=3, figsize=(4, 8))
    ax2.hlines(y2, 0, x2, colors='g', linewidth=5)

    y3 = [2, 3, 4, 5, 6, 7]
    x3 = [np.nan, 2, -6, 3, 8, 2]
    ax3.hlines(y3, 0, x3, colors='r', linewidth=3, linestyle='--')

    y4 = [2, 3, 4, 5, 6, 7]
    x4 = [np.nan, 2, -6, 3, 8, np.nan]
    ax4.hlines(y4, 0, x4, colors='k', linewidth=2)

    # tweak the y-axis so we can see the lines better
    for ax in [ax1, ax2, ax3, ax4]:
        ax.set_ylim(0, 10)

    # check that the x-lims are all automatically the same
    assert ax1.get_xlim() == ax2.get_xlim()
    assert ax1.get_xlim() == ax3.get_xlim()
    assert ax1.get_xlim() == ax4.get_xlim()

    fig3, ax5 = plt.subplots()
    y5 = np.ma.masked_equal([2, 4, 6, 8, 10, 12], 8)
    xmin5 = np.ma.masked_equal([0, 1, -1, 0, 2, 1], 2)
    xmax5 = np.ma.masked_equal([13, 14, 15, 16, 17, 18], 18)
    ax5.hlines(y5, xmin5, xmax5, colors='k', linewidth=2)
    ax5.set_ylim(0, 15)


def test_hlines_default():
    fig, ax = plt.subplots()
    with mpl.rc_context({'lines.color': 'red'}):
        lines = ax.hlines(0.5, 0, 1)
        assert mpl.colors.same_color(lines.get_color(), 'red')


@pytest.mark.parametrize('data', [[1, 2, 3, np.nan, 5],
                                  np.ma.masked_equal([1, 2, 3, 4, 5], 4)])
@check_figures_equal(extensions=["png"])
def test_lines_with_colors(fig_test, fig_ref, data):
    test_colors = ['red', 'green', 'blue', 'purple', 'orange']
    fig_test.add_subplot(2, 1, 1).vlines(data, 0, 1,
                                         colors=test_colors, linewidth=5)
    fig_test.add_subplot(2, 1, 2).hlines(data, 0, 1,
                                         colors=test_colors, linewidth=5)

    expect_xy = [1, 2, 3, 5]
    expect_color = ['red', 'green', 'blue', 'orange']
    fig_ref.add_subplot(2, 1, 1).vlines(expect_xy, 0, 1,
                                        colors=expect_color, linewidth=5)
    fig_ref.add_subplot(2, 1, 2).hlines(expect_xy, 0, 1,
                                        colors=expect_color, linewidth=5)


@image_comparison(['step_linestyle', 'step_linestyle'], remove_text=True)
def test_step_linestyle():
    x = y = np.arange(10)

    # First illustrate basic pyplot interface, using defaults where possible.
    fig, ax_lst = plt.subplots(2, 2)
    ax_lst = ax_lst.flatten()

    ln_styles = ['-', '--', '-.', ':']

    for ax, ls in zip(ax_lst, ln_styles):
        ax.step(x, y, lw=5, linestyle=ls, where='pre')
        ax.step(x, y + 1, lw=5, linestyle=ls, where='mid')
        ax.step(x, y + 2, lw=5, linestyle=ls, where='post')
        ax.set_xlim([-1, 5])
        ax.set_ylim([-1, 7])

    # Reuse testcase from above for a labeled data test
    data = {"X": x, "Y0": y, "Y1": y+1, "Y2": y+2}
    fig, ax_lst = plt.subplots(2, 2)
    ax_lst = ax_lst.flatten()
    ln_styles = ['-', '--', '-.', ':']
    for ax, ls in zip(ax_lst, ln_styles):
        ax.step("X", "Y0", lw=5, linestyle=ls, where='pre', data=data)
        ax.step("X", "Y1", lw=5, linestyle=ls, where='mid', data=data)
        ax.step("X", "Y2", lw=5, linestyle=ls, where='post', data=data)
        ax.set_xlim([-1, 5])
        ax.set_ylim([-1, 7])


@image_comparison(['mixed_collection'], remove_text=True)
def test_mixed_collection():
    # First illustrate basic pyplot interface, using defaults where possible.
    fig, ax = plt.subplots()

    c = mpatches.Circle((8, 8), radius=4, facecolor='none', edgecolor='green')

    # PDF can optimize this one
    p1 = mpl.collections.PatchCollection([c], match_original=True)
    p1.set_offsets([[0, 0], [24, 24]])
    p1.set_linewidths([1, 5])

    # PDF can't optimize this one, because the alpha of the edge changes
    p2 = mpl.collections.PatchCollection([c], match_original=True)
    p2.set_offsets([[48, 0], [-32, -16]])
    p2.set_linewidths([1, 5])
    p2.set_edgecolors([[0, 0, 0.1, 1.0], [0, 0, 0.1, 0.5]])

    ax.patch.set_color('0.5')
    ax.add_collection(p1)
    ax.add_collection(p2)

    ax.set_xlim(0, 16)
    ax.set_ylim(0, 16)


def test_subplot_key_hash():
    ax = plt.subplot(np.int32(5), np.int64(1), 1)
    ax.twinx()
    assert ax.get_subplotspec().get_geometry() == (5, 1, 0, 0)


@image_comparison(
    ["specgram_freqs.png", "specgram_freqs_linear.png",
     "specgram_noise.png", "specgram_noise_linear.png"],
    remove_text=True, tol=0.07, style="default")
def test_specgram():
    """Test axes.specgram in default (psd) mode."""

    # use former defaults to match existing baseline image
    matplotlib.rcParams['image.interpolation'] = 'nearest'

    n = 1000
    Fs = 10.

    fstims = [[Fs/4, Fs/5, Fs/11], [Fs/4.7, Fs/5.6, Fs/11.9]]
    NFFT_freqs = int(10 * Fs / np.min(fstims))
    x = np.arange(0, n, 1/Fs)
    y_freqs = np.concatenate(
        np.sin(2 * np.pi * np.multiply.outer(fstims, x)).sum(axis=1))

    NFFT_noise = int(10 * Fs / 11)
    np.random.seed(0)
    y_noise = np.concatenate([np.random.standard_normal(n), np.random.rand(n)])

    all_sides = ["default", "onesided", "twosided"]
    for y, NFFT in [(y_freqs, NFFT_freqs), (y_noise, NFFT_noise)]:
        noverlap = NFFT // 2
        pad_to = int(2 ** np.ceil(np.log2(NFFT)))
        for ax, sides in zip(plt.figure().subplots(3), all_sides):
            ax.specgram(y, NFFT=NFFT, Fs=Fs, noverlap=noverlap,
                        pad_to=pad_to, sides=sides)
        for ax, sides in zip(plt.figure().subplots(3), all_sides):
            ax.specgram(y, NFFT=NFFT, Fs=Fs, noverlap=noverlap,
                        pad_to=pad_to, sides=sides,
                        scale="linear", norm=matplotlib.colors.LogNorm())


@image_comparison(
    ["specgram_magnitude_freqs.png", "specgram_magnitude_freqs_linear.png",
     "specgram_magnitude_noise.png", "specgram_magnitude_noise_linear.png"],
    remove_text=True, tol=0.07, style="default")
def test_specgram_magnitude():
    """Test axes.specgram in magnitude mode."""

    # use former defaults to match existing baseline image
    matplotlib.rcParams['image.interpolation'] = 'nearest'

    n = 1000
    Fs = 10.

    fstims = [[Fs/4, Fs/5, Fs/11], [Fs/4.7, Fs/5.6, Fs/11.9]]
    NFFT_freqs = int(100 * Fs / np.min(fstims))
    x = np.arange(0, n, 1/Fs)
    y = np.sin(2 * np.pi * np.multiply.outer(fstims, x)).sum(axis=1)
    y[:, -1] = 1
    y_freqs = np.hstack(y)

    NFFT_noise = int(10 * Fs / 11)
    np.random.seed(0)
    y_noise = np.concatenate([np.random.standard_normal(n), np.random.rand(n)])

    all_sides = ["default", "onesided", "twosided"]
    for y, NFFT in [(y_freqs, NFFT_freqs), (y_noise, NFFT_noise)]:
        noverlap = NFFT // 2
        pad_to = int(2 ** np.ceil(np.log2(NFFT)))
        for ax, sides in zip(plt.figure().subplots(3), all_sides):
            ax.specgram(y, NFFT=NFFT, Fs=Fs, noverlap=noverlap,
                        pad_to=pad_to, sides=sides, mode="magnitude")
        for ax, sides in zip(plt.figure().subplots(3), all_sides):
            ax.specgram(y, NFFT=NFFT, Fs=Fs, noverlap=noverlap,
                        pad_to=pad_to, sides=sides, mode="magnitude",
                        scale="linear", norm=matplotlib.colors.LogNorm())


@image_comparison(
    ["specgram_angle_freqs.png", "specgram_phase_freqs.png",
     "specgram_angle_noise.png", "specgram_phase_noise.png"],
    remove_text=True, tol=0.07, style="default")
def test_specgram_angle():
    """Test axes.specgram in angle and phase modes."""

    # use former defaults to match existing baseline image
    matplotlib.rcParams['image.interpolation'] = 'nearest'

    n = 1000
    Fs = 10.

    fstims = [[Fs/4, Fs/5, Fs/11], [Fs/4.7, Fs/5.6, Fs/11.9]]
    NFFT_freqs = int(10 * Fs / np.min(fstims))
    x = np.arange(0, n, 1/Fs)
    y = np.sin(2 * np.pi * np.multiply.outer(fstims, x)).sum(axis=1)
    y[:, -1] = 1
    y_freqs = np.hstack(y)

    NFFT_noise = int(10 * Fs / 11)
    np.random.seed(0)
    y_noise = np.concatenate([np.random.standard_normal(n), np.random.rand(n)])

    all_sides = ["default", "onesided", "twosided"]
    for y, NFFT in [(y_freqs, NFFT_freqs), (y_noise, NFFT_noise)]:
        noverlap = NFFT // 2
        pad_to = int(2 ** np.ceil(np.log2(NFFT)))
        for mode in ["angle", "phase"]:
            for ax, sides in zip(plt.figure().subplots(3), all_sides):
                ax.specgram(y, NFFT=NFFT, Fs=Fs, noverlap=noverlap,
                            pad_to=pad_to, sides=sides, mode=mode)
                with pytest.raises(ValueError):
                    ax.specgram(y, NFFT=NFFT, Fs=Fs, noverlap=noverlap,
                                pad_to=pad_to, sides=sides, mode=mode,
                                scale="dB")


def test_specgram_fs_none():
    """Test axes.specgram when Fs is None, should not throw error."""
    spec, freqs, t, im = plt.specgram(np.ones(300), Fs=None, scale='linear')
    xmin, xmax, freq0, freq1 = im.get_extent()
    assert xmin == 32 and xmax == 96


@check_figures_equal(extensions=["png"])
def test_specgram_origin_rcparam(fig_test, fig_ref):
    """Test specgram ignores image.origin rcParam and uses origin 'upper'."""
    t = np.arange(500)
    signal = np.sin(t)

    plt.rcParams["image.origin"] = 'upper'

    # Reference: First graph using default origin in imshow (upper),
    fig_ref.subplots().specgram(signal)

    # Try to overwrite the setting trying to flip the specgram
    plt.rcParams["image.origin"] = 'lower'

    # Test: origin='lower' should be ignored
    fig_test.subplots().specgram(signal)


def test_specgram_origin_kwarg():
    """Ensure passing origin as a kwarg raises a TypeError."""
    t = np.arange(500)
    signal = np.sin(t)

    with pytest.raises(TypeError):
        plt.specgram(signal, origin='lower')


@image_comparison(
    ["psd_freqs.png", "csd_freqs.png", "psd_noise.png", "csd_noise.png"],
    remove_text=True, tol=0.002)
def test_psd_csd():
    n = 10000
    Fs = 100.

    fstims = [[Fs/4, Fs/5, Fs/11], [Fs/4.7, Fs/5.6, Fs/11.9]]
    NFFT_freqs = int(1000 * Fs / np.min(fstims))
    x = np.arange(0, n, 1/Fs)
    ys_freqs = np.sin(2 * np.pi * np.multiply.outer(fstims, x)).sum(axis=1)

    NFFT_noise = int(1000 * Fs / 11)
    np.random.seed(0)
    ys_noise = [np.random.standard_normal(n), np.random.rand(n)]

    all_kwargs = [{"sides": "default"},
                  {"sides": "onesided", "return_line": False},
                  {"sides": "twosided", "return_line": True}]
    for ys, NFFT in [(ys_freqs, NFFT_freqs), (ys_noise, NFFT_noise)]:
        noverlap = NFFT // 2
        pad_to = int(2 ** np.ceil(np.log2(NFFT)))
        for ax, kwargs in zip(plt.figure().subplots(3), all_kwargs):
            ret = ax.psd(np.concatenate(ys), NFFT=NFFT, Fs=Fs,
                         noverlap=noverlap, pad_to=pad_to, **kwargs)
            assert len(ret) == 2 + kwargs.get("return_line", False)
            ax.set(xlabel="", ylabel="")
        for ax, kwargs in zip(plt.figure().subplots(3), all_kwargs):
            ret = ax.csd(*ys, NFFT=NFFT, Fs=Fs,
                         noverlap=noverlap, pad_to=pad_to, **kwargs)
            assert len(ret) == 2 + kwargs.get("return_line", False)
            ax.set(xlabel="", ylabel="")


@image_comparison(
    ["magnitude_spectrum_freqs_linear.png",
     "magnitude_spectrum_freqs_dB.png",
     "angle_spectrum_freqs.png",
     "phase_spectrum_freqs.png",
     "magnitude_spectrum_noise_linear.png",
     "magnitude_spectrum_noise_dB.png",
     "angle_spectrum_noise.png",
     "phase_spectrum_noise.png"],
    remove_text=True)
def test_spectrum():
    n = 10000
    Fs = 100.

    fstims1 = [Fs/4, Fs/5, Fs/11]
    NFFT = int(1000 * Fs / min(fstims1))
    pad_to = int(2 ** np.ceil(np.log2(NFFT)))

    x = np.arange(0, n, 1/Fs)
    y_freqs = ((np.sin(2 * np.pi * np.outer(x, fstims1)) * 10**np.arange(3))
               .sum(axis=1))
    np.random.seed(0)
    y_noise = np.hstack([np.random.standard_normal(n), np.random.rand(n)]) - .5

    all_sides = ["default", "onesided", "twosided"]
    kwargs = {"Fs": Fs, "pad_to": pad_to}
    for y in [y_freqs, y_noise]:
        for ax, sides in zip(plt.figure().subplots(3), all_sides):
            spec, freqs, line = ax.magnitude_spectrum(y, sides=sides, **kwargs)
            ax.set(xlabel="", ylabel="")
        for ax, sides in zip(plt.figure().subplots(3), all_sides):
            spec, freqs, line = ax.magnitude_spectrum(y, sides=sides, **kwargs,
                                                      scale="dB")
            ax.set(xlabel="", ylabel="")
        for ax, sides in zip(plt.figure().subplots(3), all_sides):
            spec, freqs, line = ax.angle_spectrum(y, sides=sides, **kwargs)
            ax.set(xlabel="", ylabel="")
        for ax, sides in zip(plt.figure().subplots(3), all_sides):
            spec, freqs, line = ax.phase_spectrum(y, sides=sides, **kwargs)
            ax.set(xlabel="", ylabel="")


def test_psd_csd_edge_cases():
    # Inverted yaxis or fully zero inputs used to throw exceptions.
    axs = plt.figure().subplots(2)
    for ax in axs:
        ax.yaxis.set(inverted=True)
    with np.errstate(divide="ignore"):
        axs[0].psd(np.zeros(5))
        axs[1].csd(np.zeros(5), np.zeros(5))


@check_figures_equal(extensions=['png'])
def test_twin_remove(fig_test, fig_ref):
    ax_test = fig_test.add_subplot()
    ax_twinx = ax_test.twinx()
    ax_twiny = ax_test.twiny()
    ax_twinx.remove()
    ax_twiny.remove()

    ax_ref = fig_ref.add_subplot()
    # Ideally we also undo tick changes when calling ``remove()``, but for now
    # manually set the ticks of the reference image to match the test image
    ax_ref.xaxis.tick_bottom()
    ax_ref.yaxis.tick_left()


@image_comparison(['twin_spines.png'], remove_text=True)
def test_twin_spines():

    def make_patch_spines_invisible(ax):
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        ax.spines[:].set_visible(False)

    fig = plt.figure(figsize=(4, 3))
    fig.subplots_adjust(right=0.75)

    host = fig.add_subplot()
    par1 = host.twinx()
    par2 = host.twinx()

    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    par2.spines.right.set_position(("axes", 1.2))
    # Having been created by twinx, par2 has its frame off, so the line of
    # its detached spine is invisible.  First, activate the frame but make
    # the patch and spines invisible.
    make_patch_spines_invisible(par2)
    # Second, show the right spine.
    par2.spines.right.set_visible(True)

    p1, = host.plot([0, 1, 2], [0, 1, 2], "b-")
    p2, = par1.plot([0, 1, 2], [0, 3, 2], "r-")
    p3, = par2.plot([0, 1, 2], [50, 30, 15], "g-")

    host.set_xlim(0, 2)
    host.set_ylim(0, 2)
    par1.set_ylim(0, 4)
    par2.set_ylim(1, 65)

    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())

    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)


@image_comparison(['twin_spines_on_top.png', 'twin_spines_on_top.png'],
                  remove_text=True)
def test_twin_spines_on_top():
    matplotlib.rcParams['axes.linewidth'] = 48.0
    matplotlib.rcParams['lines.linewidth'] = 48.0

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    data = np.array([[1000, 1100, 1200, 1250],
                     [310, 301, 360, 400]])

    ax2 = ax1.twinx()

    ax1.plot(data[0], data[1]/1E3, color='#BEAED4')
    ax1.fill_between(data[0], data[1]/1E3, color='#BEAED4', alpha=.8)

    ax2.plot(data[0], data[1]/1E3, color='#7FC97F')
    ax2.fill_between(data[0], data[1]/1E3, color='#7FC97F', alpha=.5)

    # Reuse testcase from above for a labeled data test
    data = {"i": data[0], "j": data[1]/1E3}
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax2 = ax1.twinx()
    ax1.plot("i", "j", color='#BEAED4', data=data)
    ax1.fill_between("i", "j", color='#BEAED4', alpha=.8, data=data)
    ax2.plot("i", "j", color='#7FC97F', data=data)
    ax2.fill_between("i", "j", color='#7FC97F', alpha=.5, data=data)


@pytest.mark.parametrize("grid_which, major_visible, minor_visible", [
    ("both", True, True),
    ("major", True, False),
    ("minor", False, True),
])
def test_rcparam_grid_minor(grid_which, major_visible, minor_visible):
    mpl.rcParams.update({"axes.grid": True, "axes.grid.which": grid_which})
    fig, ax = plt.subplots()
    fig.canvas.draw()
    assert all(tick.gridline.get_visible() == major_visible
               for tick in ax.xaxis.majorTicks)
    assert all(tick.gridline.get_visible() == minor_visible
               for tick in ax.xaxis.minorTicks)


def test_grid():
    fig, ax = plt.subplots()
    ax.grid()
    fig.canvas.draw()
    assert ax.xaxis.majorTicks[0].gridline.get_visible()
    ax.grid(visible=False)
    fig.canvas.draw()
    assert not ax.xaxis.majorTicks[0].gridline.get_visible()
    ax.grid(visible=True)
    fig.canvas.draw()
    assert ax.xaxis.majorTicks[0].gridline.get_visible()
    ax.grid()
    fig.canvas.draw()
    assert not ax.xaxis.majorTicks[0].gridline.get_visible()


def test_reset_grid():
    fig, ax = plt.subplots()
    ax.tick_params(reset=True, which='major', labelsize=10)
    assert not ax.xaxis.majorTicks[0].gridline.get_visible()
    ax.grid(color='red')  # enables grid
    assert ax.xaxis.majorTicks[0].gridline.get_visible()

    with plt.rc_context({'axes.grid': True}):
        ax.clear()
        ax.tick_params(reset=True, which='major', labelsize=10)
        assert ax.xaxis.majorTicks[0].gridline.get_visible()


@check_figures_equal(extensions=['png'])
def test_reset_ticks(fig_test, fig_ref):
    for fig in [fig_ref, fig_test]:
        ax = fig.add_subplot()
        ax.grid(True)
        ax.tick_params(
            direction='in', length=10, width=5, color='C0', pad=12,
            labelsize=14, labelcolor='C1', labelrotation=45,
            grid_color='C2', grid_alpha=0.8, grid_linewidth=3,
            grid_linestyle='--')
        fig.draw_without_rendering()

    # After we've changed any setting on ticks, reset_ticks will mean
    # re-creating them from scratch. This *should* appear the same as not
    # resetting them.
    for ax in fig_test.axes:
        ax.xaxis.reset_ticks()
        ax.yaxis.reset_ticks()


def test_vline_limit():
    fig = plt.figure()
    ax = fig.gca()
    ax.axvline(0.5)
    ax.plot([-0.1, 0, 0.2, 0.1])
    assert_allclose(ax.get_ylim(), (-.1, .2))


@pytest.mark.parametrize('fv, fh, args', [[plt.axvline, plt.axhline, (1,)],
                                          [plt.axvspan, plt.axhspan, (1, 1)]])
def test_axline_minmax(fv, fh, args):
    bad_lim = matplotlib.dates.num2date(1)
    # Check vertical functions
    with pytest.raises(ValueError, match='ymin must be a single scalar value'):
        fv(*args, ymin=bad_lim, ymax=1)
    with pytest.raises(ValueError, match='ymax must be a single scalar value'):
        fv(*args, ymin=1, ymax=bad_lim)
    # Check horizontal functions
    with pytest.raises(ValueError, match='xmin must be a single scalar value'):
        fh(*args, xmin=bad_lim, xmax=1)
    with pytest.raises(ValueError, match='xmax must be a single scalar value'):
        fh(*args, xmin=1, xmax=bad_lim)


def test_empty_shared_subplots():
    # empty plots with shared axes inherit limits from populated plots
    fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True)
    axs[0].plot([1, 2, 3], [2, 4, 6])
    x0, x1 = axs[1].get_xlim()
    y0, y1 = axs[1].get_ylim()
    assert x0 <= 1
    assert x1 >= 3
    assert y0 <= 2
    assert y1 >= 6


def test_shared_with_aspect_1():
    # allow sharing one axis
    for adjustable in ['box', 'datalim']:
        fig, axs = plt.subplots(nrows=2, sharex=True)
        axs[0].set_aspect(2, adjustable=adjustable, share=True)
        assert axs[1].get_aspect() == 2
        assert axs[1].get_adjustable() == adjustable

        fig, axs = plt.subplots(nrows=2, sharex=True)
        axs[0].set_aspect(2, adjustable=adjustable)
        assert axs[1].get_aspect() == 'auto'


def test_shared_with_aspect_2():
    # Share 2 axes only with 'box':
    fig, axs = plt.subplots(nrows=2, sharex=True, sharey=True)
    axs[0].set_aspect(2, share=True)
    axs[0].plot([1, 2], [3, 4])
    axs[1].plot([3, 4], [1, 2])
    plt.draw()  # Trigger apply_aspect().
    assert axs[0].get_xlim() == axs[1].get_xlim()
    assert axs[0].get_ylim() == axs[1].get_ylim()


def test_shared_with_aspect_3():
    # Different aspect ratios:
    for adjustable in ['box', 'datalim']:
        fig, axs = plt.subplots(nrows=2, sharey=True)
        axs[0].set_aspect(2, adjustable=adjustable)
        axs[1].set_aspect(0.5, adjustable=adjustable)
        axs[0].plot([1, 2], [3, 4])
        axs[1].plot([3, 4], [1, 2])
        plt.draw()  # Trigger apply_aspect().
        assert axs[0].get_xlim() != axs[1].get_xlim()
        assert axs[0].get_ylim() == axs[1].get_ylim()
        fig_aspect = fig.bbox_inches.height / fig.bbox_inches.width
        for ax in axs:
            p = ax.get_position()
            box_aspect = p.height / p.width
            lim_aspect = ax.viewLim.height / ax.viewLim.width
            expected = fig_aspect * box_aspect / lim_aspect
            assert round(expected, 4) == round(ax.get_aspect(), 4)


@pytest.mark.parametrize('err, args, kwargs, match',
                         ((TypeError, (1, 2), {},
                           r"axis\(\) takes 0 or 1 positional arguments but 2"
                           " were given"),
                          (ValueError, ('foo', ), {},
                           "Unrecognized string foo to axis; try on or off"),
                          (TypeError, ([1, 2], ), {},
                           "the first argument to axis*"),
                          (TypeError, tuple(), {'foo': None},
                           r"axis\(\) got an unexpected keyword argument "
                           "'foo'"),
                          ))
def test_axis_errors(err, args, kwargs, match):
    with pytest.raises(err, match=match):
        plt.axis(*args, **kwargs)


@pytest.mark.parametrize('twin', ('x', 'y'))
def test_twin_with_aspect(twin):
    fig, ax = plt.subplots()
    # test twinx or twiny
    ax_twin = getattr(ax, 'twin{}'.format(twin))()
    ax.set_aspect(5)
    ax_twin.set_aspect(2)
    assert_array_equal(ax.bbox.extents,
                       ax_twin.bbox.extents)


def test_relim_visible_only():
    x1 = (0., 10.)
    y1 = (0., 10.)
    x2 = (-10., 20.)
    y2 = (-10., 30.)

    fig = matplotlib.figure.Figure()
    ax = fig.add_subplot()
    ax.plot(x1, y1)
    assert ax.get_xlim() == x1
    assert ax.get_ylim() == y1
    line, = ax.plot(x2, y2)
    assert ax.get_xlim() == x2
    assert ax.get_ylim() == y2
    line.set_visible(False)
    assert ax.get_xlim() == x2
    assert ax.get_ylim() == y2

    ax.relim(visible_only=True)
    ax.autoscale_view()

    assert ax.get_xlim() == x1
    assert ax.get_ylim() == y1


def test_text_labelsize():
    """
    tests for issue #1172
    """
    fig = plt.figure()
    ax = fig.gca()
    ax.tick_params(labelsize='large')
    ax.tick_params(direction='out')


@image_comparison(['pie_default.png'])
def test_pie_default():
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)


@image_comparison(['pie_linewidth_0', 'pie_linewidth_0', 'pie_linewidth_0'],
                  extensions=['png'])
def test_pie_linewidth_0():
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90,
            wedgeprops={'linewidth': 0})
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    # Reuse testcase from above for a labeled data test
    data = {"l": labels, "s": sizes, "c": colors, "ex": explode}
    fig = plt.figure()
    ax = fig.gca()
    ax.pie("s", explode="ex", labels="l", colors="c",
           autopct='%1.1f%%', shadow=True, startangle=90,
           wedgeprops={'linewidth': 0}, data=data)
    ax.axis('equal')

    # And again to test the pyplot functions which should also be able to be
    # called with a data kwarg
    plt.figure()
    plt.pie("s", explode="ex", labels="l", colors="c",
            autopct='%1.1f%%', shadow=True, startangle=90,
            wedgeprops={'linewidth': 0}, data=data)
    plt.axis('equal')


@image_comparison(['pie_center_radius.png'])
def test_pie_center_radius():
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90,
            wedgeprops={'linewidth': 0}, center=(1, 2), radius=1.5)

    plt.annotate("Center point", xy=(1, 2), xytext=(1, 1.3),
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3"),
                 bbox=dict(boxstyle="square", facecolor="lightgrey"))
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')


@image_comparison(['pie_linewidth_2.png'])
def test_pie_linewidth_2():
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90,
            wedgeprops={'linewidth': 2})
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')


@image_comparison(['pie_ccw_true.png'])
def test_pie_ccw_true():
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90,
            counterclock=True)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')


@image_comparison(['pie_frame_grid.png'])
def test_pie_frame_grid():
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = (0, 0.1, 0, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90,
            wedgeprops={'linewidth': 0},
            frame=True, center=(2, 2))

    plt.pie(sizes[::-1], explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90,
            wedgeprops={'linewidth': 0},
            frame=True, center=(5, 2))

    plt.pie(sizes, explode=explode[::-1], labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90,
            wedgeprops={'linewidth': 0},
            frame=True, center=(3, 5))
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')


@image_comparison(['pie_rotatelabels_true.png'])
def test_pie_rotatelabels_true():
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Hogwarts', 'Frogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90,
            rotatelabels=True)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')


@image_comparison(['pie_no_label.png'])
def test_pie_nolabel_but_legend():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90, labeldistance=None,
            rotatelabels=True)
    plt.axis('equal')
    plt.ylim(-1.2, 1.2)
    plt.legend()


def test_pie_textprops():
    data = [23, 34, 45]
    labels = ["Long name 1", "Long name 2", "Long name 3"]

    textprops = dict(horizontalalignment="center",
                     verticalalignment="top",
                     rotation=90,
                     rotation_mode="anchor",
                     size=12, color="red")

    _, texts, autopct = plt.gca().pie(data, labels=labels, autopct='%.2f',
                                      textprops=textprops)
    for labels in [texts, autopct]:
        for tx in labels:
            assert tx.get_ha() == textprops["horizontalalignment"]
            assert tx.get_va() == textprops["verticalalignment"]
            assert tx.get_rotation() == textprops["rotation"]
            assert tx.get_rotation_mode() == textprops["rotation_mode"]
            assert tx.get_size() == textprops["size"]
            assert tx.get_color() == textprops["color"]


def test_pie_get_negative_values():
    # Test the ValueError raised when feeding negative values into axes.pie
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        ax.pie([5, 5, -3], explode=[0, .1, .2])


def test_normalize_kwarg_pie():
    fig, ax = plt.subplots()
    x = [0.3, 0.3, 0.1]
    t1 = ax.pie(x=x, normalize=True)
    assert abs(t1[0][-1].theta2 - 360.) < 1e-3
    t2 = ax.pie(x=x, normalize=False)
    assert abs(t2[0][-1].theta2 - 360.) > 1e-3


@image_comparison(['set_get_ticklabels.png'])
def test_set_get_ticklabels():
    # test issue 2246
    fig, ax = plt.subplots(2)
    ha = ['normal', 'set_x/yticklabels']

    ax[0].plot(np.arange(10))
    ax[0].set_title(ha[0])

    ax[1].plot(np.arange(10))
    ax[1].set_title(ha[1])

    # set ticklabel to 1 plot in normal way
    ax[0].set_xticks(range(10))
    ax[0].set_yticks(range(10))
    ax[0].set_xticklabels(['a', 'b', 'c', 'd'] + 6 * [''])
    ax[0].set_yticklabels(['11', '12', '13', '14'] + 6 * [''])

    # set ticklabel to the other plot, expect the 2 plots have same label
    # setting pass get_ticklabels return value as ticklabels argument
    ax[1].set_xticks(ax[0].get_xticks())
    ax[1].set_yticks(ax[0].get_yticks())
    ax[1].set_xticklabels(ax[0].get_xticklabels())
    ax[1].set_yticklabels(ax[0].get_yticklabels())


@check_figures_equal(extensions=["png"])
def test_set_ticks_with_labels(fig_test, fig_ref):
    """
    Test that these two are identical::

        set_xticks(ticks); set_xticklabels(labels, **kwargs)
        set_xticks(ticks, labels, **kwargs)

    """
    ax = fig_ref.subplots()
    ax.set_xticks([1, 2, 4, 6])
    ax.set_xticklabels(['a', 'b', 'c', 'd'], fontweight='bold')
    ax.set_yticks([1, 3, 5])
    ax.set_yticks([2, 4], minor=True)
    ax.set_yticklabels(['A', 'B'], minor=True)

    ax = fig_test.subplots()
    ax.set_xticks([1, 2, 4, 6], ['a', 'b', 'c', 'd'], fontweight='bold')
    ax.set_yticks([1, 3, 5])
    ax.set_yticks([2, 4], ['A', 'B'], minor=True)


def test_subsampled_ticklabels():
    # test issue 11937
    fig, ax = plt.subplots()
    ax.plot(np.arange(10))
    ax.xaxis.set_ticks(np.arange(10) + 0.1)
    ax.locator_params(nbins=5)
    ax.xaxis.set_ticklabels([c for c in "bcdefghijk"])
    plt.draw()
    labels = [t.get_text() for t in ax.xaxis.get_ticklabels()]
    assert labels == ['b', 'd', 'f', 'h', 'j']


def test_mismatched_ticklabels():
    fig, ax = plt.subplots()
    ax.plot(np.arange(10))
    ax.xaxis.set_ticks([1.5, 2.5])
    with pytest.raises(ValueError):
        ax.xaxis.set_ticklabels(['a', 'b', 'c'])


def test_empty_ticks_fixed_loc():
    # Smoke test that [] can be used to unset all tick labels
    fig, ax = plt.subplots()
    ax.bar([1, 2], [1, 2])
    ax.set_xticks([1, 2])
    ax.set_xticklabels([])


@image_comparison(['retain_tick_visibility.png'])
def test_retain_tick_visibility():
    fig, ax = plt.subplots()
    plt.plot([0, 1, 2], [0, -1, 4])
    plt.setp(ax.get_yticklabels(), visible=False)
    ax.tick_params(axis="y", which="both", length=0)


def test_tick_label_update():
    # test issue 9397

    fig, ax = plt.subplots()

    # Set up a dummy formatter
    def formatter_func(x, pos):
        return "unit value" if x == 1 else ""
    ax.xaxis.set_major_formatter(plt.FuncFormatter(formatter_func))

    # Force some of the x-axis ticks to be outside of the drawn range
    ax.set_xticks([-1, 0, 1, 2, 3])
    ax.set_xlim(-0.5, 2.5)

    ax.figure.canvas.draw()
    tick_texts = [tick.get_text() for tick in ax.xaxis.get_ticklabels()]
    assert tick_texts == ["", "", "unit value", "", ""]


@image_comparison(['o_marker_path_snap.png'], savefig_kwarg={'dpi': 72})
def test_o_marker_path_snap():
    fig, ax = plt.subplots()
    ax.margins(.1)
    for ms in range(1, 15):
        ax.plot([1, 2, ], np.ones(2) + ms, 'o', ms=ms)

    for ms in np.linspace(1, 10, 25):
        ax.plot([3, 4, ], np.ones(2) + ms, 'o', ms=ms)


def test_margins():
    # test all ways margins can be called
    data = [1, 10]
    xmin = 0.0
    xmax = len(data) - 1.0
    ymin = min(data)
    ymax = max(data)

    fig1, ax1 = plt.subplots(1, 1)
    ax1.plot(data)
    ax1.margins(1)
    assert ax1.margins() == (1, 1)
    assert ax1.get_xlim() == (xmin - (xmax - xmin) * 1,
                              xmax + (xmax - xmin) * 1)
    assert ax1.get_ylim() == (ymin - (ymax - ymin) * 1,
                              ymax + (ymax - ymin) * 1)

    fig2, ax2 = plt.subplots(1, 1)
    ax2.plot(data)
    ax2.margins(0.5, 2)
    assert ax2.margins() == (0.5, 2)
    assert ax2.get_xlim() == (xmin - (xmax - xmin) * 0.5,
                              xmax + (xmax - xmin) * 0.5)
    assert ax2.get_ylim() == (ymin - (ymax - ymin) * 2,
                              ymax + (ymax - ymin) * 2)

    fig3, ax3 = plt.subplots(1, 1)
    ax3.plot(data)
    ax3.margins(x=-0.2, y=0.5)
    assert ax3.margins() == (-0.2, 0.5)
    assert ax3.get_xlim() == (xmin - (xmax - xmin) * -0.2,
                              xmax + (xmax - xmin) * -0.2)
    assert ax3.get_ylim() == (ymin - (ymax - ymin) * 0.5,
                              ymax + (ymax - ymin) * 0.5)


def test_set_margin_updates_limits():
    mpl.style.use("default")
    fig, ax = plt.subplots()
    ax.plot([1, 2], [1, 2])
    ax.set(xscale="log", xmargin=0)
    assert ax.get_xlim() == (1, 2)


@pytest.mark.parametrize('err, args, kwargs, match',
                         ((ValueError, (-1,), {},
                           'margin must be greater than -0.5'),
                          (ValueError, (1, -1), {},
                           'margin must be greater than -0.5'),
                          (ValueError, tuple(), {'x': -1},
                           'margin must be greater than -0.5'),
                          (ValueError, tuple(), {'y': -1},
                           'margin must be greater than -0.5'),
                          (TypeError, (1, ), {'x': 1, 'y': 1},
                           'Cannot pass both positional and keyword '
                           'arguments for x and/or y.'),
                          (TypeError, (1, 1, 1), {},
                           'Must pass a single positional argument for all*'),
                          ))
def test_margins_errors(err, args, kwargs, match):
    with pytest.raises(err, match=match):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.margins(*args, **kwargs)


def test_length_one_hist():
    fig, ax = plt.subplots()
    ax.hist(1)
    ax.hist([1])


def test_set_xy_bound():
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xbound(2.0, 3.0)
    assert ax.get_xbound() == (2.0, 3.0)
    assert ax.get_xlim() == (2.0, 3.0)
    ax.set_xbound(upper=4.0)
    assert ax.get_xbound() == (2.0, 4.0)
    assert ax.get_xlim() == (2.0, 4.0)
    ax.set_xbound(lower=3.0)
    assert ax.get_xbound() == (3.0, 4.0)
    assert ax.get_xlim() == (3.0, 4.0)

    ax.set_ybound(2.0, 3.0)
    assert ax.get_ybound() == (2.0, 3.0)
    assert ax.get_ylim() == (2.0, 3.0)
    ax.set_ybound(upper=4.0)
    assert ax.get_ybound() == (2.0, 4.0)
    assert ax.get_ylim() == (2.0, 4.0)
    ax.set_ybound(lower=3.0)
    assert ax.get_ybound() == (3.0, 4.0)
    assert ax.get_ylim() == (3.0, 4.0)


def test_pathological_hexbin():
    # issue #2863
    mylist = [10] * 100
    fig, ax = plt.subplots(1, 1)
    ax.hexbin(mylist, mylist)
    fig.savefig(io.BytesIO())  # Check that no warning is emitted.


def test_color_None():
    # issue 3855
    fig, ax = plt.subplots()
    ax.plot([1, 2], [1, 2], color=None)


def test_color_alias():
    # issues 4157 and 4162
    fig, ax = plt.subplots()
    line = ax.plot([0, 1], c='lime')[0]
    assert 'lime' == line.get_color()


def test_numerical_hist_label():
    fig, ax = plt.subplots()
    ax.hist([range(15)] * 5, label=range(5))
    ax.legend()


def test_unicode_hist_label():
    fig, ax = plt.subplots()
    a = (b'\xe5\xbe\x88\xe6\xbc\x82\xe4\xba\xae, ' +
         b'r\xc3\xb6m\xc3\xa4n ch\xc3\xa4r\xc3\xa1ct\xc3\xa8rs')
    b = b'\xd7\xa9\xd7\x9c\xd7\x95\xd7\x9d'
    labels = [a.decode('utf-8'),
              'hi aardvark',
              b.decode('utf-8'),
              ]

    ax.hist([range(15)] * 3, label=labels)
    ax.legend()


def test_move_offsetlabel():
    data = np.random.random(10) * 1e-22

    fig, ax = plt.subplots()
    ax.plot(data)
    fig.canvas.draw()
    before = ax.yaxis.offsetText.get_position()
    assert ax.yaxis.offsetText.get_horizontalalignment() == 'left'
    ax.yaxis.tick_right()
    fig.canvas.draw()
    after = ax.yaxis.offsetText.get_position()
    assert after[0] > before[0] and after[1] == before[1]
    assert ax.yaxis.offsetText.get_horizontalalignment() == 'right'

    fig, ax = plt.subplots()
    ax.plot(data)
    fig.canvas.draw()
    before = ax.xaxis.offsetText.get_position()
    assert ax.xaxis.offsetText.get_verticalalignment() == 'top'
    ax.xaxis.tick_top()
    fig.canvas.draw()
    after = ax.xaxis.offsetText.get_position()
    assert after[0] == before[0] and after[1] > before[1]
    assert ax.xaxis.offsetText.get_verticalalignment() == 'bottom'


@image_comparison(['rc_spines.png'], savefig_kwarg={'dpi': 40})
def test_rc_spines():
    rc_dict = {
        'axes.spines.left': False,
        'axes.spines.right': False,
        'axes.spines.top': False,
        'axes.spines.bottom': False}
    with matplotlib.rc_context(rc_dict):
        plt.subplots()  # create a figure and axes with the spine properties


@image_comparison(['rc_grid.png'], savefig_kwarg={'dpi': 40})
def test_rc_grid():
    fig = plt.figure()
    rc_dict0 = {
        'axes.grid': True,
        'axes.grid.axis': 'both'
    }
    rc_dict1 = {
        'axes.grid': True,
        'axes.grid.axis': 'x'
    }
    rc_dict2 = {
        'axes.grid': True,
        'axes.grid.axis': 'y'
    }
    dict_list = [rc_dict0, rc_dict1, rc_dict2]

    for i, rc_dict in enumerate(dict_list, 1):
        with matplotlib.rc_context(rc_dict):
            fig.add_subplot(3, 1, i)


def test_rc_tick():
    d = {'xtick.bottom': False, 'xtick.top': True,
         'ytick.left': True, 'ytick.right': False}
    with plt.rc_context(rc=d):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        xax = ax1.xaxis
        yax = ax1.yaxis
        # tick1On bottom/left
        assert not xax._major_tick_kw['tick1On']
        assert xax._major_tick_kw['tick2On']
        assert not xax._minor_tick_kw['tick1On']
        assert xax._minor_tick_kw['tick2On']

        assert yax._major_tick_kw['tick1On']
        assert not yax._major_tick_kw['tick2On']
        assert yax._minor_tick_kw['tick1On']
        assert not yax._minor_tick_kw['tick2On']


def test_rc_major_minor_tick():
    d = {'xtick.top': True, 'ytick.right': True,  # Enable all ticks
         'xtick.bottom': True, 'ytick.left': True,
         # Selectively disable
         'xtick.minor.bottom': False, 'xtick.major.bottom': False,
         'ytick.major.left': False, 'ytick.minor.left': False}
    with plt.rc_context(rc=d):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        xax = ax1.xaxis
        yax = ax1.yaxis
        # tick1On bottom/left
        assert not xax._major_tick_kw['tick1On']
        assert xax._major_tick_kw['tick2On']
        assert not xax._minor_tick_kw['tick1On']
        assert xax._minor_tick_kw['tick2On']

        assert not yax._major_tick_kw['tick1On']
        assert yax._major_tick_kw['tick2On']
        assert not yax._minor_tick_kw['tick1On']
        assert yax._minor_tick_kw['tick2On']


def test_square_plot():
    x = np.arange(4)
    y = np.array([1., 3., 5., 7.])
    fig, ax = plt.subplots()
    ax.plot(x, y, 'mo')
    ax.axis('square')
    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    assert np.diff(xlim) == np.diff(ylim)
    assert ax.get_aspect() == 1
    assert_array_almost_equal(
        ax.get_position(original=True).extents, (0.125, 0.1, 0.9, 0.9))
    assert_array_almost_equal(
        ax.get_position(original=False).extents, (0.2125, 0.1, 0.8125, 0.9))


def test_bad_plot_args():
    with pytest.raises(ValueError):
        plt.plot(None)
    with pytest.raises(ValueError):
        plt.plot(None, None)
    with pytest.raises(ValueError):
        plt.plot(np.zeros((2, 2)), np.zeros((2, 3)))
    with pytest.raises(ValueError):
        plt.plot((np.arange(5).reshape((1, -1)), np.arange(5).reshape(-1, 1)))


@pytest.mark.parametrize(
    "xy, cls", [
        ((), mpl.image.AxesImage),  # (0, N)
        (((3, 7), (2, 6)), mpl.image.AxesImage),  # (xmin, xmax)
        ((range(5), range(4)), mpl.image.AxesImage),  # regular grid
        (([1, 2, 4, 8, 16], [0, 1, 2, 3]),  # irregular grid
         mpl.image.PcolorImage),
        ((np.random.random((4, 5)), np.random.random((4, 5))),  # 2D coords
         mpl.collections.QuadMesh),
    ]
)
@pytest.mark.parametrize(
    "data", [np.arange(12).reshape((3, 4)), np.random.rand(3, 4, 3)]
)
def test_pcolorfast(xy, data, cls):
    fig, ax = plt.subplots()
    assert type(ax.pcolorfast(*xy, data)) == cls


def test_shared_scale():
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

    axs[0, 0].set_xscale("log")
    axs[0, 0].set_yscale("log")

    for ax in axs.flat:
        assert ax.get_yscale() == 'log'
        assert ax.get_xscale() == 'log'

    axs[1, 1].set_xscale("linear")
    axs[1, 1].set_yscale("linear")

    for ax in axs.flat:
        assert ax.get_yscale() == 'linear'
        assert ax.get_xscale() == 'linear'


def test_shared_bool():
    with pytest.raises(TypeError):
        plt.subplot(sharex=True)
    with pytest.raises(TypeError):
        plt.subplot(sharey=True)


def test_violin_point_mass():
    """Violin plot should handle point mass pdf gracefully."""
    plt.violinplot(np.array([0, 0]))


def generate_errorbar_inputs():
    base_xy = cycler('x', [np.arange(5)]) + cycler('y', [np.ones(5)])
    err_cycler = cycler('err', [1,
                                [1, 1, 1, 1, 1],
                                [[1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 1]],
                                np.ones(5),
                                np.ones((2, 5)),
                                None
                                ])
    xerr_cy = cycler('xerr', err_cycler)
    yerr_cy = cycler('yerr', err_cycler)

    empty = ((cycler('x', [[]]) + cycler('y', [[]])) *
             cycler('xerr', [[], None]) * cycler('yerr', [[], None]))
    xerr_only = base_xy * xerr_cy
    yerr_only = base_xy * yerr_cy
    both_err = base_xy * yerr_cy * xerr_cy

    return [*xerr_only, *yerr_only, *both_err, *empty]


@pytest.mark.parametrize('kwargs', generate_errorbar_inputs())
def test_errorbar_inputs_shotgun(kwargs):
    ax = plt.gca()
    eb = ax.errorbar(**kwargs)
    eb.remove()


@image_comparison(["dash_offset"], remove_text=True)
def test_dash_offset():
    fig, ax = plt.subplots()
    x = np.linspace(0, 10)
    y = np.ones_like(x)
    for j in range(0, 100, 2):
        ax.plot(x, j*y, ls=(j, (10, 10)), lw=5, color='k')


def test_title_pad():
    # check that title padding puts the title in the right
    # place...
    fig, ax = plt.subplots()
    ax.set_title('aardvark', pad=30.)
    m = ax.titleOffsetTrans.get_matrix()
    assert m[1, -1] == (30. / 72. * fig.dpi)
    ax.set_title('aardvark', pad=0.)
    m = ax.titleOffsetTrans.get_matrix()
    assert m[1, -1] == 0.
    # check that it is reverted...
    ax.set_title('aardvark', pad=None)
    m = ax.titleOffsetTrans.get_matrix()
    assert m[1, -1] == (matplotlib.rcParams['axes.titlepad'] / 72. * fig.dpi)


def test_title_location_roundtrip():
    fig, ax = plt.subplots()
    # set default title location
    plt.rcParams['axes.titlelocation'] = 'center'
    ax.set_title('aardvark')
    ax.set_title('left', loc='left')
    ax.set_title('right', loc='right')

    assert 'left' == ax.get_title(loc='left')
    assert 'right' == ax.get_title(loc='right')
    assert 'aardvark' == ax.get_title(loc='center')

    with pytest.raises(ValueError):
        ax.get_title(loc='foo')
    with pytest.raises(ValueError):
        ax.set_title('fail', loc='foo')


@image_comparison(["loglog.png"], remove_text=True, tol=0.02)
def test_loglog():
    fig, ax = plt.subplots()
    x = np.arange(1, 11)
    ax.loglog(x, x**3, lw=5)
    ax.tick_params(length=25, width=2)
    ax.tick_params(length=15, width=2, which='minor')


@image_comparison(["test_loglog_nonpos.png"], remove_text=True, style='mpl20')
def test_loglog_nonpos():
    fig, axs = plt.subplots(3, 3)
    x = np.arange(1, 11)
    y = x**3
    y[7] = -3.
    x[4] = -10
    for (mcy, mcx), ax in zip(product(['mask', 'clip', ''], repeat=2),
                              axs.flat):
        if mcx == mcy:
            if mcx:
                ax.loglog(x, y**3, lw=2, nonpositive=mcx)
            else:
                ax.loglog(x, y**3, lw=2)
        else:
            ax.loglog(x, y**3, lw=2)
            if mcx:
                ax.set_xscale("log", nonpositive=mcx)
            if mcy:
                ax.set_yscale("log", nonpositive=mcy)


@mpl.style.context('default')
def test_axes_margins():
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3])
    assert ax.get_ybound()[0] != 0

    fig, ax = plt.subplots()
    ax.bar([0, 1, 2, 3], [1, 1, 1, 1])
    assert ax.get_ybound()[0] == 0

    fig, ax = plt.subplots()
    ax.barh([0, 1, 2, 3], [1, 1, 1, 1])
    assert ax.get_xbound()[0] == 0

    fig, ax = plt.subplots()
    ax.pcolor(np.zeros((10, 10)))
    assert ax.get_xbound() == (0, 10)
    assert ax.get_ybound() == (0, 10)

    fig, ax = plt.subplots()
    ax.pcolorfast(np.zeros((10, 10)))
    assert ax.get_xbound() == (0, 10)
    assert ax.get_ybound() == (0, 10)

    fig, ax = plt.subplots()
    ax.hist(np.arange(10))
    assert ax.get_ybound()[0] == 0

    fig, ax = plt.subplots()
    ax.imshow(np.zeros((10, 10)))
    assert ax.get_xbound() == (-0.5, 9.5)
    assert ax.get_ybound() == (-0.5, 9.5)


@pytest.fixture(params=['x', 'y'])
def shared_axis_remover(request):
    def _helper_x(ax):
        ax2 = ax.twinx()
        ax2.remove()
        ax.set_xlim(0, 15)
        r = ax.xaxis.get_major_locator()()
        assert r[-1] > 14

    def _helper_y(ax):
        ax2 = ax.twiny()
        ax2.remove()
        ax.set_ylim(0, 15)
        r = ax.yaxis.get_major_locator()()
        assert r[-1] > 14

    return {"x": _helper_x, "y": _helper_y}[request.param]


@pytest.fixture(params=['gca', 'subplots', 'subplots_shared', 'add_axes'])
def shared_axes_generator(request):
    # test all of the ways to get fig/ax sets
    if request.param == 'gca':
        fig = plt.figure()
        ax = fig.gca()
    elif request.param == 'subplots':
        fig, ax = plt.subplots()
    elif request.param == 'subplots_shared':
        fig, ax_lst = plt.subplots(2, 2, sharex='all', sharey='all')
        ax = ax_lst[0][0]
    elif request.param == 'add_axes':
        fig = plt.figure()
        ax = fig.add_axes([.1, .1, .8, .8])
    return fig, ax


def test_remove_shared_axes(shared_axes_generator, shared_axis_remover):
    # test all of the ways to get fig/ax sets
    fig, ax = shared_axes_generator
    shared_axis_remover(ax)


def test_remove_shared_axes_relim():
    fig, ax_lst = plt.subplots(2, 2, sharex='all', sharey='all')
    ax = ax_lst[0][0]
    orig_xlim = ax_lst[0][1].get_xlim()
    ax.remove()
    ax.set_xlim(0, 5)
    assert_array_equal(ax_lst[0][1].get_xlim(), orig_xlim)


def test_shared_axes_autoscale():
    l = np.arange(-80, 90, 40)
    t = np.random.random_sample((l.size, l.size))

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=True)

    ax1.set_xlim(-1000, 1000)
    ax1.set_ylim(-1000, 1000)
    ax1.contour(l, l, t)

    ax2.contour(l, l, t)
    assert not ax1.get_autoscalex_on() and not ax2.get_autoscalex_on()
    assert not ax1.get_autoscaley_on() and not ax2.get_autoscaley_on()
    assert ax1.get_xlim() == ax2.get_xlim() == (-1000, 1000)
    assert ax1.get_ylim() == ax2.get_ylim() == (-1000, 1000)


def test_adjust_numtick_aspect():
    fig, ax = plt.subplots()
    ax.yaxis.get_major_locator().set_params(nbins='auto')
    ax.set_xlim(0, 1000)
    ax.set_aspect('equal')
    fig.canvas.draw()
    assert len(ax.yaxis.get_major_locator()()) == 2
    ax.set_ylim(0, 1000)
    fig.canvas.draw()
    assert len(ax.yaxis.get_major_locator()()) > 2


@image_comparison(["auto_numticks.png"], style='default')
def test_auto_numticks():
    # Make tiny, empty subplots, verify that there are only 3 ticks.
    plt.subplots(4, 4)


@image_comparison(["auto_numticks_log.png"], style='default')
def test_auto_numticks_log():
    # Verify that there are not too many ticks with a large log range.
    fig, ax = plt.subplots()
    matplotlib.rcParams['axes.autolimit_mode'] = 'round_numbers'
    ax.loglog([1e-20, 1e5], [1e-16, 10])


def test_broken_barh_empty():
    fig, ax = plt.subplots()
    ax.broken_barh([], (.1, .5))


def test_broken_barh_timedelta():
    """Check that timedelta works as x, dx pair for this method."""
    fig, ax = plt.subplots()
    d0 = datetime.datetime(2018, 11, 9, 0, 0, 0)
    pp = ax.broken_barh([(d0, datetime.timedelta(hours=1))], [1, 2])
    assert pp.get_paths()[0].vertices[0, 0] == mdates.date2num(d0)
    assert pp.get_paths()[0].vertices[2, 0] == mdates.date2num(d0) + 1 / 24


def test_pandas_pcolormesh(pd):
    time = pd.date_range('2000-01-01', periods=10)
    depth = np.arange(20)
    data = np.random.rand(19, 9)

    fig, ax = plt.subplots()
    ax.pcolormesh(time, depth, data)


def test_pandas_indexing_dates(pd):
    dates = np.arange('2005-02', '2005-03', dtype='datetime64[D]')
    values = np.sin(np.array(range(len(dates))))
    df = pd.DataFrame({'dates': dates, 'values': values})

    ax = plt.gca()

    without_zero_index = df[np.array(df.index) % 2 == 1].copy()
    ax.plot('dates', 'values', data=without_zero_index)


def test_pandas_errorbar_indexing(pd):
    df = pd.DataFrame(np.random.uniform(size=(5, 4)),
                      columns=['x', 'y', 'xe', 'ye'],
                      index=[1, 2, 3, 4, 5])
    fig, ax = plt.subplots()
    ax.errorbar('x', 'y', xerr='xe', yerr='ye', data=df)


def test_pandas_index_shape(pd):
    df = pd.DataFrame({"XX": [4, 5, 6], "YY": [7, 1, 2]})
    fig, ax = plt.subplots()
    ax.plot(df.index, df['YY'])


def test_pandas_indexing_hist(pd):
    ser_1 = pd.Series(data=[1, 2, 2, 3, 3, 4, 4, 4, 4, 5])
    ser_2 = ser_1.iloc[1:]
    fig, ax = plt.subplots()
    ax.hist(ser_2)


def test_pandas_bar_align_center(pd):
    # Tests fix for issue 8767
    df = pd.DataFrame({'a': range(2), 'b': range(2)})

    fig, ax = plt.subplots(1)

    ax.bar(df.loc[df['a'] == 1, 'b'],
           df.loc[df['a'] == 1, 'b'],
           align='center')

    fig.canvas.draw()


def test_tick_apply_tickdir_deprecation():
    # Remove this test when the deprecation expires.
    import matplotlib.axis as maxis
    ax = plt.axes()

    tick = maxis.XTick(ax, 0)
    with pytest.warns(MatplotlibDeprecationWarning,
                      match="The apply_tickdir function was deprecated in "
                            "Matplotlib 3.5"):
        tick.apply_tickdir('out')

    tick = maxis.YTick(ax, 0)
    with pytest.warns(MatplotlibDeprecationWarning,
                      match="The apply_tickdir function was deprecated in "
                            "Matplotlib 3.5"):
        tick.apply_tickdir('out')


def test_axis_set_tick_params_labelsize_labelcolor():
    # Tests fix for issue 4346
    axis_1 = plt.subplot()
    axis_1.yaxis.set_tick_params(labelsize=30, labelcolor='red',
                                 direction='out')

    # Expected values after setting the ticks
    assert axis_1.yaxis.majorTicks[0]._size == 4.0
    assert axis_1.yaxis.majorTicks[0].tick1line.get_color() == 'k'
    assert axis_1.yaxis.majorTicks[0].label1.get_size() == 30.0
    assert axis_1.yaxis.majorTicks[0].label1.get_color() == 'red'


def test_axes_tick_params_gridlines():
    # Now treating grid params like other Tick params
    ax = plt.subplot()
    ax.tick_params(grid_color='b', grid_linewidth=5, grid_alpha=0.5,
                   grid_linestyle='dashdot')
    for axis in ax.xaxis, ax.yaxis:
        assert axis.majorTicks[0].gridline.get_color() == 'b'
        assert axis.majorTicks[0].gridline.get_linewidth() == 5
        assert axis.majorTicks[0].gridline.get_alpha() == 0.5
        assert axis.majorTicks[0].gridline.get_linestyle() == '-.'


def test_axes_tick_params_ylabelside():
    # Tests fix for issue 10267
    ax = plt.subplot()
    ax.tick_params(labelleft=False, labelright=True,
                   which='major')
    ax.tick_params(labelleft=False, labelright=True,
                   which='minor')
    # expects left false, right true
    assert ax.yaxis.majorTicks[0].label1.get_visible() is False
    assert ax.yaxis.majorTicks[0].label2.get_visible() is True
    assert ax.yaxis.minorTicks[0].label1.get_visible() is False
    assert ax.yaxis.minorTicks[0].label2.get_visible() is True


def test_axes_tick_params_xlabelside():
    # Tests fix for issue 10267
    ax = plt.subplot()
    ax.tick_params(labeltop=True, labelbottom=False,
                   which='major')
    ax.tick_params(labeltop=True, labelbottom=False,
                   which='minor')
    # expects top True, bottom False
    # label1.get_visible() mapped to labelbottom
    # label2.get_visible() mapped to labeltop
    assert ax.xaxis.majorTicks[0].label1.get_visible() is False
    assert ax.xaxis.majorTicks[0].label2.get_visible() is True
    assert ax.xaxis.minorTicks[0].label1.get_visible() is False
    assert ax.xaxis.minorTicks[0].label2.get_visible() is True


def test_none_kwargs():
    ax = plt.figure().subplots()
    ln, = ax.plot(range(32), linestyle=None)
    assert ln.get_linestyle() == '-'


def test_bar_uint8():
    xs = [0, 1, 2, 3]
    b = plt.bar(np.array(xs, dtype=np.uint8), [2, 3, 4, 5], align="edge")
    for (patch, x) in zip(b.patches, xs):
        assert patch.xy[0] == x


@image_comparison(['date_timezone_x.png'], tol=1.0)
def test_date_timezone_x():
    # Tests issue 5575
    time_index = [datetime.datetime(2016, 2, 22, hour=x,
                                    tzinfo=dateutil.tz.gettz('Canada/Eastern'))
                  for x in range(3)]

    # Same Timezone
    plt.figure(figsize=(20, 12))
    plt.subplot(2, 1, 1)
    plt.plot_date(time_index, [3] * 3, tz='Canada/Eastern')

    # Different Timezone
    plt.subplot(2, 1, 2)
    plt.plot_date(time_index, [3] * 3, tz='UTC')


@image_comparison(['date_timezone_y.png'])
def test_date_timezone_y():
    # Tests issue 5575
    time_index = [datetime.datetime(2016, 2, 22, hour=x,
                                    tzinfo=dateutil.tz.gettz('Canada/Eastern'))
                  for x in range(3)]

    # Same Timezone
    plt.figure(figsize=(20, 12))
    plt.subplot(2, 1, 1)
    plt.plot_date([3] * 3,
                  time_index, tz='Canada/Eastern', xdate=False, ydate=True)

    # Different Timezone
    plt.subplot(2, 1, 2)
    plt.plot_date([3] * 3, time_index, tz='UTC', xdate=False, ydate=True)


@image_comparison(['date_timezone_x_and_y.png'], tol=1.0)
def test_date_timezone_x_and_y():
    # Tests issue 5575
    UTC = datetime.timezone.utc
    time_index = [datetime.datetime(2016, 2, 22, hour=x, tzinfo=UTC)
                  for x in range(3)]

    # Same Timezone
    plt.figure(figsize=(20, 12))
    plt.subplot(2, 1, 1)
    plt.plot_date(time_index, time_index, tz='UTC', ydate=True)

    # Different Timezone
    plt.subplot(2, 1, 2)
    plt.plot_date(time_index, time_index, tz='US/Eastern', ydate=True)


@image_comparison(['axisbelow.png'], remove_text=True)
def test_axisbelow():
    # Test 'line' setting added in 6287.
    # Show only grids, not frame or ticks, to make this test
    # independent of future change to drawing order of those elements.
    axs = plt.figure().subplots(ncols=3, sharex=True, sharey=True)
    settings = (False, 'line', True)

    for ax, setting in zip(axs, settings):
        ax.plot((0, 10), (0, 10), lw=10, color='m')
        circ = mpatches.Circle((3, 3), color='r')
        ax.add_patch(circ)
        ax.grid(color='c', linestyle='-', linewidth=3)
        ax.tick_params(top=False, bottom=False,
                       left=False, right=False)
        ax.spines[:].set_visible(False)
        ax.set_axisbelow(setting)
        assert ax.get_axisbelow() == setting


def test_titletwiny():
    plt.style.use('mpl20')
    fig, ax = plt.subplots(dpi=72)
    ax2 = ax.twiny()
    xlabel2 = ax2.set_xlabel('Xlabel2')
    title = ax.set_title('Title')
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    # ------- Test that title is put above Xlabel2 (Xlabel2 at top) ----------
    bbox_y0_title = title.get_window_extent(renderer).y0  # bottom of title
    bbox_y1_xlabel2 = xlabel2.get_window_extent(renderer).y1  # top of xlabel2
    y_diff = bbox_y0_title - bbox_y1_xlabel2
    assert np.isclose(y_diff, 3)


def test_titlesetpos():
    # Test that title stays put if we set it manually
    fig, ax = plt.subplots()
    fig.subplots_adjust(top=0.8)
    ax2 = ax.twiny()
    ax.set_xlabel('Xlabel')
    ax2.set_xlabel('Xlabel2')
    ax.set_title('Title')
    pos = (0.5, 1.11)
    ax.title.set_position(pos)
    renderer = fig.canvas.get_renderer()
    ax._update_title_position(renderer)
    assert ax.title.get_position() == pos


def test_title_xticks_top():
    # Test that title moves if xticks on top of axes.
    mpl.rcParams['axes.titley'] = None
    fig, ax = plt.subplots()
    ax.xaxis.set_ticks_position('top')
    ax.set_title('xlabel top')
    fig.canvas.draw()
    assert ax.title.get_position()[1] > 1.04


def test_title_xticks_top_both():
    # Test that title moves if xticks on top of axes.
    mpl.rcParams['axes.titley'] = None
    fig, ax = plt.subplots()
    ax.tick_params(axis="x",
                   bottom=True, top=True, labelbottom=True, labeltop=True)
    ax.set_title('xlabel top')
    fig.canvas.draw()
    assert ax.title.get_position()[1] > 1.04


def test_title_no_move_off_page():
    # If an axes is off the figure (ie. if it is cropped during a save)
    # make sure that the automatic title repositioning does not get done.
    mpl.rcParams['axes.titley'] = None
    fig = plt.figure()
    ax = fig.add_axes([0.1, -0.5, 0.8, 0.2])
    ax.tick_params(axis="x",
                   bottom=True, top=True, labelbottom=True, labeltop=True)
    tt = ax.set_title('Boo')
    fig.canvas.draw()
    assert tt.get_position()[1] == 1.0


def test_offset_label_color():
    # Tests issue 6440
    fig, ax = plt.subplots()
    ax.plot([1.01e9, 1.02e9, 1.03e9])
    ax.yaxis.set_tick_params(labelcolor='red')
    assert ax.yaxis.get_offset_text().get_color() == 'red'


def test_offset_text_visible():
    fig, ax = plt.subplots()
    ax.plot([1.01e9, 1.02e9, 1.03e9])
    ax.yaxis.set_tick_params(label1On=False, label2On=True)
    assert ax.yaxis.get_offset_text().get_visible()
    ax.yaxis.set_tick_params(label2On=False)
    assert not ax.yaxis.get_offset_text().get_visible()


def test_large_offset():
    fig, ax = plt.subplots()
    ax.plot((1 + np.array([0, 1.e-12])) * 1.e27)
    fig.canvas.draw()


def test_barb_units():
    fig, ax = plt.subplots()
    dates = [datetime.datetime(2017, 7, 15, 18, i) for i in range(0, 60, 10)]
    y = np.linspace(0, 5, len(dates))
    u = v = np.linspace(0, 50, len(dates))
    ax.barbs(dates, y, u, v)


def test_quiver_units():
    fig, ax = plt.subplots()
    dates = [datetime.datetime(2017, 7, 15, 18, i) for i in range(0, 60, 10)]
    y = np.linspace(0, 5, len(dates))
    u = v = np.linspace(0, 50, len(dates))
    ax.quiver(dates, y, u, v)


def test_bar_color_cycle():
    to_rgb = mcolors.to_rgb
    fig, ax = plt.subplots()
    for j in range(5):
        ln, = ax.plot(range(3))
        brs = ax.bar(range(3), range(3))
        for br in brs:
            assert to_rgb(ln.get_color()) == to_rgb(br.get_facecolor())


def test_tick_param_label_rotation():
    fix, (ax, ax2) = plt.subplots(1, 2)
    ax.plot([0, 1], [0, 1])
    ax2.plot([0, 1], [0, 1])
    ax.xaxis.set_tick_params(which='both', rotation=75)
    ax.yaxis.set_tick_params(which='both', rotation=90)
    for text in ax.get_xticklabels(which='both'):
        assert text.get_rotation() == 75
    for text in ax.get_yticklabels(which='both'):
        assert text.get_rotation() == 90

    ax2.tick_params(axis='x', labelrotation=53)
    ax2.tick_params(axis='y', rotation=35)
    for text in ax2.get_xticklabels(which='major'):
        assert text.get_rotation() == 53
    for text in ax2.get_yticklabels(which='major'):
        assert text.get_rotation() == 35


@mpl.style.context('default')
def test_fillbetween_cycle():
    fig, ax = plt.subplots()

    for j in range(3):
        cc = ax.fill_between(range(3), range(3))
        target = mcolors.to_rgba('C{}'.format(j))
        assert tuple(cc.get_facecolors().squeeze()) == tuple(target)

    for j in range(3, 6):
        cc = ax.fill_betweenx(range(3), range(3))
        target = mcolors.to_rgba('C{}'.format(j))
        assert tuple(cc.get_facecolors().squeeze()) == tuple(target)

    target = mcolors.to_rgba('k')

    for al in ['facecolor', 'facecolors', 'color']:
        cc = ax.fill_between(range(3), range(3), **{al: 'k'})
        assert tuple(cc.get_facecolors().squeeze()) == tuple(target)

    edge_target = mcolors.to_rgba('k')
    for j, el in enumerate(['edgecolor', 'edgecolors'], start=6):
        cc = ax.fill_between(range(3), range(3), **{el: 'k'})
        face_target = mcolors.to_rgba('C{}'.format(j))
        assert tuple(cc.get_facecolors().squeeze()) == tuple(face_target)
        assert tuple(cc.get_edgecolors().squeeze()) == tuple(edge_target)


def test_log_margins():
    plt.rcParams['axes.autolimit_mode'] = 'data'
    fig, ax = plt.subplots()
    margin = 0.05
    ax.set_xmargin(margin)
    ax.semilogx([10, 100], [10, 100])
    xlim0, xlim1 = ax.get_xlim()
    transform = ax.xaxis.get_transform()
    xlim0t, xlim1t = transform.transform([xlim0, xlim1])
    x0t, x1t = transform.transform([10, 100])
    delta = (x1t - x0t) * margin
    assert_allclose([xlim0t + delta, xlim1t - delta], [x0t, x1t])


def test_color_length_mismatch():
    N = 5
    x, y = np.arange(N), np.arange(N)
    colors = np.arange(N+1)
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        ax.scatter(x, y, c=colors)
    c_rgb = (0.5, 0.5, 0.5)
    ax.scatter(x, y, c=c_rgb)
    ax.scatter(x, y, c=[c_rgb] * N)


def test_eventplot_legend():
    plt.eventplot([1.0], label='Label')
    plt.legend()


def test_bar_broadcast_args():
    fig, ax = plt.subplots()
    # Check that a bar chart with a single height for all bars works.
    ax.bar(range(4), 1)
    # Check that a horizontal chart with one width works.
    ax.barh(0, 1, left=range(4), height=1)
    # Check that edgecolor gets broadcast.
    rect1, rect2 = ax.bar([0, 1], [0, 1], edgecolor=(.1, .2, .3, .4))
    assert rect1.get_edgecolor() == rect2.get_edgecolor() == (.1, .2, .3, .4)


def test_invalid_axis_limits():
    plt.plot([0, 1], [0, 1])
    with pytest.raises(ValueError):
        plt.xlim(np.nan)
    with pytest.raises(ValueError):
        plt.xlim(np.inf)
    with pytest.raises(ValueError):
        plt.ylim(np.nan)
    with pytest.raises(ValueError):
        plt.ylim(np.inf)


# Test all 4 combinations of logs/symlogs for minorticks_on()
@pytest.mark.parametrize('xscale', ['symlog', 'log'])
@pytest.mark.parametrize('yscale', ['symlog', 'log'])
def test_minorticks_on(xscale, yscale):
    ax = plt.subplot()
    ax.plot([1, 2, 3, 4])
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)
    ax.minorticks_on()


def test_twinx_knows_limits():
    fig, ax = plt.subplots()

    ax.axvspan(1, 2)
    xtwin = ax.twinx()
    xtwin.plot([0, 0.5], [1, 2])
    # control axis
    fig2, ax2 = plt.subplots()

    ax2.axvspan(1, 2)
    ax2.plot([0, 0.5], [1, 2])

    assert_array_equal(xtwin.viewLim.intervalx, ax2.viewLim.intervalx)


def test_zero_linewidth():
    # Check that setting a zero linewidth doesn't error
    plt.plot([0, 1], [0, 1], ls='--', lw=0)


def test_empty_errorbar_legend():
    fig, ax = plt.subplots()
    ax.errorbar([], [], xerr=[], label='empty y')
    ax.errorbar([], [], yerr=[], label='empty x')
    ax.legend()


@check_figures_equal(extensions=["png"])
def test_plot_decimal(fig_test, fig_ref):
    x0 = np.arange(-10, 10, 0.3)
    y0 = [5.2 * x ** 3 - 2.1 * x ** 2 + 7.34 * x + 4.5 for x in x0]
    x = [Decimal(i) for i in x0]
    y = [Decimal(i) for i in y0]
    # Test image - line plot with Decimal input
    fig_test.subplots().plot(x, y)
    # Reference image
    fig_ref.subplots().plot(x0, y0)


# pdf and svg tests fail using travis' old versions of gs and inkscape.
@check_figures_equal(extensions=["png"])
def test_markerfacecolor_none_alpha(fig_test, fig_ref):
    fig_test.subplots().plot(0, "o", mfc="none", alpha=.5)
    fig_ref.subplots().plot(0, "o", mfc="w", alpha=.5)


def test_tick_padding_tightbbox():
    """Test that tick padding gets turned off if axis is off"""
    plt.rcParams["xtick.direction"] = "out"
    plt.rcParams["ytick.direction"] = "out"
    fig, ax = plt.subplots()
    bb = ax.get_tightbbox(fig.canvas.get_renderer())
    ax.axis('off')
    bb2 = ax.get_tightbbox(fig.canvas.get_renderer())
    assert bb.x0 < bb2.x0
    assert bb.y0 < bb2.y0


def test_inset():
    """
    Ensure that inset_ax argument is indeed optional
    """
    dx, dy = 0.05, 0.05
    # generate 2 2d grids for the x & y bounds
    y, x = np.mgrid[slice(1, 5 + dy, dy),
                    slice(1, 5 + dx, dx)]
    z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

    fig, ax = plt.subplots()
    ax.pcolormesh(x, y, z[:-1, :-1])
    ax.set_aspect(1.)
    ax.apply_aspect()
    # we need to apply_aspect to make the drawing below work.

    xlim = [1.5, 2.15]
    ylim = [2, 2.5]

    rect = [xlim[0], ylim[0], xlim[1] - xlim[0], ylim[1] - ylim[0]]

    rec, connectors = ax.indicate_inset(bounds=rect)
    assert connectors is None
    fig.canvas.draw()
    xx = np.array([[1.5, 2.],
                   [2.15, 2.5]])
    assert np.all(rec.get_bbox().get_points() == xx)


def test_zoom_inset():
    dx, dy = 0.05, 0.05
    # generate 2 2d grids for the x & y bounds
    y, x = np.mgrid[slice(1, 5 + dy, dy),
                    slice(1, 5 + dx, dx)]
    z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

    fig, ax = plt.subplots()
    ax.pcolormesh(x, y, z[:-1, :-1])
    ax.set_aspect(1.)
    ax.apply_aspect()
    # we need to apply_aspect to make the drawing below work.

    # Make the inset_axes...  Position axes coordinates...
    axin1 = ax.inset_axes([0.7, 0.7, 0.35, 0.35])
    # redraw the data in the inset axes...
    axin1.pcolormesh(x, y, z[:-1, :-1])
    axin1.set_xlim([1.5, 2.15])
    axin1.set_ylim([2, 2.5])
    axin1.set_aspect(ax.get_aspect())

    rec, connectors = ax.indicate_inset_zoom(axin1)
    assert len(connectors) == 4
    fig.canvas.draw()
    xx = np.array([[1.5,  2.],
                   [2.15, 2.5]])
    assert np.all(rec.get_bbox().get_points() == xx)
    xx = np.array([[0.6325, 0.692308],
                   [0.8425, 0.907692]])
    np.testing.assert_allclose(
        axin1.get_position().get_points(), xx, rtol=1e-4)


@pytest.mark.parametrize('x_inverted', [False, True])
@pytest.mark.parametrize('y_inverted', [False, True])
def test_indicate_inset_inverted(x_inverted, y_inverted):
    """
    Test that the inset lines are correctly located with inverted data axes.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2)

    x = np.arange(10)
    ax1.plot(x, x, 'o')
    if x_inverted:
        ax1.invert_xaxis()
    if y_inverted:
        ax1.invert_yaxis()

    rect, bounds = ax1.indicate_inset([2, 2, 5, 4], ax2)
    lower_left, upper_left, lower_right, upper_right = bounds

    sign_x = -1 if x_inverted else 1
    sign_y = -1 if y_inverted else 1
    assert sign_x * (lower_right.xy2[0] - lower_left.xy2[0]) > 0
    assert sign_x * (upper_right.xy2[0] - upper_left.xy2[0]) > 0
    assert sign_y * (upper_left.xy2[1] - lower_left.xy2[1]) > 0
    assert sign_y * (upper_right.xy2[1] - lower_right.xy2[1]) > 0


def test_set_position():
    fig, ax = plt.subplots()
    ax.set_aspect(3.)
    ax.set_position([0.1, 0.1, 0.4, 0.4], which='both')
    assert np.allclose(ax.get_position().width, 0.1)
    ax.set_aspect(2.)
    ax.set_position([0.1, 0.1, 0.4, 0.4], which='original')
    assert np.allclose(ax.get_position().width, 0.15)
    ax.set_aspect(3.)
    ax.set_position([0.1, 0.1, 0.4, 0.4], which='active')
    assert np.allclose(ax.get_position().width, 0.1)


def test_spines_properbbox_after_zoom():
    fig, ax = plt.subplots()
    bb = ax.spines.bottom.get_window_extent(fig.canvas.get_renderer())
    # this is what zoom calls:
    ax._set_view_from_bbox((320, 320, 500, 500), 'in',
                           None, False, False)
    bb2 = ax.spines.bottom.get_window_extent(fig.canvas.get_renderer())
    np.testing.assert_allclose(bb.get_points(), bb2.get_points(), rtol=1e-6)


def test_gettightbbox_ignore_nan():
    fig, ax = plt.subplots()
    remove_ticks_and_titles(fig)
    ax.text(np.NaN, 1, 'Boo')
    renderer = fig.canvas.get_renderer()
    np.testing.assert_allclose(ax.get_tightbbox(renderer).width, 496)


def test_scatter_series_non_zero_index(pd):
    # create non-zero index
    ids = range(10, 18)
    x = pd.Series(np.random.uniform(size=8), index=ids)
    y = pd.Series(np.random.uniform(size=8), index=ids)
    c = pd.Series([1, 1, 1, 1, 1, 0, 0, 0], index=ids)
    plt.scatter(x, y, c)


def test_scatter_empty_data():
    # making sure this does not raise an exception
    plt.scatter([], [])
    plt.scatter([], [], s=[], c=[])


@image_comparison(['annotate_across_transforms.png'],
                  style='mpl20', remove_text=True)
def test_annotate_across_transforms():
    x = np.linspace(0, 10, 200)
    y = np.exp(-x) * np.sin(x)

    fig, ax = plt.subplots(figsize=(3.39, 3))
    ax.plot(x, y)
    axins = ax.inset_axes([0.4, 0.5, 0.3, 0.3])
    axins.set_aspect(0.2)
    axins.xaxis.set_visible(False)
    axins.yaxis.set_visible(False)
    ax.annotate("", xy=(x[150], y[150]), xycoords=ax.transData,
                xytext=(1, 0), textcoords=axins.transAxes,
                arrowprops=dict(arrowstyle="->"))


@image_comparison(['secondary_xy.png'], style='mpl20')
def test_secondary_xy():
    fig, axs = plt.subplots(1, 2, figsize=(10, 5), constrained_layout=True)

    def invert(x):
        with np.errstate(divide='ignore'):
            return 1 / x

    for nn, ax in enumerate(axs):
        ax.plot(np.arange(2, 11), np.arange(2, 11))
        if nn == 0:
            secax = ax.secondary_xaxis
        else:
            secax = ax.secondary_yaxis

        secax(0.2, functions=(invert, invert))
        secax(0.4, functions=(lambda x: 2 * x, lambda x: x / 2))
        secax(0.6, functions=(lambda x: x**2, lambda x: x**(1/2)))
        secax(0.8)


def test_secondary_fail():
    fig, ax = plt.subplots()
    ax.plot(np.arange(2, 11), np.arange(2, 11))
    with pytest.raises(ValueError):
        ax.secondary_xaxis(0.2, functions=(lambda x: 1 / x))
    with pytest.raises(ValueError):
        ax.secondary_xaxis('right')
    with pytest.raises(ValueError):
        ax.secondary_yaxis('bottom')


def test_secondary_resize():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(np.arange(2, 11), np.arange(2, 11))

    def invert(x):
        with np.errstate(divide='ignore'):
            return 1 / x

    ax.secondary_xaxis('top', functions=(invert, invert))
    fig.canvas.draw()
    fig.set_size_inches((7, 4))
    assert_allclose(ax.get_position().extents, [0.125, 0.1, 0.9, 0.9])


def test_secondary_minorloc():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(np.arange(2, 11), np.arange(2, 11))

    def invert(x):
        with np.errstate(divide='ignore'):
            return 1 / x

    secax = ax.secondary_xaxis('top', functions=(invert, invert))
    assert isinstance(secax._axis.get_minor_locator(),
                      mticker.NullLocator)
    secax.minorticks_on()
    assert isinstance(secax._axis.get_minor_locator(),
                      mticker.AutoMinorLocator)
    ax.set_xscale('log')
    plt.draw()
    assert isinstance(secax._axis.get_minor_locator(),
                      mticker.LogLocator)
    ax.set_xscale('linear')
    plt.draw()
    assert isinstance(secax._axis.get_minor_locator(),
                      mticker.NullLocator)


def test_secondary_formatter():
    fig, ax = plt.subplots()
    ax.set_xscale("log")
    secax = ax.secondary_xaxis("top")
    secax.xaxis.set_major_formatter(mticker.ScalarFormatter())
    fig.canvas.draw()
    assert isinstance(
        secax.xaxis.get_major_formatter(), mticker.ScalarFormatter)


def test_secondary_repr():
    fig, ax = plt.subplots()
    secax = ax.secondary_xaxis("top")
    assert repr(secax) == '<SecondaryAxis:>'


def color_boxes(fig, ax):
    """
    Helper for the tests below that test the extents of various axes elements
    """
    fig.canvas.draw()

    renderer = fig.canvas.get_renderer()
    bbaxis = []
    for nn, axx in enumerate([ax.xaxis, ax.yaxis]):
        bb = axx.get_tightbbox(renderer)
        if bb:
            axisr = plt.Rectangle(
                (bb.x0, bb.y0), width=bb.width, height=bb.height,
                linewidth=0.7, edgecolor='y', facecolor="none", transform=None,
                zorder=3)
            fig.add_artist(axisr)
        bbaxis += [bb]

    bbspines = []
    for nn, a in enumerate(['bottom', 'top', 'left', 'right']):
        bb = ax.spines[a].get_window_extent(renderer)
        spiner = plt.Rectangle(
            (bb.x0, bb.y0), width=bb.width, height=bb.height,
            linewidth=0.7, edgecolor="green", facecolor="none", transform=None,
            zorder=3)
        fig.add_artist(spiner)
        bbspines += [bb]

    bb = ax.get_window_extent()
    rect2 = plt.Rectangle(
        (bb.x0, bb.y0), width=bb.width, height=bb.height,
        linewidth=1.5, edgecolor="magenta", facecolor="none", transform=None,
        zorder=2)
    fig.add_artist(rect2)
    bbax = bb

    bb2 = ax.get_tightbbox(renderer)
    rect2 = plt.Rectangle(
        (bb2.x0, bb2.y0), width=bb2.width, height=bb2.height,
        linewidth=3, edgecolor="red", facecolor="none", transform=None,
        zorder=1)
    fig.add_artist(rect2)
    bbtb = bb2
    return bbaxis, bbspines, bbax, bbtb


def test_normal_axes():
    with rc_context({'_internal.classic_mode': False}):
        fig, ax = plt.subplots(dpi=200, figsize=(6, 6))
        fig.canvas.draw()
        plt.close(fig)
        bbaxis, bbspines, bbax, bbtb = color_boxes(fig, ax)

    # test the axis bboxes
    target = [
        [123.375, 75.88888888888886, 983.25, 33.0],
        [85.51388888888889, 99.99999999999997, 53.375, 993.0]
    ]
    for nn, b in enumerate(bbaxis):
        targetbb = mtransforms.Bbox.from_bounds(*target[nn])
        assert_array_almost_equal(b.bounds, targetbb.bounds, decimal=2)

    target = [
        [150.0, 119.999, 930.0, 11.111],
        [150.0, 1080.0, 930.0, 0.0],
        [150.0, 119.9999, 11.111, 960.0],
        [1068.8888, 119.9999, 11.111, 960.0]
    ]
    for nn, b in enumerate(bbspines):
        targetbb = mtransforms.Bbox.from_bounds(*target[nn])
        assert_array_almost_equal(b.bounds, targetbb.bounds, decimal=2)

    target = [150.0, 119.99999999999997, 930.0, 960.0]
    targetbb = mtransforms.Bbox.from_bounds(*target)
    assert_array_almost_equal(bbax.bounds, targetbb.bounds, decimal=2)

    target = [85.5138, 75.88888, 1021.11, 1017.11]
    targetbb = mtransforms.Bbox.from_bounds(*target)
    assert_array_almost_equal(bbtb.bounds, targetbb.bounds, decimal=2)

    # test that get_position roundtrips to get_window_extent
    axbb = ax.get_position().transformed(fig.transFigure).bounds
    assert_array_almost_equal(axbb, ax.get_window_extent().bounds, decimal=2)


def test_nodecorator():
    with rc_context({'_internal.classic_mode': False}):
        fig, ax = plt.subplots(dpi=200, figsize=(6, 6))
        fig.canvas.draw()
        ax.set(xticklabels=[], yticklabels=[])
        bbaxis, bbspines, bbax, bbtb = color_boxes(fig, ax)

    # test the axis bboxes
    for nn, b in enumerate(bbaxis):
        assert b is None

    target = [
        [150.0, 119.999, 930.0, 11.111],
        [150.0, 1080.0, 930.0, 0.0],
        [150.0, 119.9999, 11.111, 960.0],
        [1068.8888, 119.9999, 11.111, 960.0]
    ]
    for nn, b in enumerate(bbspines):
        targetbb = mtransforms.Bbox.from_bounds(*target[nn])
        assert_allclose(b.bounds, targetbb.bounds, atol=1e-2)

    target = [150.0, 119.99999999999997, 930.0, 960.0]
    targetbb = mtransforms.Bbox.from_bounds(*target)
    assert_allclose(bbax.bounds, targetbb.bounds, atol=1e-2)

    target = [150., 120., 930., 960.]
    targetbb = mtransforms.Bbox.from_bounds(*target)
    assert_allclose(bbtb.bounds, targetbb.bounds, atol=1e-2)


def test_displaced_spine():
    with rc_context({'_internal.classic_mode': False}):
        fig, ax = plt.subplots(dpi=200, figsize=(6, 6))
        ax.set(xticklabels=[], yticklabels=[])
        ax.spines.bottom.set_position(('axes', -0.1))
        fig.canvas.draw()
        bbaxis, bbspines, bbax, bbtb = color_boxes(fig, ax)

    targets = [
        [150., 24., 930., 11.111111],
        [150.0, 1080.0, 930.0, 0.0],
        [150.0, 119.9999, 11.111, 960.0],
        [1068.8888, 119.9999, 11.111, 960.0]
    ]
    for target, bbspine in zip(targets, bbspines):
        targetbb = mtransforms.Bbox.from_bounds(*target)
        assert_allclose(bbspine.bounds, targetbb.bounds, atol=1e-2)

    target = [150.0, 119.99999999999997, 930.0, 960.0]
    targetbb = mtransforms.Bbox.from_bounds(*target)
    assert_allclose(bbax.bounds, targetbb.bounds, atol=1e-2)

    target = [150., 24., 930., 1056.]
    targetbb = mtransforms.Bbox.from_bounds(*target)
    assert_allclose(bbtb.bounds, targetbb.bounds, atol=1e-2)


def test_tickdirs():
    """
    Switch the tickdirs and make sure the bboxes switch with them
    """
    targets = [[[150.0, 120.0, 930.0, 11.1111],
                [150.0, 120.0, 11.111, 960.0]],
               [[150.0, 108.8889, 930.0, 11.111111111111114],
                [138.889, 120, 11.111, 960.0]],
               [[150.0, 114.44444444444441, 930.0, 11.111111111111114],
                [144.44444444444446, 119.999, 11.111, 960.0]]]
    for dnum, dirs in enumerate(['in', 'out', 'inout']):
        with rc_context({'_internal.classic_mode': False}):
            fig, ax = plt.subplots(dpi=200, figsize=(6, 6))
            ax.tick_params(direction=dirs)
            fig.canvas.draw()
            bbaxis, bbspines, bbax, bbtb = color_boxes(fig, ax)
            for nn, num in enumerate([0, 2]):
                targetbb = mtransforms.Bbox.from_bounds(*targets[dnum][nn])
                assert_allclose(
                    bbspines[num].bounds, targetbb.bounds, atol=1e-2)


def test_minor_accountedfor():
    with rc_context({'_internal.classic_mode': False}):
        fig, ax = plt.subplots(dpi=200, figsize=(6, 6))
        fig.canvas.draw()
        ax.tick_params(which='both', direction='out')

        bbaxis, bbspines, bbax, bbtb = color_boxes(fig, ax)
        bbaxis, bbspines, bbax, bbtb = color_boxes(fig, ax)
        targets = [[150.0, 108.88888888888886, 930.0, 11.111111111111114],
                   [138.8889, 119.9999, 11.1111, 960.0]]
        for n in range(2):
            targetbb = mtransforms.Bbox.from_bounds(*targets[n])
            assert_allclose(
                bbspines[n * 2].bounds, targetbb.bounds, atol=1e-2)

        fig, ax = plt.subplots(dpi=200, figsize=(6, 6))
        fig.canvas.draw()
        ax.tick_params(which='both', direction='out')
        ax.minorticks_on()
        ax.tick_params(axis='both', which='minor', length=30)
        fig.canvas.draw()
        bbaxis, bbspines, bbax, bbtb = color_boxes(fig, ax)
        targets = [[150.0, 36.66666666666663, 930.0, 83.33333333333334],
                   [66.6667, 120.0, 83.3333, 960.0]]

        for n in range(2):
            targetbb = mtransforms.Bbox.from_bounds(*targets[n])
            assert_allclose(
                bbspines[n * 2].bounds, targetbb.bounds, atol=1e-2)


@check_figures_equal(extensions=["png"])
def test_axis_bool_arguments(fig_test, fig_ref):
    # Test if False and "off" give the same
    fig_test.add_subplot(211).axis(False)
    fig_ref.add_subplot(211).axis("off")
    # Test if True after False gives the same as "on"
    ax = fig_test.add_subplot(212)
    ax.axis(False)
    ax.axis(True)
    fig_ref.add_subplot(212).axis("on")


def test_axis_extent_arg():
    fig, ax = plt.subplots()
    xmin = 5
    xmax = 10
    ymin = 15
    ymax = 20
    extent = ax.axis([xmin, xmax, ymin, ymax])

    # test that the docstring is correct
    assert tuple(extent) == (xmin, xmax, ymin, ymax)

    # test that limits were set per the docstring
    assert (xmin, xmax) == ax.get_xlim()
    assert (ymin, ymax) == ax.get_ylim()


def test_axis_extent_arg2():
    # Same as test_axis_extent_arg, but with keyword arguments
    fig, ax = plt.subplots()
    xmin = 5
    xmax = 10
    ymin = 15
    ymax = 20
    extent = ax.axis(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)

    # test that the docstring is correct
    assert tuple(extent) == (xmin, xmax, ymin, ymax)

    # test that limits were set per the docstring
    assert (xmin, xmax) == ax.get_xlim()
    assert (ymin, ymax) == ax.get_ylim()


def test_datetime_masked():
    # make sure that all-masked data falls back to the viewlim
    # set in convert.axisinfo....
    x = np.array([datetime.datetime(2017, 1, n) for n in range(1, 6)])
    y = np.array([1, 2, 3, 4, 5])
    m = np.ma.masked_greater(y, 0)

    fig, ax = plt.subplots()
    ax.plot(x, m)
    dt = mdates.date2num(np.datetime64('0000-12-31'))
    assert ax.get_xlim() == (730120.0 + dt, 733773.0 + dt)


def test_hist_auto_bins():
    _, bins, _ = plt.hist([[1, 2, 3], [3, 4, 5, 6]], bins='auto')
    assert bins[0] <= 1
    assert bins[-1] >= 6


def test_hist_nan_data():
    fig, (ax1, ax2) = plt.subplots(2)

    data = [1, 2, 3]
    nan_data = data + [np.nan]

    bins, edges, _ = ax1.hist(data)
    with np.errstate(invalid='ignore'):
        nanbins, nanedges, _ = ax2.hist(nan_data)

    np.testing.assert_allclose(bins, nanbins)
    np.testing.assert_allclose(edges, nanedges)


def test_hist_range_and_density():
    _, bins, _ = plt.hist(np.random.rand(10), "auto",
                          range=(0, 1), density=True)
    assert bins[0] == 0
    assert bins[-1] == 1


def test_bar_errbar_zorder():
    # Check that the zorder of errorbars is always greater than the bar they
    # are plotted on
    fig, ax = plt.subplots()
    x = [1, 2, 3]
    barcont = ax.bar(x=x, height=x, yerr=x, capsize=5, zorder=3)

    data_line, caplines, barlinecols = barcont.errorbar.lines
    for bar in barcont.patches:
        for capline in caplines:
            assert capline.zorder > bar.zorder
        for barlinecol in barlinecols:
            assert barlinecol.zorder > bar.zorder


def test_set_ticks_inverted():
    fig, ax = plt.subplots()
    ax.invert_xaxis()
    ax.set_xticks([.3, .7])
    assert ax.get_xlim() == (1, 0)


def test_aspect_nonlinear_adjustable_box():
    fig = plt.figure(figsize=(10, 10))  # Square.

    ax = fig.add_subplot()
    ax.plot([.4, .6], [.4, .6])  # Set minpos to keep logit happy.
    ax.set(xscale="log", xlim=(1, 10),
           yscale="logit", ylim=(1/11, 1/1001),
           aspect=1, adjustable="box")
    ax.margins(0)
    pos = fig.transFigure.transform_bbox(ax.get_position())
    assert pos.height / pos.width == pytest.approx(2)


def test_aspect_nonlinear_adjustable_datalim():
    fig = plt.figure(figsize=(10, 10))  # Square.

    ax = fig.add_axes([.1, .1, .8, .8])  # Square.
    ax.plot([.4, .6], [.4, .6])  # Set minpos to keep logit happy.
    ax.set(xscale="log", xlim=(1, 100),
           yscale="logit", ylim=(1 / 101, 1 / 11),
           aspect=1, adjustable="datalim")
    ax.margins(0)
    ax.apply_aspect()

    assert ax.get_xlim() == pytest.approx([1*10**(1/2), 100/10**(1/2)])
    assert ax.get_ylim() == (1 / 101, 1 / 11)


def test_box_aspect():
    # Test if axes with box_aspect=1 has same dimensions
    # as axes with aspect equal and adjustable="box"

    fig1, ax1 = plt.subplots()
    axtwin = ax1.twinx()
    axtwin.plot([12, 344])

    ax1.set_box_aspect(1)

    fig2, ax2 = plt.subplots()
    ax2.margins(0)
    ax2.plot([0, 2], [6, 8])
    ax2.set_aspect("equal", adjustable="box")

    fig1.canvas.draw()
    fig2.canvas.draw()

    bb1 = ax1.get_position()
    bbt = axtwin.get_position()
    bb2 = ax2.get_position()

    assert_array_equal(bb1.extents, bb2.extents)
    assert_array_equal(bbt.extents, bb2.extents)


def test_box_aspect_custom_position():
    # Test if axes with custom position and box_aspect
    # behaves the same independent of the order of setting those.

    fig1, ax1 = plt.subplots()
    ax1.set_position([0.1, 0.1, 0.9, 0.2])
    fig1.canvas.draw()
    ax1.set_box_aspect(1.)

    fig2, ax2 = plt.subplots()
    ax2.set_box_aspect(1.)
    fig2.canvas.draw()
    ax2.set_position([0.1, 0.1, 0.9, 0.2])

    fig1.canvas.draw()
    fig2.canvas.draw()

    bb1 = ax1.get_position()
    bb2 = ax2.get_position()

    assert_array_equal(bb1.extents, bb2.extents)


def test_bbox_aspect_axes_init():
    # Test that box_aspect can be given to axes init and produces
    # all equal square axes.
    fig, axs = plt.subplots(2, 3, subplot_kw=dict(box_aspect=1),
                            constrained_layout=True)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    sizes = []
    for ax in axs.flat:
        bb = ax.get_window_extent(renderer)
        sizes.extend([bb.width, bb.height])

    assert_allclose(sizes, sizes[0])


def test_redraw_in_frame():
    fig, ax = plt.subplots(1, 1)
    ax.plot([1, 2, 3])
    fig.canvas.draw()
    ax.redraw_in_frame()


def test_invisible_axes():
    # invisible axes should not respond to events...
    fig, ax = plt.subplots()
    assert fig.canvas.inaxes((200, 200)) is not None
    ax.set_visible(False)
    assert fig.canvas.inaxes((200, 200)) is None


def test_xtickcolor_is_not_markercolor():
    plt.rcParams['lines.markeredgecolor'] = 'white'
    ax = plt.axes()
    ticks = ax.xaxis.get_major_ticks()
    for tick in ticks:
        assert tick.tick1line.get_markeredgecolor() != 'white'


def test_ytickcolor_is_not_markercolor():
    plt.rcParams['lines.markeredgecolor'] = 'white'
    ax = plt.axes()
    ticks = ax.yaxis.get_major_ticks()
    for tick in ticks:
        assert tick.tick1line.get_markeredgecolor() != 'white'


@pytest.mark.parametrize('axis', ('x', 'y'))
@pytest.mark.parametrize('auto', (True, False, None))
def test_unautoscale(axis, auto):
    fig, ax = plt.subplots()
    x = np.arange(100)
    y = np.linspace(-.1, .1, 100)
    ax.scatter(y, x)

    get_autoscale_on = getattr(ax, f'get_autoscale{axis}_on')
    set_lim = getattr(ax, f'set_{axis}lim')
    get_lim = getattr(ax, f'get_{axis}lim')

    post_auto = get_autoscale_on() if auto is None else auto

    set_lim((-0.5, 0.5), auto=auto)
    assert post_auto == get_autoscale_on()
    fig.canvas.draw()
    assert_array_equal(get_lim(), (-0.5, 0.5))


@check_figures_equal(extensions=["png"])
def test_polar_interpolation_steps_variable_r(fig_test, fig_ref):
    l, = fig_test.add_subplot(projection="polar").plot([0, np.pi/2], [1, 2])
    l.get_path()._interpolation_steps = 100
    fig_ref.add_subplot(projection="polar").plot(
        np.linspace(0, np.pi/2, 101), np.linspace(1, 2, 101))


@mpl.style.context('default')
def test_autoscale_tiny_sticky():
    fig, ax = plt.subplots()
    ax.bar(0, 1e-9)
    fig.canvas.draw()
    assert ax.get_ylim() == (0, 1.05e-9)


def test_xtickcolor_is_not_xticklabelcolor():
    plt.rcParams['xtick.color'] = 'yellow'
    plt.rcParams['xtick.labelcolor'] = 'blue'
    ax = plt.axes()
    ticks = ax.xaxis.get_major_ticks()
    for tick in ticks:
        assert tick.tick1line.get_color() == 'yellow'
        assert tick.label1.get_color() == 'blue'


def test_ytickcolor_is_not_yticklabelcolor():
    plt.rcParams['ytick.color'] = 'yellow'
    plt.rcParams['ytick.labelcolor'] = 'blue'
    ax = plt.axes()
    ticks = ax.yaxis.get_major_ticks()
    for tick in ticks:
        assert tick.tick1line.get_color() == 'yellow'
        assert tick.label1.get_color() == 'blue'


@pytest.mark.parametrize('size', [size for size in mfont_manager.font_scalings
                                  if size is not None] + [8, 10, 12])
@mpl.style.context('default')
def test_relative_ticklabel_sizes(size):
    mpl.rcParams['xtick.labelsize'] = size
    mpl.rcParams['ytick.labelsize'] = size
    fig, ax = plt.subplots()
    fig.canvas.draw()

    for name, axis in zip(['x', 'y'], [ax.xaxis, ax.yaxis]):
        for tick in axis.get_major_ticks():
            assert tick.label1.get_size() == axis._get_tick_label_size(name)


def test_multiplot_autoscale():
    fig = plt.figure()
    ax1, ax2 = fig.subplots(2, 1, sharex='all')
    ax1.scatter([1, 2, 3, 4], [2, 3, 2, 3])
    ax2.axhspan(-5, 5)
    xlim = ax1.get_xlim()
    assert np.allclose(xlim, [0.5, 4.5])


def test_sharing_does_not_link_positions():
    fig = plt.figure()
    ax0 = fig.add_subplot(221)
    ax1 = fig.add_axes([.6, .6, .3, .3], sharex=ax0)
    init_pos = ax1.get_position()
    fig.subplots_adjust(left=0)
    assert (ax1.get_position().get_points() == init_pos.get_points()).all()


@check_figures_equal(extensions=["pdf"])
def test_2dcolor_plot(fig_test, fig_ref):
    color = np.array([0.1, 0.2, 0.3])
    # plot with 1D-color:
    axs = fig_test.subplots(5)
    axs[0].plot([1, 2], [1, 2], c=color.reshape(-1))
    axs[1].scatter([1, 2], [1, 2], c=color.reshape(-1))
    axs[2].step([1, 2], [1, 2], c=color.reshape(-1))
    axs[3].hist(np.arange(10), color=color.reshape(-1))
    axs[4].bar(np.arange(10), np.arange(10), color=color.reshape(-1))
    # plot with 2D-color:
    axs = fig_ref.subplots(5)
    axs[0].plot([1, 2], [1, 2], c=color.reshape((1, -1)))
    axs[1].scatter([1, 2], [1, 2], c=color.reshape((1, -1)))
    axs[2].step([1, 2], [1, 2], c=color.reshape((1, -1)))
    axs[3].hist(np.arange(10), color=color.reshape((1, -1)))
    axs[4].bar(np.arange(10), np.arange(10), color=color.reshape((1, -1)))


@check_figures_equal(extensions=['png'])
def test_shared_axes_clear(fig_test, fig_ref):
    x = np.arange(0.0, 2*np.pi, 0.01)
    y = np.sin(x)

    axs = fig_ref.subplots(2, 2, sharex=True, sharey=True)
    for ax in axs.flat:
        ax.plot(x, y)

    axs = fig_test.subplots(2, 2, sharex=True, sharey=True)
    for ax in axs.flat:
        ax.clear()
        ax.plot(x, y)


def test_shared_axes_retick():
    fig, axs = plt.subplots(2, 2, sharex='all', sharey='all')

    for ax in axs.flat:
        ax.plot([0, 2], 'o-')

    axs[0, 0].set_xticks([-0.5, 0, 1, 1.5])  # should affect all axes xlims
    for ax in axs.flat:
        assert ax.get_xlim() == axs[0, 0].get_xlim()

    axs[0, 0].set_yticks([-0.5, 0, 2, 2.5])  # should affect all axes ylims
    for ax in axs.flat:
        assert ax.get_ylim() == axs[0, 0].get_ylim()


@pytest.mark.parametrize('ha', ['left', 'center', 'right'])
def test_ylabel_ha_with_position(ha):
    fig = Figure()
    ax = fig.subplots()
    ax.set_ylabel("test", y=1, ha=ha)
    ax.yaxis.set_label_position("right")
    assert ax.yaxis.get_label().get_ha() == ha


def test_bar_label_location_vertical():
    ax = plt.gca()
    xs, heights = [1, 2], [3, -4]
    rects = ax.bar(xs, heights)
    labels = ax.bar_label(rects)
    assert labels[0].xy == (xs[0], heights[0])
    assert labels[0].get_ha() == 'center'
    assert labels[0].get_va() == 'bottom'
    assert labels[1].xy == (xs[1], heights[1])
    assert labels[1].get_ha() == 'center'
    assert labels[1].get_va() == 'top'


def test_bar_label_location_horizontal():
    ax = plt.gca()
    ys, widths = [1, 2], [3, -4]
    rects = ax.barh(ys, widths)
    labels = ax.bar_label(rects)
    assert labels[0].xy == (widths[0], ys[0])
    assert labels[0].get_ha() == 'left'
    assert labels[0].get_va() == 'center'
    assert labels[1].xy == (widths[1], ys[1])
    assert labels[1].get_ha() == 'right'
    assert labels[1].get_va() == 'center'


def test_bar_label_location_center():
    ax = plt.gca()
    ys, widths = [1, 2], [3, -4]
    rects = ax.barh(ys, widths)
    labels = ax.bar_label(rects, label_type='center')
    assert labels[0].xy == (widths[0] / 2, ys[0])
    assert labels[0].get_ha() == 'center'
    assert labels[0].get_va() == 'center'
    assert labels[1].xy == (widths[1] / 2, ys[1])
    assert labels[1].get_ha() == 'center'
    assert labels[1].get_va() == 'center'


def test_bar_label_location_errorbars():
    ax = plt.gca()
    xs, heights = [1, 2], [3, -4]
    rects = ax.bar(xs, heights, yerr=1)
    labels = ax.bar_label(rects)
    assert labels[0].xy == (xs[0], heights[0] + 1)
    assert labels[0].get_ha() == 'center'
    assert labels[0].get_va() == 'bottom'
    assert labels[1].xy == (xs[1], heights[1] - 1)
    assert labels[1].get_ha() == 'center'
    assert labels[1].get_va() == 'top'


def test_bar_label_fmt():
    ax = plt.gca()
    rects = ax.bar([1, 2], [3, -4])
    labels = ax.bar_label(rects, fmt='%.2f')
    assert labels[0].get_text() == '3.00'
    assert labels[1].get_text() == '-4.00'


def test_bar_label_labels():
    ax = plt.gca()
    rects = ax.bar([1, 2], [3, -4])
    labels = ax.bar_label(rects, labels=['A', 'B'])
    assert labels[0].get_text() == 'A'
    assert labels[1].get_text() == 'B'


def test_bar_label_nan_ydata():
    ax = plt.gca()
    bars = ax.bar([2, 3], [np.nan, 1])
    labels = ax.bar_label(bars)
    assert [l.get_text() for l in labels] == ['', '1']
    assert labels[0].xy == (2, 0)
    assert labels[0].get_va() == 'bottom'


def test_patch_bounds():  # PR 19078
    fig, ax = plt.subplots()
    ax.add_patch(mpatches.Wedge((0, -1), 1.05, 60, 120, 0.1))
    bot = 1.9*np.sin(15*np.pi/180)**2
    np.testing.assert_array_almost_equal_nulp(
        np.array((-0.525, -(bot+0.05), 1.05, bot+0.1)), ax.dataLim.bounds, 16)


@mpl.style.context('default')
def test_warn_ignored_scatter_kwargs():
    with pytest.warns(UserWarning,
                      match=r"You passed a edgecolor/edgecolors"):

        c = plt.scatter(
            [0], [0], marker="+", s=500, facecolor="r", edgecolor="b"
        )


def test_artist_sublists():
    fig, ax = plt.subplots()
    lines = [ax.plot(np.arange(i, i + 5))[0] for i in range(6)]
    col = ax.scatter(np.arange(5), np.arange(5))
    im = ax.imshow(np.zeros((5, 5)))
    patch = ax.add_patch(mpatches.Rectangle((0, 0), 5, 5))
    text = ax.text(0, 0, 'foo')

    # Get items, which should not be mixed.
    assert list(ax.collections) == [col]
    assert list(ax.images) == [im]
    assert list(ax.lines) == lines
    assert list(ax.patches) == [patch]
    assert not ax.tables
    assert list(ax.texts) == [text]

    # Get items should work like lists/tuple.
    assert ax.lines[0] is lines[0]
    assert ax.lines[-1] is lines[-1]
    with pytest.raises(IndexError, match='out of range'):
        ax.lines[len(lines) + 1]

    # Deleting items (multiple or single) should warn.
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.lines property'):
        del ax.lines[-1]
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.lines property'):
        del ax.lines[-1:]
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.lines property'):
        del ax.lines[1:]
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.lines property'):
        del ax.lines[0]

    # Lists should be empty after removing items.
    col.remove()
    assert not ax.collections
    im.remove()
    assert not ax.images
    patch.remove()
    assert not ax.patches
    text.remove()
    assert not ax.texts

    # Everything else should remain empty.
    assert not ax.lines
    assert not ax.tables

    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.texts property'):
        ax.texts.append(text)
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.collections property'):
        ax.collections.append(col)
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.images property'):
        ax.images.append(im)
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.patches property'):
        ax.patches.append(patch)
    # verify things are back
    assert list(ax.collections) == [col]
    assert list(ax.images) == [im]
    assert list(ax.patches) == [patch]
    assert list(ax.texts) == [text]

    # Adding items should warn.
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.lines property'):
        ax.lines.append(lines[-2])
    assert list(ax.lines) == [lines[-2]]
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.lines property'):
        ax.lines.append(lines[-1])
    assert list(ax.lines) == lines[-2:]
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.lines property'):
        ax.lines.insert(-2, lines[0])
    assert list(ax.lines) == [lines[0], lines[-2], lines[-1]]

    # Modifying items should warn.
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.lines property'):
        ax.lines[0] = lines[0]
    assert list(ax.lines) == [lines[0], lines[-2], lines[-1]]
    with pytest.warns(MatplotlibDeprecationWarning,
                      match='modification of the Axes.lines property'):
        ax.lines[1:1] = lines[1:-2]
    assert list(ax.lines) == lines

    # Adding to other lists should produce a regular list.
    assert ax.lines + [1, 2, 3] == [*lines, 1, 2, 3]
    assert [1, 2, 3] + ax.lines == [1, 2, 3, *lines]


def test_empty_line_plots():
    # Incompatible nr columns, plot "nothing"
    x = np.ones(10)
    y = np.ones((10, 0))
    _, ax = plt.subplots()
    line = ax.plot(x, y)
    assert len(line) == 0

    # Ensure plot([],[]) creates line
    _, ax = plt.subplots()
    line = ax.plot([], [])
    assert len(line) == 1


def test_clim():
    ax = plt.figure().add_subplot()
    for plot_method in [ax.imshow, ax.pcolor, ax.pcolormesh, ax.pcolorfast]:
        clim = (7, 8)
        norm = plot_method([[0, 1], [2, 3]], clim=clim).norm
        assert (norm.vmin, norm.vmax) == clim
