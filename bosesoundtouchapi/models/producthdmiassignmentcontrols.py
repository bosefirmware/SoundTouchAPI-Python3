# external package imports.
from typing import Iterator
from xml.etree.ElementTree import Element

# our package imports.
from ..bstutils import export
from ..soundtouchmodelrequest import SoundTouchModelRequest
from .hdmiinputselectiontypes import HdmiInputSelectionTypes

@export
class ProductHdmiAssignmentControls(SoundTouchModelRequest):
    """
    SoundTouch device ProductHdmiAssignmentControls configuration object.
       
    This class contains the attributes and sub-items that represent the 
    Product HDMI Assignment Controls configuration of the device.      
    """

    def __init__(self, root:Element=None) -> None:
        """
        Initializes a new instance of the class.
        
        Args:
            root (Element):
                xmltree Element item to load arguments from.  
                If specified, then other passed arguments are ignored.
        """
        # initialize storage.
        self._HdmiInputSelection01:str = None

        if (root is None):

            pass

        elif root.tag == 'producthdmiassignmentcontrols':

            # base fields.
            self._HdmiInputSelection01 = root.get('hdmiinputselection_01')

    def __repr__(self) -> str:
        return self.ToString()


    def __str__(self) -> str:
        return self.ToString()


    @property
    def HdmiInputSelection01(self) -> str:
        """ 
        The HDMI input selection 1 value. 

        See `HdmiInputSelectionTypes` for more information.
        """
        return self._HdmiInputSelection01


    @HdmiInputSelection01.setter
    def HdmiInputSelection01(self, value:str):
        """ 
        Sets the HdmiInputSelection01 property value.
        """
        if value != None:
            if isinstance(value, HdmiInputSelectionTypes):
                self._HdmiInputSelection01 = value.value
            elif isinstance(value, str):
                self._HdmiInputSelection01 = value


    def ToDictionary(self) -> dict:
        """
        Returns a dictionary representation of the class.
        """
        result:dict = \
        {
            'hdmi_input_selection_01': self._HdmiInputSelection01,
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
        elm = Element('producthdmiassignmentcontrols')
        
        if self._HdmiInputSelection01 is not None and len(self._HdmiInputSelection01) > 0: elm.set('hdmiinputselection_01', self._HdmiInputSelection01)
        if isRequestBody == True:
            return elm

        return elm

        
    def ToString(self) -> str:
        """
        Returns a displayable string representation of the class.
        """
        msg:str = 'ProductHdmiAssignmentControls:'
        msg = '%s HdmiInputSelection01="%s"' % (msg, str(self._HdmiInputSelection01))
        return msg 
