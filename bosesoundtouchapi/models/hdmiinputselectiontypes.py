# external package imports.
from enum import Enum

# our package imports.
from ..bstutils import export

@export
class HdmiInputSelectionTypes(Enum):
    """
    HDMI Input Selection Types enumeration.
    """
    
    SOURCE_NONE = "HDMI_IN_BUTTON_NONE"
    """
    No input source selected.
    """

    SOURCE_01 = "HDMI_IN_BUTTON_SOURCE_01"
    """
    Input button source 1 selected.
    """

    SOURCE_02 = "HDMI_IN_BUTTON_SOURCE_02"
    """
    Input button source 2 selected.
    """

    SOURCE_03 = "HDMI_IN_BUTTON_SOURCE_03"
    """
    Input button source 3 selected.
    """


    @staticmethod    
    def ToString(value) -> str:
        """ Returns the enum.value (instead of classname.value) as a string. """
        if isinstance(value, HdmiInputSelectionTypes):
            return value.value
        return str(value)
