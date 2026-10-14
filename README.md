# open-when
A discord bot that gives personalized letters based on moods.
There is an interactive letter box with a clickable menu. When a letter is opened, the user can return to open more

<br>
This was made with discord.py and python-dotenv
<br>
Current letters incude:

Open when you're anxious

Open when you miss me

Open when you're having a bad day

## Do it yourself
Clone the repo with:

git clone https://github.com/thewatermellonman/open-when.git

cd open-when
<br>
Create a virtual Enviornment:

py -m venv .venv

.\.venv\Scripts\Activate.ps1
<br>

Install dependencies:

python -m pip install discord.py python=dotenv

<br>
Set up the bot token:

Create a .env file in the project folder:

DISCORD_TOKEN=BotToken

(replace BotToken with your discord bot token)

Make sure your .gitignore includes:

.env

.venv\

__pycache__/   (with two underscores_ infront and behind pychache)

<br>

Invite the discord bot to your server using the Discord Developer Portal

<br>
Then, start the bot using

python bot.py

in your terminal

<br>
Once in your server, you can use /open !
