from bosesoundtouchapi import *
from bosesoundtouchapi.models import LanguageCodes

try:
    
    # create SoundTouch device instance.
    device:SoundTouchDevice = SoundTouchDevice("192.168.1.81") # Bose SoundTouch 10
            
    # create SoundTouch client instance from device.
    client:SoundTouchClient = SoundTouchClient(device)

    # get current language value.
    oldValue:str = client.GetLanguage(True).Value
    print("Language Before: '%s'" % oldValue)
    
    # set the device language.
    client.SetLanguage(LanguageCodes.ENGLISH)

    # get current language value.
    newValue:str = client.GetLanguage(True).Value
    print("Language After:  '%s'" % newValue)

except Exception as ex:

    print("** Exception: %s" % str(ex))
