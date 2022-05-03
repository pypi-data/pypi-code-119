"""Class implementation for mouse move interface.
"""

from typing import Callable
from typing import Dict
from typing import Optional
from typing import TypeVar

from apysc._event.handler import HandlerData
from apysc._event.mouse_event import MouseEvent
from apysc._event.mouse_event_interface_base import MouseEventInterfaceBase
from apysc._html.debug_mode import add_debug_info_setting

_O = TypeVar('_O')
_Handler = Callable[[MouseEvent, _O], None]


class MouseMoveInterface(MouseEventInterfaceBase):

    _mouse_move_handlers: Dict[str, HandlerData]

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='MouseMoveInterface')
    def mousemove(
            self, handler: _Handler[_O], *,
            options: Optional[_O] = None) -> str:
        """
        Add mouse move event listener setting.

        Parameters
        ----------
        handler : _Handler
            Callable that would be called when mousemove on this instance.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.

        Returns
        -------
        name : str
            Handler's name.

        References
        ----------
        - Mousemove interface document
            - https://simon-ritchie.github.io/apysc/mousemove.html
        - About the handler options' type document
            - https://simon-ritchie.github.io/apysc/about_handler_options_type.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousemove(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     stage_x: ap.Int = e.stage_x
        ...     ap.trace('stage_x:', stage_x)
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mousemove(on_mousemove)
        """
        import apysc as ap
        from apysc._event.handler import append_handler_expression
        from apysc._event.handler import get_handler_name
        from apysc._type.variable_name_interface import VariableNameInterface
        from apysc._validation.handler_options_validation import \
            validate_options_type
        from apysc._validation.variable_name_validation import \
            validate_variable_name_interface_type
        self_instance: VariableNameInterface = \
            validate_variable_name_interface_type(instance=self)
        validate_options_type(options=options)
        self._initialize_mouse_move_handlers_if_not_initialized()
        name: str = get_handler_name(handler=handler, instance=self)
        self._set_mouse_event_handler_data(
            handler=handler, handlers_dict=self._mouse_move_handlers,
            options=options)
        self._append_mouse_event_binding_expression(
            name=name, mouse_event_type=ap.MouseEventType.MOUSEMOVE)
        e: ap.MouseEvent = ap.MouseEvent(this=self_instance)
        append_handler_expression(
            handler_data=self._mouse_move_handlers[name],
            handler_name=name, e=e)
        return name

    def _initialize_mouse_move_handlers_if_not_initialized(self) -> None:
        """
        Initialize _mouse_move_handlers attribute if this
        interface does not initialize it yet.
        """
        if hasattr(self, '_mouse_move_handlers'):
            return
        self._mouse_move_handlers = {}

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='MouseMoveInterface')
    def unbind_mousemove(self, handler: _Handler[_O]) -> None:
        """
        Unbind a specified handler's mouse move event.

        Parameters
        ----------
        handler : _Handler
            Unbinding target Callable.

        References
        ----------
        - Mousemove interface document
            - https://simon-ritchie.github.io/apysc/mousemove.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousemove(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     stage_x: ap.Int = e.stage_x
        ...     ap.trace('stage_x:', stage_x)
        >>> def on_click(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.unbind_mousemove(on_mousemove)
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mousemove(on_mousemove)
        >>> _ = rectangle.click(on_click)
        """
        import apysc as ap
        self._initialize_mouse_move_handlers_if_not_initialized()
        self._unbind_mouse_event(
            handler=handler, mouse_event_type=ap.MouseEventType.MOUSEMOVE,
            handlers_dict=self._mouse_move_handlers)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='MouseMoveInterface')
    def unbind_mousemove_all(self) -> None:
        """
        Unbind all mouse move events.

        References
        ----------
        - Mousemove interface document
            - https://simon-ritchie.github.io/apysc/mousemove.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousemove(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     stage_x: ap.Int = e.stage_x
        ...     ap.trace('stage_x:', stage_x)
        >>> def on_click(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.unbind_mousemove_all()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mousemove(on_mousemove)
        >>> _ = rectangle.click(on_click)
        """
        import apysc as ap
        self._initialize_mouse_move_handlers_if_not_initialized()
        self._unbind_all_mouse_events(
            mouse_event_type=ap.MouseEventType.MOUSEMOVE,
            handlers_dict=self._mouse_move_handlers)
