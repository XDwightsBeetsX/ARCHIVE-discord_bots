
import time
import discord
import asyncio

from utils.parsing import parseKeychainFromFile
from utils.Keychain import Keychain


class DiscordBot(object):
    """
    An example discord bot with some classic methods.
    """
    def __init__(self, keychain):
        """
        - Initialize the bot with a Keychain that holds secret info.
        - Construct the discord.Client()
        
        Optionally:
        - Set up some methods to write log/stat files.
        """
        self.Client = discord.Client()
        self.Keychain = keychain
        
        self.Name = "Example Bot"
        self.SpecialChar = '!'

        self.LogFilepath = "logs/log.log"
        self.StatsFilepath = "stats/stats.txt"
    
    def run(self):
        """
        Begins the client routine.
        """
        print(f"Starting {self.Name}...")
        self.Client.run(self.Keychain.BotToken)

    def sendMessage(self, message):
        """
        1. Connect to server with Keychain
        2. Post message
        """
        pass

    def writeStatsToFile(self):
        """
        It might be nice to write statistics or users to file...
        """
        statlines = []
        
        try:
            with open(self.StatsFilepath, 'w+') as statsFile:
                statsFile.writelines(statlines)
        
        except Exception as e:
            print("[ERROR] - There was an issue writing to the stats file:")
            print(e)

    def logLine(self, line):
        """
        Write line to the log file at Self.LogFilepath.
        """
        try:
            with open(self.LogFilepath, 'w+') as logFile:
                logFile.write(line + '\n')
        
        except Exception as e:
            print("[ERROR] - There was an issue writing to the log file:")
            print(e)


if __name__ == "__main__":
    print("Starting Example Bot...")
    print("The world has much to fear.")

    keychain = parseKeychainFromFile("keys/example_bot_key.txt")
    DB = DiscordBot(keychain)
    DB.run()
