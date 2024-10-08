import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")

BOT_TOKEN = getenv("BOT_TOKEN", "6607357754:AAHv3nZdp5aRo-DDXD_QgX9RxrbszwG1fpY")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://IYIusic:P8QtOotbu7QrXVNI@iyiusic.dlxc3.mongodb.net/?retryWrites=true&w=majority&appName=IYIusic")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOGGER_ID = int(getenv("LOGGER_ID",-1002105614809))

OWNER_ID = int(getenv("OWNER_ID", 5810668543))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/PiadBoT/IYIusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SuperBanSBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AM_YTSUPPORT")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION", "BQC6kfsAvhnR04ErG1WMWnmKoaoklAjBeuG_trj-J348ygus4eP0-bV1w4fDqAkfqFF82Fk5tHo5fV67Wd20wRPzwh12iTupUA2Nynivb34_V_R1fDJ-n1ga_oattdPQ3ENdP9mw1QWMug5LFX-PW9c3LhvpBpWkoKozUcXUYwk5vLUeEiDISAahrcZV5YQ8bdFmiPdDg8h8t6eXFGSmBSl3bamBn7MewvIoho26rqlsEaYhvKND8uEAJWX6sgN8H64TYkilGr-13_yNi5wj-FUVbxTdlf-fAXB2d9eGpg5UHJp5mmUHJmeZYNzdpyFSnq4tKedZwk0E6YyZUyhHTn8n5Dh6tQAAAAGZs7ltAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/4e68b6d15e042249fb284.png")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/4e68b6d15e042249fb284.png")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://telegra.ph/file/4e68b6d15e042249fb284.png")
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
