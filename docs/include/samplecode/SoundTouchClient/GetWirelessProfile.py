from bosesoundtouchapi import *
from bosesoundtouchapi.models import *
from bosesoundtouchapi.uri import *

try:
    
    # create SoundTouch device instance.
    device:SoundTouchDevice = SoundTouchDevice("192.168.1.81") # Bose SoundTouch 10
            
    # create SoundTouch client instance from device.
    client:SoundTouchClient = SoundTouchClient(device)

    # get real-time configuration from the device.
    wirelessProfile:WirelessProfileActive = client.GetWirelessProfile()
    print(wirelessProfile.ToString())

    # get cached configuration, refreshing from device if needed.
    wirelessProfile:WirelessProfileActive = client.GetWirelessProfile(False)
    print("\nCached configuration:\n%s" % wirelessProfile.ToString())

    # get cached configuration directly from the configuration manager dictionary.
    if SoundTouchNodes.getActiveWirelessProfile.Path in client.ConfigurationCache:
        wirelessProfile:WirelessProfileActive = client.ConfigurationCache[SoundTouchNodes.getActiveWirelessProfile.Path]
        print("\nCached configuration, direct:\n%s" % wirelessProfile.ToString())
        
except Exception as ex:

    print("** Exception: %s" % str(ex))
