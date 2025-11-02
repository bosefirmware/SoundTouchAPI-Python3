# external package imports.
from enum import Enum

# our package imports.
from ..bstutils import export

@export
class SetupRequestStates(Enum):
    """
    Setup Request States enumeration.
    """
    
    SETUP_ENTER = "SETUP_ENTER"
    """ Enter setup mode. """
    
    SETUP_LANG = "SETUP_LANG"
    """ Language setup mode. """

    SETUP_WIFI = "SETUP_WIFI"
    """ Wifi setup mode. """

    SETUP_LEAVE = "SETUP_LEAVE"
    """ Leave setup mode. """

    SETUP_WIFI_LEAVE = "SETUP_WIFI_LEAVE"
    """ Leave Wifi setup mode. """

    SETUP_ENTER_SETUPAP = "SETUP_ENTER_SETUPAP"
    """ Enter Access Point setup mode. """

    SETUP_IDENTIFY_DEVICE_ENTER = "SETUP_IDENTIFY_DEVICE_ENTER"
    """ Enter device identification setup mode. """

    SETUP_IDENTIFY_DEVICE_LEAVE = "SETUP_IDENTIFY_DEVICE_LEAVE"
    """ Leave device identification setup mode. """

    SETUP_START = "SETUP_START"
    """ Start setup mode. """
