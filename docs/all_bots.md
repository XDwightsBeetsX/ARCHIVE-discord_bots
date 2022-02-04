# ALL Bots

All discord-bots must have some things in common for easy use.

Consult the [Discord API Reference.](https://discord.com/developers/docs/reference)

## Quick & Easy Startup

1. Store the bot's keys in **`./keys/`**

    **`[UTILS] - expected file format:`**

    ```shell
    bot_name="bot_name"
    bot_token="bot_token"
    server="serverAddress"
    client_id="client_id"
    client_secret="client_secret"
    ```

2. Each bot needs a **`main`** function.

    Typically done like this:

    ```python
    if __name__ == '__main__':
        print('Running...')
    ```

## User Help & Messages

- Provide help to the user
  - Discord server
    - `> !help`-style messages
    - Show a list of commands when the bot enters a server
  - Programmer
    - `print()` useful information to the console
    - *and/or* write a log in `./logs/`
