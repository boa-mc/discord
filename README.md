# discord
A Discord bot node

## Installing
> :warning: Remember: mc-server-tools is meant to be run on ubuntu server.

Run the following commands:
```bash
git clone https://github.com/mc-server-tools/discord/
cd discord
python3 main.py
```
You will need to enter a discord token and your [mc-server-tools server](https://github.com/mc-server-tools/server)'s IP address / hostname.
After the setup, the bot will automatically start.

If you want to re-setup the server, use:
```bash
python3 main.py -s
```

## Starting
To start the bot afterwards, use
```bash
python3 main.py
```
If you want to be able to log out of the ssh session while letting the bot run, you can use [screen](https://help.ubuntu.com/community/Screen).

## Discord commands
After you added the bot to a discord server, you can use the following commands:

| Command     | Effect                                            |
|-------------|---------------------------------------------------|
| &setchannel | Set the announcement channel.                     |
| &start      | Starts the Minecraft server.                      |
| &stop       | Stops the Minecraft server and displays its log.  |
| &log        | Displays the Minecraft server's log.              |
| &status     | Shows the current status of the Minecraft server. |
| &help       | List commands                                     |