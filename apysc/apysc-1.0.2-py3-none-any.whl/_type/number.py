"""Class implementation of the floating-point number value.
"""

from typing import Any
from typing import Union

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number_value_interface import NumberValueInterface


class Number(NumberValueInterface[float, 'Number']):
    """
    Floating point number class for the apysc library.

    Notes
    -----
    The `Float` class is the alias of the Number,
    and it behaves the same as the Number class.

    References
    ----------
    - Int and Number document
        - https://simon-ritchie.github.io/apysc/int_and_number.html
    - Int and Number common arithmetic operations document
        - https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html  # noqa
    - Int and Number common comparison operations document
        - https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> number: ap.Number = ap.Number(10.5)
    >>> number
    Number(10.5)

    >>> number == 10.5
    Boolean(True)

    >>> number == ap.Number(10.5)
    Boolean(True)

    >>> number >= 10.5
    Boolean(True)

    >>> number += 10.3
    >>> number
    Number(20.8)
    """

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='Number')
    def __init__(
            self,
            value: Union[int, float, NumberValueInterface]) -> None:
        """
        Floating point number class for apysc library.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial floating point number value. This class
            casts it to float if you specify int or Int value.

        Notes
        -----
        The `Float` class is the alias of the Number, and it behaves
        the same as the Number class.

        References
        ----------
        - Int and Number document
            - https://simon-ritchie.github.io/apysc/int_and_number.html
        - Int and Number common arithmetic operations document
            - https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html  # noqa
        - Int and Number common comparison operations document
            - https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> number: ap.Number = ap.Number(10.5)
        >>> number
        Number(10.5)

        >>> number == 10.5
        Boolean(True)

        >>> number == ap.Number(10.5)
        Boolean(True)

        >>> number >= 10.5
        Boolean(True)

        >>> number += 10.3
        >>> number
        Number(20.8)
        """
        from apysc._converter import cast
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import \
            TemporaryNotHandlerScope
        with TemporaryNotHandlerScope():
            TYPE_NAME: str = var_names.NUMBER
            self.variable_name = expression_variables_util.\
                get_next_variable_name(type_name=TYPE_NAME)
            super(Number, self).__init__(value=value, type_name=TYPE_NAME)
            self._value = cast.to_float_from_int(int_or_float=self.value)
            self.append_constructor_expression()

    def _set_value_and_skip_expression_appending(
            self, *, value: Union[int, float, Any]) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : int or float or Int or Number
            Any number value to set. If a float or Number
            value is specified, this interface casts its
            value to an integer.
        """
        from apysc._converter import cast
        from apysc._validation import number_validation
        number_validation.validate_num(num=value)
        if isinstance(value, NumberValueInterface):
            value._value = cast.to_float_from_int(int_or_float=value._value)
            value_ = value._value
        else:
            value = cast.to_float_from_int(int_or_float=value)
            value_ = value
        self._value = value_

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        if not hasattr(self, '_value'):
            repr_str: str = 'Number(0)'
        else:
            repr_str = f'Number({self._value})'
        return repr_str
