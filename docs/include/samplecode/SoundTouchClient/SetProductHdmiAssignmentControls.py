from bosesoundtouchapi import *
from bosesoundtouchapi.models import *

try:
    
    # create SoundTouch device instance.
    device:SoundTouchDevice = SoundTouchDevice("192.168.1.80")
            
    # create SoundTouch client instance from device.
    client:SoundTouchClient = SoundTouchClient(device)

    # get current product hdmi assignment controls.
    # note that not all devices support retrieval of this information.
    cfgBefore:ProductHdmiAssignmentControls = None
    cfgBefore = client.GetProductHdmiAssignmentControls()
    print("\nCurrent product hdmi assignment controls value: \n%s" % cfgBefore.ToString())
        
    # create new product hdmi assignment controls object.
    cfgUpdate:ProductHdmiAssignmentControls = ProductHdmiAssignmentControls()

    # for testing purposes, toggle the value from SOURCE_NONE to SOURCE_01 or vice versa.
    # if the level is currently SOURCE_NONE, then we will set to SOURCE_01.
    cfgUpdate.HdmiInputSelection01 = HdmiInputSelectionTypes.SOURCE_NONE
    if cfgUpdate.HdmiInputSelection01 == cfgBefore.HdmiInputSelection01:
        cfgUpdate.HdmiInputSelection01 = HdmiInputSelectionTypes.SOURCE_01
    print("\nSetting product hdmi assignment controls to '%s' (from '%s') ..." % (cfgUpdate.HdmiInputSelection01, cfgBefore.HdmiInputSelection01))
                
    # update product hdmi assignment controls.
    client.SetProductHdmiAssignmentControls(cfgUpdate)
            
    # get current product hdmi assignment controls.
    cfgAfter:ProductHdmiAssignmentControls = client.GetProductHdmiAssignmentControls(True)
    print("\nChanged product hdmi assignment controls: \n%s" % (cfgAfter.ToString()))
        
except Exception as ex:

    print("** Exception: %s" % str(ex))

finally:
    
    if cfgBefore is not None:
        
        # restore product hdmi assignment controls to original values.
        client.SetProductHdmiAssignmentControls(cfgBefore)            

        # get current product hdmi assignment controls.
        cfgAfter:ProductHdmiAssignmentControls = client.GetProductHdmiAssignmentControls(True)
        print("\nRestored product hdmi assignment controls: \n%s" % (cfgAfter.ToString()))
