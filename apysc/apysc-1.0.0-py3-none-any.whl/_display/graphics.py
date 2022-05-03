"""Implementations for Graphics class.
"""

from typing import List
from typing import Optional
from typing import Union

from apysc._display import circle as _circle
from apysc._display import ellipse as _ellipse
from apysc._display import line as _line
from apysc._display import path as _path
from apysc._display import polygon as _polyg
from apysc._display import polyline as _polyline
from apysc._display import sprite
from apysc._display.begin_fill_interface import BeginFillInterface
from apysc._display.child_interface import ChildInterface
from apysc._display.display_object import DisplayObject
from apysc._display.graphics_clear_interface import GraphicsClearInterface
from apysc._display.line_style_interface import LineStyleInterface
from apysc._display.rectangle import Rectangle
from apysc._geom.path_data_base import PathDataBase
from apysc._geom.point2d import Point2D
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._type.variable_name_interface import VariableNameInterface


class Graphics(
        DisplayObject,
        BeginFillInterface, LineStyleInterface, VariableNameInterface,
        GraphicsClearInterface, ChildInterface):
    """
    Create an object that has each vector graphics interface.

    References
    ----------
    - Graphics document
        - https://simon-ritchie.github.io/apysc/graphics.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50)
    >>> rectangle.x
    Int(50)

    >>> circle: ap.Circle = sprite.graphics.draw_circle(
    ...     x=100, y=100, radius=50)
    >>> circle.x
    Int(100)
    """

    _current_line: Optional['_polyline.Polyline'] = None

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def __init__(
            self, *, parent: 'sprite.Sprite',
            variable_name: Optional[str] = None) -> None:
        """
        Create an object that has each vector graphics interface.

        Parameters
        ----------
        parent : Sprite
            A parent instance.
        variable_name : str or None, default None
            Variable name to set. Specified only when
            a subclass instantiation.

        References
        ----------
        - Graphics document
            - https://simon-ritchie.github.io/apysc/graphics.html
        """
        import apysc as ap
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._validation import display_validation

        display_validation.validate_sprite(sprite=parent)
        self.parent_sprite: ap.Sprite = parent
        if variable_name is None:
            variable_name = expression_variables_util.\
                get_next_variable_name(type_name=var_names.GRAPHICS)
        super(Graphics, self).__init__(variable_name=variable_name)
        self._fill_color = ap.String('')
        self._fill_alpha = ap.Number(1.0)
        self._line_color = ap.String('')
        self._line_alpha = ap.Number(1.0)
        self._line_thickness = ap.Int(1.0)
        self._children = ap.Array([])
        self._append_constructor_expression()
        self.parent_sprite.add_child(self)
        self._set_overflow_visible_setting()

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        import apysc as ap
        stage_name: str = self.parent_sprite.stage.variable_name
        expression: str = (
            f'var {self.variable_name} = {stage_name}.nested();'
        )
        ap.append_js_expression(expression=expression)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_rect(
            self, x: Union[int, Int],
            y: Union[int, Int],
            width: Union[int, Int],
            height: Union[int, Int]) -> Rectangle:
        """
        Draw a rectangle vector graphics.

        Parameters
        ----------
        x : Int or int
            X position to start drawing.
        y : Int or int
            Y position to start drawing.
        width : Int or int
            Rectangle width.
        height : Int or int
            Rectangle height.

        Returns
        -------
        rectangle : Rectangle
            Created rectangle.

        References
        ----------
        - Graphics draw_rect interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_rect.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> rectangle.x
        Int(50)

        >>> rectangle.width
        Int(50)

        >>> rectangle.fill_color
        String('#00aaff')
        """
        rectangle: Rectangle = Rectangle(
            parent=self, x=x, y=y, width=width, height=height)
        self.add_child(child=rectangle)
        return rectangle

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_round_rect(
            self, x: Union[int, Int],
            y: Union[int, Int],
            width: Union[int, Int],
            height: Union[int, Int],
            ellipse_width: Union[int, Int],
            ellipse_height: Union[int, Int]) -> Rectangle:
        """
        Draw a rounded rectangle vector graphics.

        Parameters
        ----------
        x : Int or int
            X-coordinate to start drawing.
        y : Int or int
            Y-coordinate to start drawing.
        width : Int or int
            Rectangle width.
        height : Int or int
            Rectangle height.
        ellipse_width : Int or int
            Ellipse width of the rectangle corner.
        ellipse_height : Int or int
            Ellipse height of the rectangle corner.

        Returns
        -------
        rectangle : Rectangle
            Created rectangle.

        References
        ----------
        - Graphics draw_round_rect interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_round_rect.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> round_rect: ap.Rectangle = sprite.graphics.draw_round_rect(
        ...     x=50, y=50, width=50, height=50,
        ...     ellipse_width=10, ellipse_height=15)
        >>> round_rect.ellipse_width
        Int(10)

        >>> round_rect.ellipse_height
        Int(15)
        """
        import apysc as ap
        rectangle: Rectangle = Rectangle(
            parent=self, x=x, y=y, width=width, height=height)
        if isinstance(ellipse_width, int):
            ellipse_width = ap.Int(ellipse_width)
        if isinstance(ellipse_height, int):
            ellipse_height = ap.Int(ellipse_height)
        rectangle.ellipse_width = ellipse_width
        rectangle.ellipse_height = ellipse_height
        self.add_child(child=rectangle)
        return rectangle

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_circle(
            self,
            x: Union[int, Int],
            y: Union[int, Int],
            radius: Union[int, Int]) -> '_circle.Circle':
        """
        Draw a circle vector graphics.

        Parameters
        ----------
        x : Int or int
            X-coordinate of the circle center.
        y : Int or int
            Y-coordinate of the circle center.
        radius : Int or int
            Circle radius.

        Returns
        -------
        circle : Circle
            Created circle graphics instance.

        References
        ----------
        - Graphics draw_circle interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_circle.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> circle: ap.Circle = sprite.graphics.draw_circle(
        ...     x=100, y=100, radius=50)
        >>> circle.x
        Int(100)

        >>> circle.y
        Int(100)

        >>> circle.radius
        Int(50)

        >>> circle.fill_color
        String('#00aaff')
        """
        circle: _circle.Circle = _circle.Circle(
            parent=self, x=x, y=y, radius=radius)
        self.add_child(child=circle)
        return circle

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_ellipse(
            self,
            x: Union[int, Int],
            y: Union[int, Int],
            width: Union[int, Int],
            height: Union[int, Int]) -> '_ellipse.Ellipse':
        """
        Draw an ellipse vector graphic.

        Parameters
        ----------
        x : Int or int
            X-coordinate of the ellipse center.
        y : Int or int
            Y-coordinate of the ellipse center.
        width : Int or int
            Ellipse width.
        height : Int or int
            Ellipse height.

        Returns
        -------
        ellipse : Ellipse
            Created ellipse graphics instance.

        References
        ----------
        - Graphics draw_ellipse interface
            - https://simon-ritchie.github.io/apysc/graphics_draw_ellipse.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        ...     x=100, y=100, width=100, height=50)
        >>> ellipse.x
        Int(100)

        >>> ellipse.y
        Int(100)

        >>> ellipse.width
        Int(100)

        >>> ellipse.height
        Int(50)

        >>> ellipse.fill_color
        String('#00aaff')
        """
        ellipse: _ellipse.Ellipse = _ellipse.Ellipse(
            parent=self, x=x, y=y, width=width, height=height)
        self.add_child(child=ellipse)
        return ellipse

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def line_to(
            self, x: Union[int, Int],
            y: Union[int, Int]) -> '_polyline.Polyline':
        """
        Draw a line from previous point to specified point (initial
        point is x = 0, y = 0).

        Parameters
        ----------
        x : Int or int
            X destination point to draw a line.
        y : Int or int
            Y destination point to draw a line.

        Returns
        -------
        line : Polyline
            Line graphics instance.

        References
        ----------
        - Graphics move_to and line_to interfaces document
            - https://simon-ritchie.github.io/apysc/graphics_move_to_and_line_to.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=5)
        >>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
        >>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
        >>> line_3: ap.Polyline = sprite.graphics.line_to(x=50, y=150)
        >>> line_1 == line_2 == line_3
        True

        >>> line_1.line_color
        String('#ffffff')

        >>> line_1.line_thickness
        Int(5)
        """
        import apysc as ap
        if self._current_line is None:
            self._current_line = _polyline.Polyline(
                parent=self,
                points=ap.Array([Point2D(x=0, y=0), Point2D(x=x, y=y)]))
            self.add_child(self._current_line)
        else:
            self._current_line.append_line_point(x=x, y=y)
        return self._current_line

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def move_to(
            self,
            x: Union[int, Int],
            y: Union[int, Int]) -> '_polyline.Polyline':
        """
        Move a line position to a specified point.

        Parameters
        ----------
        x : Int or int
            X destination point to move.
        y : Int or int
            Y destination point to move.

        Returns
        -------
        line : Polyline
            Line graphics instance.

        References
        ----------
        - Graphics move_to and line_to interfaces document
            - https://simon-ritchie.github.io/apysc/graphics_move_to_and_line_to.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=5)
        >>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
        >>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
        >>> line_1 == line_2
        True

        >>> line_1.line_color
        String('#ffffff')

        >>> line_1.line_thickness
        Int(5)
        """
        import apysc as ap
        polyline: _polyline.Polyline = _polyline.Polyline(
            parent=self, points=ap.Array([Point2D(x=x, y=y)]))
        self._current_line = polyline
        return polyline

    def _reset_each_line_settings(self) -> None:
        """
        Reset each line settings (e.g., LineDotSetting, LineDashSetting,
        and so on).

        Notes
        -----
        This interface does not append an expression.
        """
        self._line_dot_setting = None
        self._line_dash_setting = None
        self._line_round_dot_setting = None
        self._line_dash_dot_setting = None

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_line(
            self,
            x_start: Union[int, Int],
            y_start: Union[int, Int],
            x_end: Union[int, Int],
            y_end: Union[int, Int]) -> '_line.Line':
        """
        Draw a normal line vector graphic.

        Notes
        -----
        - This interface ignores line settings, like
            the `LineDotSetting`, `LineDashSetting`.

        Parameters
        ----------
        x_start : Int or int
            Line start x-coordinate.
        y_start : Int or int
            Line start y-coordinate.
        x_end : Int or int
            Line end x-coordinate.
        y_end : Int or int
            Line end y-coordinate.

        Returns
        -------
        line : Line
            Created line graphics instance.

        References
        ----------
        - Graphics draw_line interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_line.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_color
        String('#ffffff')

        >>> line.line_thickness
        Int(5)
        """
        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        line: _line.Line = _line.Line(
            parent=self,
            start_point=Point2D(x=x_start, y=y_start),
            end_point=Point2D(x=x_end, y=y_end))
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        self.add_child(child=line)
        return line

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_dotted_line(
            self,
            x_start: Union[int, Int],
            y_start: Union[int, Int],
            x_end: Union[int, Int],
            y_end: Union[int, Int],
            dot_size: Union[int, Int]) -> '_line.Line':
        """
        Draw a dotted line vector graphics.

        Notes
        -----
        - This interface ignores line settings, like the
            `LineDashSetting`, except `LineDotSetting`.

        Parameters
        ----------
        x_start : Int or int
            Line start x-coordinate.
        y_start : Int or int
            Line start y-coordinate.
        x_end : Int or int
            Line end x-coordinate.
        y_end : Int or int
            Line end y-coordinate.
        dot_size : Int or int
            Dot size.

        Returns
        -------
        line : Line
            Created line graphics instance.

        References
        ----------
        - Graphics draw_dotted_line interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_dotted_line.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_dotted_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50, dot_size=5)
        >>> line.line_color
        String('#ffffff')

        >>> line.line_thickness
        Int(5)

        >>> line.line_dot_setting.dot_size
        Int(5)
        """
        import apysc as ap
        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_dot_setting = ap.LineDotSetting(dot_size=dot_size)
        line: _line.Line = _line.Line(
            parent=self,
            start_point=Point2D(x=x_start, y=y_start),
            end_point=Point2D(x=x_end, y=y_end))
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        self.add_child(child=line)
        return line

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_dashed_line(
            self,
            x_start: Union[int, Int],
            y_start: Union[int, Int],
            x_end: Union[int, Int],
            y_end: Union[int, Int],
            dash_size: Union[int, Int],
            space_size: Union[int, Int]) -> '_line.Line':
        """
        Draw a dashed line vector graphics.

        Notes
        -----
        - This interface ignores line settings, like
        the `LineDotSetting`, except `LineDashSetting`.

        Parameters
        ----------
        x_start : Int or int
            Line start x-coordinate.
        y_start : Int or int
            Line start y-coordinate.
        x_end : Int or int
            Line end x-coordinate.
        y_end : Int or int
            Line end y-coordinate.
        dash_size : Int or int
            Dash size.
        space_size : Int or int
            Blank space size between dashes.

        Returns
        -------
        line : Line
            Created line graphics instance.

        References
        ----------
        - Graphics draw_dashed_line interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_dashed_line.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_dashed_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50,
        ...     dash_size=5, space_size=2)
        >>> line.line_color
        String('#ffffff')

        >>> line.line_dash_setting.dash_size
        Int(5)

        >>> line.line_dash_setting.space_size
        Int(2)
        """
        import apysc as ap
        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_dash_setting = ap.LineDashSetting(
            dash_size=dash_size, space_size=space_size)
        line: _line.Line = _line.Line(
            parent=self,
            start_point=Point2D(x=x_start, y=y_start),
            end_point=Point2D(x=x_end, y=y_end))
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        self.add_child(child=line)
        return line

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_round_dotted_line(
            self,
            x_start: Union[int, Int],
            y_start: Union[int, Int],
            x_end: Union[int, Int],
            y_end: Union[int, Int],
            round_size: Union[int, Int],
            space_size: Union[int, Int]) -> '_line.Line':
        """
        Draw a round-dotted line vector graphics.

        Notes
        -----
        This interface ignores line settings, like the
        `LineDotSetting`, except `LineRoundDotSetting`.

        Parameters
        ----------
        x_start : Int or int
            Line start x-coordinate.
        y_start : Int or int
            Line start y-coordinate.
        x_end : Int or int
            Line end x-coordinate.
        y_end : Int or int
            Line end y-coordinate.
        round_size : Int or int
            Dot round size.
        space_size : Int or int
            Blank space size between dots.

        Returns
        -------
        line : Line
            Created line graphics instance.

        References
        ----------
        - Graphics draw_round_dotted_line interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_round_dotted_line.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_round_dotted_line(
        ...    x_start=50, y_start=50, x_end=150, y_end=50,
        ...    round_size=6, space_size=3)
        >>> line.line_color
        String('#ffffff')

        >>> line.line_round_dot_setting.round_size
        Int(6)

        >>> line.line_round_dot_setting.space_size
        Int(3)
        """
        import apysc as ap
        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_round_dot_setting = ap.LineRoundDotSetting(
            round_size=round_size, space_size=space_size)
        line: _line.Line = _line.Line(
            parent=self,
            start_point=Point2D(x=x_start, y=y_start),
            end_point=Point2D(x=x_end, y=y_end))
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        self.add_child(child=line)
        return line

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_dash_dotted_line(
            self,
            x_start: Union[int, Int],
            y_start: Union[int, Int],
            x_end: Union[int, Int],
            y_end: Union[int, Int],
            dot_size: Union[int, Int],
            dash_size: Union[int, Int],
            space_size: Union[int, Int]) -> '_line.Line':
        """
        Draw a dash-dotted (1-dot chain) line vector graphics.

        Parameters
        ----------
        x_start : Int or int
            Line start x-coordinate.
        y_start : Int or int
            Line start y-coordinate.
        x_end : Int or int
            Line end x-coordinate.
        y_end : Int or int
            Line end y-coordinate.
        dot_size : Int or int
            Dot size.
        dash_size : Int or int
            Dash size.
        space_size : Int or int
            Blank space size between dots and dashes.

        Returns
        -------
        line : Line
            Created line graphics instance.

        References
        ----------
        - Graphics draw_dash_dotted_line interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_dash_dotted_line.html # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_dash_dotted_line(
        ...    x_start=50, y_start=50, x_end=150, y_end=50,
        ...    dot_size=2, dash_size=5, space_size=3)
        >>> line.line_color
        String('#ffffff')

        >>> line.line_dash_dot_setting.dot_size
        Int(2)

        >>> line.line_dash_dot_setting.dash_size
        Int(5)

        >>> line.line_dash_dot_setting.space_size
        Int(3)
        """
        import apysc as ap
        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_dash_dot_setting = ap.LineDashDotSetting(
            dot_size=dot_size,
            dash_size=dash_size,
            space_size=space_size)
        line: _line.Line = _line.Line(
            parent=self,
            start_point=Point2D(x=x_start, y=y_start),
            end_point=Point2D(x=x_end, y=y_end))
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        self.add_child(child=line)
        return line

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_polygon(
            self,
            points: Union[List[Point2D], Array[Point2D]]) -> '_polyg.Polygon':
        """
        Draw a polygon vector graphic. This interface is similar
        to the Polyline class (created by `move_to` or `line_to`).
        But unlike that, this interface connects the last point
        and the start point.

        Parameters
        ----------
        points : list of Point2D or Array.
            Polygon vertex points.

        Returns
        -------
        polygon : Polygon
            Created polygon graphics instance.

        References
        ----------
        - Graphics draw_polygon interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_polygon.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=25, y=0),
        ...         ap.Point2D(x=0, y=50),
        ...         ap.Point2D(x=50, y=50),
        ...     ])
        >>> polygon.fill_color
        String('#00aaff')
        """
        import apysc as ap
        if isinstance(points, list):
            points = ap.Array(points)
        polygon: _polyg.Polygon = _polyg.Polygon(
            parent=self, points=points)
        self.add_child(polygon)
        return polygon

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Graphics')
    def draw_path(
            self, path_data_list: List[PathDataBase]) -> '_path.Path':
        """
        Draw a path vector graphics.

        Parameters
        ----------
        path_data_list : list of PathDataBase
            Target path data settings, such as the ap.PathData.MoveTo.

        Returns
        -------
        path : Path
            Created path graphics instance.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=3)
        >>> path: ap.Path = sprite.graphics.draw_path(
        ...     path_data_list=[
        ...         ap.PathMoveTo(x=0, y=50),
        ...         ap.PathBezier2D(
        ...             control_x=50, control_y=0,
        ...             dest_x=100, dest_y=50),
        ...     ])
        """
        path: _path.Path = _path.Path(
            parent=self, path_data_list=path_data_list)
        self.add_child(path)
        return path

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Graphics('<variable_name>')`).
        """
        repr_str: str = f"Graphics('{self.variable_name}')"
        return repr_str
