#The repo is fully coded and modified by @Dypixx.
#Please do not sell or remove credits.

import os

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN = int(os.getenv("ADMIN", ""))

DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "")) #Channel Id
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002364289630"))

DB_URI = os.getenv("DB_URI", "mongodb+srv://instadownloadmv:instadownloadmv@cluster0.au6obsd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Force Subscribe Enable
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH

ENABLE_FLOOD_WAIT = bool(os.getenv("ENABLE_FLOOD_WAIT", False)) # Set "True" For Enable Floodwait
FLOOD_WAIT_TIME = int(os.getenv("FLOOD_WAIT_TIME", 300)) #5min
