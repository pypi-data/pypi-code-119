"""Class implementation for the width animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationWidth(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a width.

    References
    ----------
    - animation_width and animation_height interfaces document
        - https://simon-ritchie.github.io/apysc/animation_width_and_height.html  # noqa
    - Animation interfaces duration setting document
        - https://simon-ritchie.github.io/apysc/animation_duration.html
    - Animation interfaces delay setting document
        - https://simon-ritchie.github.io/apysc/animation_delay.html
    - Each animation interface return value document
        - https://simon-ritchie.github.io/apysc/animation_return_value.html  # noqa
    - Sequential animation setting document
        - https://simon-ritchie.github.io/apysc/sequential_animation.html
    - animation_parallel interface document
        - https://simon-ritchie.github.io/apysc/animation_parallel.html
    - Easing enum document
        - https://simon-ritchie.github.io/apysc/easing_enum.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50)
    >>> animation: ap.AnimationHeight = rectangle.animation_height(
    ...     height=100,
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _width: Int

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='AnimationWidth')
    def __init__(
            self,
            *,
            target: _T,
            width: Union[int, Int],
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a width.

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        width : Int or int
            The final width of the animation.
        duration : Int or int, default 3000
            Milliseconds before an animation ends.
        delay : Int or int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        variable_name: str = expression_variables_util.\
            get_next_variable_name(type_name=var_names.ANIMATION_WIDTH)
        self._width = to_apysc_val_from_builtin.\
            get_copied_int_from_builtin_val(integer=width)
        self._set_basic_animation_settings(
            target=target,
            duration=duration,
            delay=delay,
            easing=easing)
        super(AnimationWidth, self).__init__(variable_name=variable_name)

    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
        """
        from apysc._type import value_util
        width_str: str = value_util.get_value_str_for_expression(
            value=self._width)
        return f'\n  .width({width_str});'

    def _get_complete_event_in_handler_head_expression(self) -> str:
        """
        Get an expression to be inserted into the complete event
        handler's head.

        Returns
        -------
        expression : str
            An expression to insert into the complete event
            handler's head.
        """
        from apysc._display.width_interface import WidthInterface
        expression: str = ''
        if isinstance(self._target, WidthInterface):
            self._target._initialize_width_if_not_initialized()
            expression = (
                f'{self._target._width.variable_name} = '
                f'{self._width.variable_name};'
            )
        return expression
