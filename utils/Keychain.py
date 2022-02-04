# A compact way of storing Key-Values
# Able to check against the globals.REQUIRED Key-Values

from .globals import *

class Keychain(object):
    """
    An easier way to keep track of important keys that might be used against you.
    
    - `addKeyValue` - update `self.KeysDict`
    - `hasAllRequired` - check if `self.KeysDict` has all required fields
    - `lockKeys` - set data members to values in `self.KeysDict`
    """
    def __init__(self):
        self.KeysDict = {}
        self.RequiredKeys = REQUIRED

        # Required-s set after self.lockKeys()
        self.BotName = None
        self.BotToken = None
        self.Server = None
        self.ClientId = None
        self.ClientSecret = None
    
    def addKeyValue(self, key, value):
        """
        Updates the `self.KeysDict`.
        """
        self.KeysDict[key] = value
    
    def hasAllRequired(self):
        """
        Go through all `self.RequiredKeys` and make sure they are present in `self.KeysDict`.

        returns True when all `self.RequiredKeys` are in `self.KeysDict` and False otherwise.
        """
        for k in self.RequiredKeys:
            if k not in self.KeysDict.keys():
                return False
        return True

    def lockKeys(self):
        """
        Sets data members to their Key-Values.
        
        NOTE: Important to do this before using these data member names.
        """
        self.BotName = self.KeysDict[KF_BOT_NAME]
        self.BotToken = self.KeysDict[KF_BOT_TOKEN]
        self.Server = self.KeysDict[KF_SERVER]
        self.ClientId = self.KeysDict[KF_CLIENT_ID]
        self.ClientSecret = self.KeysDict[KF_CLIENT_SECRET]
