# external package imports.
from enum import Enum

# our package imports.
from ..bstutils import export

@export
class WirelessSecurityTypes(Enum):
    """
    Wireless Security Types enumeration.
    """
    
    NoSecurity = "none"
    """ No security / unsecure network. """
    
    WEP = "wep"
    """ WEP. """

    WPATKIP = "wpatkip"
    """ WPA/TKIP. """

    WPAAES = "wpaaes"
    """ WPA/AES. """

    WPA2TKIP = "wpa2tkip"
    """ WPA2/TKIP. """

    WPA2AES = "wpa2aes"
    """ WPA2/AES. """

    WPA_OR_WPA2 = "wpa_or_wpa2"
    """ WPA or WPA2 (recommended). """
