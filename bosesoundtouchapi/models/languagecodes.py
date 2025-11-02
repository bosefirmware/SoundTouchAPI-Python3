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