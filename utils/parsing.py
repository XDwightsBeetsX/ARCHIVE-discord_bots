# Methods to help parse like for private keys to servers and safes.
# Used in Bot.py files to read in the user's key-values.

from .globals import *
from utils.Keychain import Keychain


def parseKeychainFromFile(folder="keys", filename="key.txt"):
    """
    Parses in the bot's private information into a dictionary of {key:value} pairs.
    This is used to return a `Keychain` object.
    """
    filepath = folder + "/" + filename
    print(f"{CM_UTILS}attempting to read keys from {filepath}...")
    
    # Required bot startup parameters
    print(f"{CM_UTILS}required values in expected file format:")
    for rk in REQUIRED:
        print(f'{rk}{KF_SPLIT}"{rk}"')
    
    # File parsing
    try:
        # Initialize the read keys dictionary
        keychain = Keychain()

        # Go through keys file line-by-line and add to keysDict.
        # Also for each collected key parameter, check it off the required list.
        with open(filepath, 'r+') as keyFile:
            for line in keyFile.readlines():
                ls = line.strip().split(KF_SPLIT)
                key = ls[0].strip()
                val = ls[1].strip()
                keychain.addKeyValue(key, val)
        
        # Not all required 
        if not keychain.hasAllRequired():
            print(f"{CM_UTILS}Did not read all required parameters. Please double-check your key file and try again.")
            print("Quitting")
            quit()
        
        # All required parameters met. Lock the keychain and return data for bot.
        keychain.lockKeys()
        return keychain

    # Catch file errors or other strange beasts
    except Exception as e:
        print(f"{CM_UTILS}there was an error reading data from the file.\nCheck your file input.")
        print(f"{CM_UTILS}[ERROR]: {e}")
        quit()
