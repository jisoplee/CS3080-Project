# CS3080-Project
For CS3080 Fall 2020 Python Project

Contributors: Ben Martin, Jisop Lee

About Epic Dawn Bot:
  Epic Dawn Bot is a sealed play deck generator for the Yu-Gi-Oh! Trading Card Game set Battle Pack: Epic Dawn. It gathers people for a tournament (ideally with 2 or more players, but you can enter as just 1 for testing purposes), and sends via DM (direct message) the contents of 10 Battle Pack: Epic Dawn packs and a .ydk file of all 50 cards pulled. The .ydk file can be imported into virtual cards on Dueling Book, a third-party website that emulates virtual Yu-Gi-Oh matches.
  
GitHub repository contents:

  main.py - contains all back-end methods, such as database generation, pack opening, deck building, and .ydk generation.

  epicdawnbot.py - contains all front-end Discord integrations, events, and commands.

  BP_Epic_Dawn.txt - text file used to generate card database
  
Important links:

  https://discord.gg/k5HjCvJSrD - Discord channel (running epicdawnbot.py will connect the bot to Discord and run bot commands). Requires account.

  https://duelingbook.com/html5 - Third-party site that emulates virtual Yu-Gi-Oh matches. Requires account.
  
How to run Epic Dawn Bot:
  1. Download the files and run them on a Python environment (we use PyCharm).
  2. In line 273 of epicdawn.py, fill the empty string in client.run('') with the bot token (provided in final report).
  3. Run epicdawnbot.py. After a few seconds, the bot should say 'Epic Dawn Bot is online and running.' in the Python terminal.
  4. You will need a Discord account. Click the discord.gg link in Important Links.
  5. Once you've joined the server, Epic Dawn Bot should welcome you.
  6. Go to the #bot-commands channel and enter !commands.
  7. To start a solo tournament, enter !new, !join, and then !begin.
  
NOTES:
  1. I cannot disclose Epic Dawn Bot's token to the Internet for security reasons. For Dr. Yanyan, I will attach it to the final report that won't be submitted here.
  2. Make sure that when running epicdawnbot.py, that main.py and BP_Epic_Dawn.txt are in the same folder.
  3. You will have to install discord.py entering 'pip install discord.py' in the terminal before running epicdawnbot.py.
