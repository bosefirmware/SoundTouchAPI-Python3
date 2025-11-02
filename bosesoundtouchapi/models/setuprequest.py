# external package imports.
from xml.etree.ElementTree import Element

# our package imports.
from ..bstutils import export
from ..soundtouchmodelrequest import SoundTouchModelRequest
from .setuprequeststates import SetupRequestStates

@export
class SetupRequest(SoundTouchModelRequest):
    """
    SoundTouch device Setup Request configuration object.
       
    This class contains the attributes and sub-items that represent
    setup request criteria.
    """

    def __init__(
        self, 
        requestState:SetupRequestStates,
        timeoutMS:int=None,
        ) -> None:
        """
        Initializes a new instance of the class.
        
        Args:
            requestState (SetupRequestStates):
                Setup request state to process.
            timeoutMS (int):
                Timeout value (in milliseconds); only used for some setup states.
                
        Raises:
            SoundTouchError:
                startItem argument was not of type int.  
        """
        self._State:str = None
        self._TimeoutMS:int = None

        # convert enums to strings.
        if isinstance(requestState, SetupRequestStates):
            requestState = requestState.value

        # validations.
        if (timeoutMS is not None):
            if (not isinstance(timeoutMS, int)):
                timeoutMS = 3000
            if (timeoutMS < 1000) or (timeoutMS > 300000):
                timeoutMS = 3000

        self._State = requestState
        self._TimeoutMS = timeoutMS


    def __repr__(self) -> str:
        return self.ToString()


    def __str__(self) -> str:
        return self.ToString()


    @property
    def State(self) -> str:
        """ 
        Setup state to request.

        See `SetupRequestStates` enum for more details.
        """
        return self._State

    @State.setter
    def State(self, value:str):
        """ 
        Sets the State property value.
        """
        if isinstance(value, SetupRequestStates):
            value = value.value
        self._State = value


    @property
    def TimeoutMS(self) -> str:
        """ 
        Setup timeout value.
        """
        return self._TimeoutMS

    @TimeoutMS.setter
    def TimeoutMS(self, value:str):
        """ 
        Sets the TimeoutMS property value.
        """
        self._TimeoutMS = value


    def ToElement(self, isRequestBody:bool=False) -> Element:
        """ 
        Overridden.  
        Returns an xmltree Element node representation of the class. 

        Args:
            isRequestBody (bool):
                True if the element should only return attributes needed for a POST
                request body; otherwise, False to return all attributes.
        """
        elm = Element('setupState')
        elm.set('state', str(self._State))
        if (self._TimeoutMS is not None):
            elm.set('timeout', str(self._TimeoutMS))
        return elm
        
        
    def ToString(self) -> str:
        """
        Returns a displayable string representation of the class.
        """
        msg:str = 'SetupState:'
        msg = '%s state="%s"' % (msg, str(self._State))
        if self._TimeoutMS is not None: msg = '%s timeout="%s"' % (msg, str(self._TimeoutMS))
        return msg 
