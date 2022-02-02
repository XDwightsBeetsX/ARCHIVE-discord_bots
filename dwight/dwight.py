"""
Learning API through link: https://www.youtube.com/watch?v=xdg39s4HSJQ
John Gutierrez
"""

import discord
import asyncio


client = discord.Client()

discord_bot_name = '2853'
discord_bot_token = 'NjM4OTE1MTI3Mjk4NjIxNDQy.XbkB0w.IhRmAB6pWwtWCuxAhIt3txvcRtU'
discord_server = 'https://discord.gg/CZTBQmc'  # name of server is bot_test
discord_client_id = 638912417648214047
discord_client_secret = 'O1y7XNNt0MXaUY-ImRclLeaa1aMUFyGJ'

# channels and users where bot commands are allowed
channels = ['general', 'commands']
valid_users = ['XDwightsBeetsX#2765']

# vars to keep track of data
data_file = 'data.csv'
messages, joined = 0, 0
stats_delay = 30  # checks server every half minute
data = {}  # author: message_count


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            # reset counter variables
            messages, joined = 0, 0
            print(data)
            await asyncio.sleep(stats_delay)
        except Exception as e:
            print(e)
            await asyncio.sleep(stats_delay)


async def update_file():
    await client.wait_until_ready()

    while not client.is_closed():
        try:
            with open(data_file, 'w') as file:
                file.write('Author,Message Count\n')
                for author, message_count in data.items():
                    file.write(str(author) + ', ' + str(message_count) + '\n')
            await asyncio.sleep(stats_delay)
        except Exception as e:
            print(e)
            await asyncio.sleep(stats_delay)


@client.event
async def on_message(message):
    global messages
    messages += 1

    # get message info
    author, content, channel = str(message.author), str(message.content), str(message.channel)

    # add info to data
    if author not in data.keys():
        data[author] = 1
    else:
        data[author] += 1

    # log in console
    print('New Message in #%s from %s: %s'
          % (channel, author.split('#')[0], content))

    # ensure valid channel and user
    if (channel in channels[1:]) and (author in valid_users):

        # Dwight's commands
        if message.content == '!help':
            await message.channel.send('Commands for Dwight:'
                                       '\n!help: show commands'
                                       '\n!dwight: Dwight says stuff'
                                       '\n!message_count: Dwight tells you total number of messages'
                                       '\n!member_count: Dwight tells you how many peeps on server')

        if message.content == '!dwight':
            await message.channel.send('\"Bears. Beets. Battlestar Galactica.\"')

        if message.content == '!message_count':
            await message.channel.send(f'Number of Messages: {messages}')

        elif message.content == '!member_count':
            await message.channel.send(f'Number of Members: {client.get_guild(discord_client_id).member_count}')

    # regular message, check if trying to use command
    elif content[0] == '!':
        print(f'User {author} tried to use command {content} in #{channel}.')


@client.event
async def on_member_join(member):
    global joined
    joined += 1

    # find channel and welcome member
    for channel in member.sever.channels:
        if channel == channels[0]:
            await channel.send(f'Howdy {member}!')

    # add member to database
    if member not in data.keys():
        data[member] = 0


if __name__ == '__main__':
    print('Running...')
    print(f'Connecting to server %{discord_server}...')
    client.loop.create_task(update_stats())
    client.loop.create_task(update_file())
    client.run(discord_bot_token)
