# external package imports.
from xml.etree.ElementTree import Element

# our package imports.
from ..bstutils import export, _xmlFind
from ..soundtouchmodelrequest import SoundTouchModelRequest
from .wirelesssecuritytypes import WirelessSecurityTypes

@export
class WirelessProfile(SoundTouchModelRequest):
    """
    SoundTouch device WirelessProfile configuration object.
       
    This class contains the attributes and sub-items that represent the
    wireless profile configuration of the device.
    """

    def __init__(self, ssid:str=None, password:str=None, securityType:WirelessSecurityTypes|str=None, timeoutSecs:int=None,
                 root:Element=None
                 ) -> None:
        """
        Initializes a new instance of the class.
        
        Args:
            ssid (str):
                Wifi network service set identifier (SSID).
            password (str):
                Wifi network password.
            securityType (WirelessSecurityTypes):
                Wifi network security type.
            timeoutSecs (int):
                Time to wait (in seconds) for the request to be processed before raising
                an exception for taking too long.
            root (Element):
                xmltree Element item to load arguments from.  
                If specified, then other passed arguments are ignored.
                
        Raises:
            SoundTouchError:
                startItem argument was not of type int.  
        """
        self._Password:str = None
        self._SecurityType:str = None
        self._Ssid:str = None
        self._TimeoutSecs:int = None

        if (root is None):

            # convert enums to strings.
            if isinstance(securityType, WirelessSecurityTypes):
                securityType = securityType.value
            if securityType is None:
                securityType = WirelessSecurityTypes.WPA_OR_WPA2.value

            if (not isinstance(timeoutSecs, int)):
                timeoutSecs = 30
            if (timeoutSecs < 5) or (timeoutSecs > 60):
                timeoutSecs = 30
                
            self._Ssid = ssid
            self._Password = password
            self._SecurityType = securityType
            self._TimeoutSecs = timeoutSecs

        else:

            self._Ssid = _xmlFind(root, 'ssid')
            self._Password = _xmlFind(root, 'password')
            self._SecurityType = _xmlFind(root, 'securityType')
            self._TimeoutSecs = 30


    def __repr__(self) -> str:
        return self.ToString()


    def __str__(self) -> str:
        return self.ToString()


    @property
    def Ssid(self) -> str:
        """ Wifi network service set identifier (SSID) to connect to. """
        return self._Ssid


    @property
    def Password(self) -> str:
        """ Wifi network password. """
        return self._Password


    @property
    def SecurityType(self) -> str:
        """ Wifi network security type. """
        return self._SecurityType


    @property
    def TimeoutSecs(self) -> str:
        """ 
        Time to wait (in seconds) for the request to be processed before raising
        an exception for taking too long. 
        """
        return self._TimeoutSecs


    def ToDictionary(self) -> dict:
        """
        Returns a dictionary representation of the class.
        """
        result:dict = \
        {
            'ssid': self._Ssid,
            'password': self._Password,
            'security_type': self._SecurityType,
            'timeout': self._TimeoutSecs,
        }
        return result
        

    def ToElement(self, isRequestBody:bool=False) -> Element:
        """ 
        Overridden.  
        Returns an xmltree Element node representation of the class. 

        Args:
            isRequestBody (bool):
                True if the element should only return attributes needed for a POST
                request body; otherwise, False to return all attributes.
        """
        # create parent element.
        elm = Element('AddWirelessProfile')
        elm.set('timeout', str(self._TimeoutSecs))

        # create child element.
        elmChild = Element('profile')
        elmChild.set('ssid', str(self._Ssid))
        elmChild.set('password', str(self._Password))
        elmChild.set('securityType', str(self._SecurityType))
        elm.append(elmChild)
        
        # return to caller.
        return elm


    def ToString(self) -> str:
        """
        Returns a displayable string representation of the class.
        """
        msg:str = 'WirelessProfile:'
        if self._Ssid and len(self._Ssid) > 0: msg = '%s ssid="%s"' % (msg, str(self._Ssid))
        if self._Password and len(self._Password) > 0: msg = '%s password="%s"' % (msg, str(self._Password))
        if self._SecurityType and len(self._SecurityType) > 0: msg = '%s securityType="%s"' % (msg, str(self._SecurityType))
        if self._TimeoutSecs: msg = '%s timeout="%s"' % (msg, str(self._TimeoutSecs))
        return msg
