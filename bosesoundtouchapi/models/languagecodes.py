# external package imports.
from enum import Enum

# our package imports.
from ..bstutils import export

@export
class LanguageCodes(Enum):
    """
    Language Codes enumeration.
    """
    
    NOT_SET = 0
    DANISH = 1
    GERMAN = 2
    ENGLISH = 3
    SPANISH = 4
    FRENCH = 5
    ITALIAN = 6
    DUTCH = 7
    SWEDISH = 8
    JAPANESE = 9
    SIMPLIFIED_CHINESE = 10
    TRADITIONAL_CHINESE = 11
    KOREAN = 12
    THAI = 13
    CZECH = 15
    FINNISH = 16
    GREEK = 17
    NORWEGIAN = 18
    POLISH = 19
    PORTUGUESE = 20
    ROMANIAN = 21
    RUSSIAN = 22
    SLOVENIAN = 23
    TURKISH = 24
    HUNGARIAN = 25


    @classmethod
    def value_from_name(
        cls,
        name:str, 
        default:int|None = None,
        ) -> int | None:
        """
        Return a language value for its name (or value).

        Args:
            name (str):
                Name to resolve; case-insensitive match will be performed.
            default (int):
                Default value to return if `name` argument could not be resolved.

        Returns:
            A value that represents the given name if found; 
            otherwise, the default value.
        """
        if (not isinstance(name, str)):
            return default 

        # prepare for comparison.
        name = name.upper()

        # check for name match.
        for member in LanguageCodes:
            if member.name == name.upper():
                return member.value

        # check for value match.
        for member in LanguageCodes:
            if str(member.value) == name:
                return member.value

        # no match; return default value.
        if (isinstance(default, cls)):
            return default.value
        return default
