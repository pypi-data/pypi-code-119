from .ABC import SQLType


def _int_cast_(size):
    def cast(value):
        value = int(value)
        if value.bit_length() > size:
            raise ValueError(f'can only accept {size} bits but got {value.bit_length()} bits')
        return int(value)

    return cast


INT64 = BIGINT = SQLType('BIGINT', caster=_int_cast_(64), default=0)
INT32 = INT = INTEGER = SQLType('INT', caster=_int_cast_(32), default=0)
INT24 = MEDIUMINT = SQLType('MEDIUMINT', caster=_int_cast_(24), default=0)
INT16 = SMALLINT = SQLType('SMALLINT', caster=_int_cast_(16), default=0)
INT8 = TINYINT = SQLType('TINYINT', caster=_int_cast_(8), default=0)

BIT = SQLType('BIT', 1, get_caster=lambda self: _int_cast_(self.args[0]), default=0, modifiable=True)
BOOL = SQLType('BIT', 1, caster=lambda value: True if value else False, default=False, parser=lambda value: '1' if value else '0')

FLOAT = SQLType('FLOAT', caster=float, default=0.0)
DOUBLE = SQLType('DOUBLE', 12, 6, caster=float, default=0.0, modifiable=True)
DEC = DECIMAL = SQLType('DECIMAL', 12, 6, caster=float, default=0.0, modifiable=True)

STRING = VARCHAR = SQLType('VARCHAR', 255, caster=lambda value: f"{value}", default='', parser=lambda value: f"'{value}'", modifiable=True)
CHAR = SQLType('CHAR', 255, caster=lambda value: f"{value}", default='', parser=lambda value: f"'{value}'", modifiable=True)

type_dict = {
    INT64: ['bigint'],
    INT32: ['int', 'integer'],
    INT24: ['mediumint'],
    INT16: ['smallint'],
    INT8: ['tinyint'],
    BIT: ['bit'],
    BOOL: ['bool', 'boolean'],
    FLOAT: ['float'],
    DOUBLE: ['double'],
    DEC: ['decimal', 'dec'],
    STRING: ['varchar'],
    CHAR: ['char']
}


def string_to_type(string: str):
    args = string[string.find('(') + 1:string.rfind(')')]
    string = string[:string.find('(')].lower()
    for key, value in type_dict.items():
        if string in value:
            if not key.modifiable:
                return key
            return key(*[int(arg) for arg in args.split(',')])
    return None
