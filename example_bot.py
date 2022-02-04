"""
An example python discord-bot with some template methods.
"""

import discord
from utils.parsing import parseKeychainFromFile


class DiscordBot(object):
    """
    An example python discord-bot with some template methods.
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

        self.CM_PRE = "[EXAMPLE_BOT] - "
        self.LogFilepath = "logs/log.log"
        self.StatsFilepath = "stats/stats.txt"
    
    def run(self):
        """
        Begins the client routine.

        Tests API connection with `Client.event async def on_ready()`
        """
        print(f"{self.CM_PRE}Starting {self.Name}...")
        
        @self.Client.event
        async def on_ready():
            print(f"{self.CM_PRE}{self.Name} is connected to Discord.")
        
        self.Client.run(self.Keychain.BotToken)

    async def sendMessage(self, channel, message):
        """
        Posts `message` in `channel`.
        """
        await channel.send(message)

    def writeStatsToFile(self):
        """
        It might be nice to write statistics or users to file...
        """
        statlines = []
        
        try:
            with open(self.StatsFilepath, 'w+') as statsFile:
                statsFile.writelines(statlines)
        
        except Exception as e:
            print(f"{self.CM_PRE}[ERROR] - There was an issue writing to the stats file:")
            print(f">{e}")

    def logLine(self, line):
        """
        Write line to the log file at Self.LogFilepath.
        """
        try:
            with open(self.LogFilepath, 'w+') as logFile:
                logFile.write(line + '\n')
        
        except Exception as e:
            print(f"{self.CM_PRE}[ERROR] - There was an issue writing to the log file:")
            print(f">{e}")


# =========================================================================================== #
if __name__ == "__main__":
    keychain = parseKeychainFromFile("example_bot.txt")
    DB = DiscordBot(keychain)
    
    print(f"Starting {DB.Name}...")
    print("The world has much to fear.")

    DB.run()
