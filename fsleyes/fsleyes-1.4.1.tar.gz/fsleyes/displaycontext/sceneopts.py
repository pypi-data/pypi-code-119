#!/usr/bin/env python
#
# sceneopts.py - Provides the SceneOpts class.
#
# Author: Paul McCarthy <pauldmccarthy@gmail.com>
#
"""This module provides the :class:`.SceneOpts` class, which contains display
settings used by :class:`.CanvasPanel` instances.
"""


import copy
import logging

import fsleyes_props      as props
import fsleyes.gl         as fslgl
import fsleyes.colourmaps as fslcm

from . import canvasopts


log = logging.getLogger(__name__)


class SceneOpts(props.HasProperties):
    """The ``SceneOpts`` class defines settings which are used by
    :class:`.CanvasPanel` instances.

    Several of the properties of the ``SceneOpts`` class are defined in the
    :class:`.SliceCanvasOpts` class, so see its documentation for more
    details.
    """


    showCursor      = copy.copy(canvasopts.SliceCanvasOpts.showCursor)
    cursorWidth     = copy.copy(canvasopts.SliceCanvasOpts.cursorWidth)
    zoom            = copy.copy(canvasopts.SliceCanvasOpts.zoom)
    bgColour        = copy.copy(canvasopts.SliceCanvasOpts.bgColour)
    cursorColour    = copy.copy(canvasopts.SliceCanvasOpts.cursorColour)
    highDpi         = copy.copy(canvasopts.SliceCanvasOpts.highDpi)


    fgColour = props.Colour(default=(1, 1, 1))
    """Colour to use for foreground items (e.g. labels).

    .. note:: This colour is automatically updated whenever the
              :attr:`.bgColour` is changed. But it can be modified
              independently.
    """


    showColourBar = props.Boolean(default=False)
    """If ``True``, and it is possible to do so, a colour bar is shown on
    the scene.
    """


    colourBarLocation  = props.Choice(('top', 'bottom', 'left', 'right'))
    """This property controls the location of the colour bar, if it is being
    shown.
    """


    colourBarLabelSide = props.Choice(('top-left', 'bottom-right'))
    """This property controls the location of the colour bar labels, relative
    to the colour bar, if it is being shown.
    """


    colourBarSize = props.Percentage(default=100)
    """Size of the major axis of the colour bar, as a proportion of the
    available space.
    """


    labelSize = props.Int(minval=4, maxval=96, default=12, clamped=True)
    """Font size used for any labels drawn on the canvas, including
    orthographic labels, and colour bar labels.
    """


    movieSyncRefresh = props.Boolean(default=True)
    """Whether, when in movie mode, to synchronise the refresh for GL
    canvases. This is not possible in some platforms/environments. See
    :attr:`.CanvasPanel.movieSyncRefresh`.
    """


    def __init__(self, panel):
        """Create a ``SceneOpts`` instance. """

        self.__panel = panel
        self.__name  = '{}_{}'.format(type(self).__name__, id(self))

        self.movieSyncRefresh = self.defaultMovieSyncRefresh
        self.addListener('bgColour', self.__name, self.__onBgColourChange)


    @property
    def defaultMovieSyncRefresh(self):
        """In movie mode, the canvas refreshes are performed by the
        __syncMovieRefresh or __unsyncMovieRefresh methods of the CanvasPanel
        class. Some platforms/GL drivers/environments seem to have a problem
        with separate renders/buffer swaps, so we have to use a shitty
        unsynchronised update routine.

        These heuristics are not perfect - the movieSyncRefresh property can
        therefore be overridden by the user.
        """
        renderer        = fslgl.GL_RENDERER.lower()
        unsyncRenderers = ['gallium', 'mesa dri intel(r)']
        unsync          = any([r in renderer for r in unsyncRenderers])

        return not unsync


    @property
    def panel(self):
        """Return a reference to the ``CanvasPanel`` that owns this
        ``SceneOpts`` instance.
        """
        return self.__panel


    def __onBgColourChange(self, *a):
        """Called when the background colour changes. Updates the
        :attr:`fgColour` to a complementary colour.
        """
        self.fgColour = fslcm.complementaryColour(self.bgColour)
