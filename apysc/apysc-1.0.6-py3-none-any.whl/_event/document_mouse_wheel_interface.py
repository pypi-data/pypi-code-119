"""Implementation of mouse wheel event interfaces.

Notes
-----
Not supported each SVG elements' mouse wheel event currently, only
supported document (overall screen) mouse wheel.
"""

from typing import Callable
from typing import Optional
from typing import TypeVar

from apysc._event.wheel_event import WheelEvent
from apysc._html.debug_mode import add_debug_info_setting

_O = TypeVar('_O')
_Handler = Callable[[WheelEvent, _O], None]


@add_debug_info_setting(  # type: ignore[misc]
    module_name=__name__)
def bind_wheel_event_to_document(
        handler: _Handler[_O],
        *,
        options: Optional[_O] = None) -> str:
    """
    Bind wheel event to document (overall window).

    Parameters
    ----------
    handler : _Handler
        Callable that handles wheel event.
    options : dict or None, default None
        Optional arguments dictionary to pass.

    Returns
    -------
    name : str
        Handler's name.

    References
    ----------
    - About the handler options' type document
        - https://simon-ritchie.github.io/apysc/about_handler_options_type.html  # noqa
    """
    import apysc as ap
    from apysc._event.handler import HandlerData
    from apysc._event.handler import append_handler_expression
    from apysc._event.handler import get_handler_name
    from apysc._validation.handler_options_validation import \
        validate_options_type
    validate_options_type(options=options)
    name: str = get_handler_name(handler=handler, instance=ap.document)
    expression: str = (
        f'$({ap.document.variable_name}).on("mousewheel", {name});'
    )
    ap.append_js_expression(expression=expression)

    if options is None:
        options = {}  # type: ignore
    handler_data: HandlerData = {  # type: ignore
        'handler': handler,  # type: ignore
        'options': options,
    }
    e: ap.WheelEvent = ap.WheelEvent(this=ap.document)
    append_handler_expression(
        handler_data=handler_data, handler_name=name, e=e)
    return name


@add_debug_info_setting(  # type: ignore[misc]
    module_name=__name__)
def unbind_wheel_event_from_document(handler: _Handler[_O]) -> None:
    """
    Unbind a specified handler's wheel event from a document
    (overall window).

    Parameters
    ----------
    handler : _Handler
        Callable to unbind.
    """
    import apysc as ap
    from apysc._event.handler import get_handler_name
    name: str = get_handler_name(handler=handler, instance=ap.document)
    expression: str = (
        f'$({ap.document.variable_name}).off("mousewheel", {name});'
    )
    ap.append_js_expression(expression=expression)


@add_debug_info_setting(  # type: ignore[misc]
    module_name=__name__)
def unbind_wheel_event_all_from_document() -> None:
    """
    Unbind all wheels event from the document (overall window).
    """
    import apysc as ap
    expression: str = (
        f'$({ap.document.variable_name}).off("mousewheel");'
    )
    ap.append_js_expression(expression=expression)
