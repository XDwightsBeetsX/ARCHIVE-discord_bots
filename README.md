# discord-bots

<img src="imgs/discord_logo.png" style="width: 16px;"/> **Discord Bots!** <img src="imgs/discord_logo.png" style="width: 16px;"/>

*Bots can and should:*

- Interact on the server
- Track member stats
- Do cool things
  - Music
  - Pictures

---

Table of Contents

- [discord-bots](#discord-bots)
  - [Usage](#usage)
    - [Add the Bot to Your Server](#add-the-bot-to-your-server)
    - [Download the repo](#download-the-repo)
    - [Check the requirements.txt](#check-the-requirementstxt)
    - [Add Your Discord Secrets](#add-your-discord-secrets)
    - [Run the Bot(s)](#run-the-bots)
  - [The Bots](#the-bots)
    - [Dwight](#dwight)
    - [Example Bot](#example-bot)
  - [Docs](#docs)

## Usage

### Add the Bot to Your Server

Follow the guide [here](https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-bot)

- Starting a server
- Creating a bot on the [Discord Dev Portal](https://discord.com/developers/docs)
- Adding the bot to your server
  - Permissions
- Getting started with Discord Bots in python

### Download the repo

Use one of the following or just download the `.zip` [here.](https://github.com/XDwightsBeetsX/discord-bots)

```shell
> gh repo clone XDwightsBeetsX/discord-bots
```

```shell
> git clone https://github.com/XDwightsBeetsX/discord-bots.git
```

### Check the [requirements.txt](./requirements.txt)

- Most will need to simply install the discord python API:

  ```shell
  > pip install discord
  ```

- You can also make sure you got it all (it's not much):

  ```shell
  > pip install requirements.txt
  ```

### Add Your Discord Secrets

- Store tokens/keys in a folder like `keys`
  - **Add your folder to the `.gitignore`** to keep your key(s) safe
  - Add files like `keys/dwight.txt`
  - Parse these in with the bot using `utils/Parsing`

### Run the Bot(s)

Easily run bots like any other python script!

  ```shell
  > python <bot-name>.py
  ```

## [The Bots](docs/all_bots.md)

### [Dwight](./dwight.py)

The first bot!

| Discord Command | Info |
| :-- | :-- |
| `!help` | Prints off a list of available commands. |
| `!dwight` | Messages: "Bears, Beets, Battlestar Galactica" |
| `!message_count` | Dwights lets you know how many messages have been sent. |
| `!member_count` | Dwight tells you how popular your server is |

### [Example Bot](./example.py)

A template for making new bots.

Offers some skeleton methods:

- `__main__`
- `run()`
- `sendMessage(message)`
- `writeStatsToFile()`
- `logLine(line)`

## [Docs](./docs/)

- General
  - [bot suggestions](docs/all_bots.md)
  - [creating a discord app](docs/create_application.md)
  - [generating bot tokens](docs/generating_bot_tokens.md)
- Bots
  - [dwight](docs/dwight.md)

> *with reference to:* [*realpython's tutorial*](https://realpython.com/how-to-make-a-discord-bot-python/)
>
> *links:*
> [*Discord Developer Portal*](https://discord.com/developers/docs)
