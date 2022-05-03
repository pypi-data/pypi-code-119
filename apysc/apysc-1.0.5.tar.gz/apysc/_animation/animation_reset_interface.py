"""Class implementation for the animation_reset interface.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_interface import VariableNameInterface


class AnimationResetInterface(VariableNameInterface):

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='AnimationResetInterface')
    def animation_reset(self) -> None:
        """
        Stop all animations and reset.

        References
        ----------
        - animation_reset interface document
            - https://simon-ritchie.github.io/apysc/animation_reset.html

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        >>> def on_timer(
        ...         e: ap.TimerEvent,
        ...         options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options['rectangle']
        ...     rectangle.animation_reset()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.animation_x(
        ...     x=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        >>> options: RectOptions = {'rectangle': rectangle}
        >>> ap.Timer(on_timer, delay=750, options=options).start()
        """
        import apysc as ap
        expression: str = (
            f'{self.variable_name}.timeline().stop();'
        )
        ap.append_js_expression(expression=expression)
