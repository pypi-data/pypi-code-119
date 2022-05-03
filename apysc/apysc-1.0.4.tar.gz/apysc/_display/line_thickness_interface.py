"""Class implementation for line thickness interface.
"""

from typing import Dict
from typing import Union

from apysc._animation.animation_line_thickness_interface import \
    AnimationLineThicknessInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class LineThicknessInterface(
        AnimationLineThicknessInterface,
        RevertInterface,
        AttrLinkingInterface):

    _line_thickness: Int

    def _initialize_line_thickness_if_not_initialized(self) -> None:
        """
        Initialize _line_thickness attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, '_line_thickness'):
            return
        self._line_thickness = Int(1)

        self._append_line_thickness_attr_linking_setting()

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='LineThicknessInterface')
    def _append_line_thickness_attr_linking_setting(self) -> None:
        """
        Append a line thickness attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._line_thickness, attr_name='line_thickness')
        self._append_attr_to_linking_stack(
            attr=self._line_thickness, attr_name='line_thickness')

    @property  # type: ignore[misc]
    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='LineThicknessInterface')
    def line_thickness(self) -> Int:
        """
        Get this instance's line thickness.

        Returns
        -------
        line_thickness : Int
            Current line thickness.

        References
        ----------
        - Graphics line_thickness interface document
            - https://simon-ritchie.github.io/apysc/graphics_line_thickness.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color='#fff', thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_thickness
        Int(5)
        """
        from apysc._type import value_util
        return value_util.get_copy(value=self._line_thickness)

    @line_thickness.setter
    def line_thickness(self, value: Int) -> None:
        """
        Update this instance's line thickness.

        Parameters
        ----------
        value : Int
            Line thickness to set.

        References
        ----------
        - Graphics line_thickness interface document
            - https://simon-ritchie.github.io/apysc/graphics_line_thickness.html  # noqa
        """
        from apysc._html.debug_mode import DebugInfo
        with DebugInfo(
                callable_='line_thickness', args=[value],
                kwargs={}, module_name=__name__,
                class_name=LineThicknessInterface.__name__):
            self._update_line_thickness_and_skip_appending_exp(value=value)
            self._line_thickness.\
                _append_incremental_calc_substitution_expression()
            self._append_line_thickness_update_expression()

            self._append_line_thickness_attr_linking_setting()

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='LineThicknessInterface')
    def _append_line_thickness_update_expression(self) -> None:
        """
        Append line thickness update expression.
        """
        import apysc as ap
        from apysc._type import value_util
        line_thickness_str: str = value_util.get_value_str_for_expression(
            value=self.line_thickness)
        expression: str = (
            f'{self.variable_name}.attr({{"stroke-width": '
            f'{line_thickness_str}}});'
        )
        ap.append_js_expression(expression=expression)

    def _update_line_thickness_and_skip_appending_exp(
            self, *, value: Union[int, Int]) -> None:
        """
        Update line thickness and skip appending expression.

        Parameters
        ----------
        value : Int or int
            Line thickness to set.
        """
        import apysc as ap
        from apysc._validation import number_validation
        number_validation.validate_integer(integer=value)
        number_validation.validate_num_is_gte_zero(num=value)
        if isinstance(value, ap.Int):
            value_: ap.Int = value
        else:
            value_ = Int(value)
        self._line_thickness = value_

    _line_thickness_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_thickness_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_thickness_snapshots',
            value=self._line_thickness._value, snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._line_thickness._value = self._line_thickness_snapshots[
            snapshot_name]
