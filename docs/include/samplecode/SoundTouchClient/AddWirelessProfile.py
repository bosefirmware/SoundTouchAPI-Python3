from bosesoundtouchapi import *
from bosesoundtouchapi.models import *
from bosesoundtouchapi.uri import *

try:
    
    # create SoundTouch device instance.
    device:SoundTouchDevice = SoundTouchDevice("192.0.2.1") # Bose SoundTouch 10 (initialized device)
    #device:SoundTouchDevice = SoundTouchDevice("192.168.1.84") # Bose SoundTouch 10
            
    # create SoundTouch client instance from device.
    client:SoundTouchClient = SoundTouchClient(device)

    # build a wireless profile to add.
    profile:WirelessProfile = WirelessProfile(
        ssid="your_network_ssid_name",
        password="your_network_ssid_password",
        securityType=WirelessSecurityTypes.WPA_OR_WPA2,
        timeoutSecs=30
    )

    # add a wireless profile to the device.
    client.AddWirelessProfile(profile)

    # get real-time configuration from the device.
    wirelessProfile:WirelessProfileActive = client.GetWirelessProfile(True)
    print(wirelessProfile.ToString())

except Exception as ex:

    print("** Exception: %s" % str(ex))
