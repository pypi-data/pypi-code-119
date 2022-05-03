"""Class implementation for the flip_y interface.
"""

from typing import Dict

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.boolean import Boolean
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class FlipYInterface(
        VariableNameInterface, RevertInterface, AttrLinkingInterface):

    _flip_y: Boolean

    def _initialize_flip_y_if_not_initialized(self) -> None:
        """
        Initialize the _flip_y attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, '_flip_y'):
            return
        self._flip_y = Boolean(False)

        self._append_flip_y_attr_linking_setting()

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='FlipYInterface')
    def _append_flip_y_attr_linking_setting(self) -> None:
        """
        Append a flip-y attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._flip_y, attr_name='flip_y')
        self._append_attr_to_linking_stack(
            attr=self._flip_y, attr_name='flip_y')

    @property  # type: ignore[misc]
    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='FlipYInterface')
    def flip_y(self) -> Boolean:
        """
        Get a boolean value whether the y-axis is flipping or not.

        Returns
        -------
        flip_y : Boolean
            A boolean value whether the y-axis is flipping or not.

        References
        ----------
        - GraphicsBase flip_x and flip_y interfaces document
            - https://simon-ritchie.github.io/apysc/graphics_base_flip_interfaces.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=0, y=0),
        ...         ap.Point2D(x=50, y=0),
        ...         ap.Point2D(x=25, y=50),
        ...     ])
        >>> polygon.flip_y = ap.Boolean(True)
        >>> polygon.flip_y
        Boolean(True)
        """
        from apysc._type import value_util
        self._initialize_flip_y_if_not_initialized()
        return value_util.get_copy(value=self._flip_y)

    @flip_y.setter
    def flip_y(self, value: Boolean) -> None:
        """
        Update a y-axis flipping value.

        Parameters
        ----------
        value : Boolean
            Flipping value. If true, a y-axis will be flipped,
            otherwise it will be reset.

        References
        ----------
        - GraphicsBase flip_x and flip_y interfaces document
            - https://simon-ritchie.github.io/apysc/graphics_base_flip_interfaces.html  # noqa
        """
        from apysc._html.debug_mode import DebugInfo
        with DebugInfo(
                callable_='flip_y', args=[], kwargs={},
                module_name=__name__,
                class_name=FlipYInterface.__name__):
            import apysc as ap
            self._initialize_flip_y_if_not_initialized()
            before_value: ap.Boolean = self._flip_y
            self._flip_y = value
            self._append_flip_y_update_expression(before_value=before_value)

            self._append_flip_y_attr_linking_setting()

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='FlipYInterface')
    def _append_flip_y_update_expression(
            self, *, before_value: Boolean) -> None:
        """
        Append a y-axis flipping value updating expression.

        Parameters
        ----------
        before_value : Boolean
            Before updating flipping value.
        """
        import apysc as ap
        from apysc._display import flip_interface_helper
        self._initialize_flip_y_if_not_initialized()
        expression: str = flip_interface_helper.\
            make_flip_update_expression(
                before_value=before_value, after_value=self._flip_y,
                axis=flip_interface_helper.Axis.Y,
                interface_variable_name=self.variable_name)
        ap.append_js_expression(expression=expression)

    _flip_y_snapshots: Dict[str, bool]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_flip_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_flip_y_snapshots',
            value=self._flip_y._value, snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._flip_y._value = self._flip_y_snapshots[snapshot_name]
