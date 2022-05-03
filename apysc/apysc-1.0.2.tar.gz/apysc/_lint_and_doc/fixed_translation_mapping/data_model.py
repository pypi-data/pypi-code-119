"""This module is for the data model of the fixed-translation
mapping settings.
"""

import inspect
import os
from functools import lru_cache
from types import ModuleType
from typing import List
from typing import Optional
from typing import Tuple

from apysc._lint_and_doc.docs_lang import Lang


class Mapping:
    """This class is for a single fixed-translation mapping setting.
    """

    _key: str
    _val: str

    def __init__(self, *, key: str, val: str) -> None:
        """
        A single fixed-translation mapping setting.

        Parameters
        ----------
        key : str
            A key value (this value needs to set source
            English string).
        val : str
            A translated value.
        """
        self._key = key
        self._val = val

    @property
    def key(self) -> str:
        """
        Get a key value (a source english string).

        Returns
        -------
        key : str
            A key value (a source english string).
        """
        return self._key

    @property
    def val(self) -> str:
        """
        Get a translated value.

        Returns
        -------
        val : str
            A translated value.
        """
        return self._val


class Mappings:
    """This class is for fixed-translation mappings settings.
    """

    mappings: List[Mapping]

    def __init__(self, mappings: List[Mapping]) -> None:
        """
        The class for fixed-translation mappings settings.

        Parameters
        ----------
        mappings : list of Mapping
            A target mappings list.
        """
        self.mappings = mappings


def get_fixed_translation_str_if_exists(
        *, key: str, lang: Lang) -> str:
    """
    If a mapping setting exists, get a fixed-translation
    string from a specified language key string.

    Parameters
    ----------
    key : str
        A target key string (source English string).
    lang : Lang
        A target language.

    Returns
    -------
    translation_str : str
        A translated string. If there is no fixed-translation
        mapping setting, this interface returns a blank string.
    """
    mappings: Optional[Mappings] = _read_mappings(lang=lang)
    if mappings is None:
        return ''
    for mapping in mappings.mappings:
        if mapping.key == key:
            return mapping.val
    return ''


@lru_cache(maxsize=None)
def _read_mappings(*, lang: Lang) -> Optional[Mappings]:
    """
    Read a fixed-translation mappings settings if it exists.

    Parameters
    ----------
    lang : Lang
        A target language.

    Returns
    -------
    mappings : Mappings or None
        A read mappings settings. If there is no mappings
        settings, this interface returns None.
    """
    from apysc._file import module_util
    module_path: str = _get_mappings_module_path_from_lang(lang=lang)
    if not os.path.isfile(module_path):
        return None
    module: ModuleType = module_util.read_target_path_module(
        module_path=module_path)
    members: List[Tuple[str, Mappings]] = inspect.getmembers(
        module, predicate=lambda x: isinstance(x, Mappings))
    if not members:
        return None
    return members[0][1]


def _get_mappings_module_path_from_lang(*, lang: Lang) -> str:
    """
    Get a fixed-translation mappings settings module path
    of a specified language.

    Parameters
    ----------
    lang : Lang
        A target language.

    Returns
    -------
    module_path : str
        A fixed-translation mappings settings module path
        of a specified language.
    """
    module_path: str = (
        './apysc/_lint_and_doc/fixed_translation_mapping/'
        f'{lang.value}.py'
    )
    return module_path
