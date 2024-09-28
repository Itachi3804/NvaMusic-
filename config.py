import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2500))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002063031380))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7202110938))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/saiboks/NvaMusic-",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/where_lucy")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/PhoenixXsupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 204857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
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


STICKER = [
"CAACAgUAAx0Cd9xEawACEQlmLuvFijxhTZXjFbLPOsZFBoZzYQAC2AUAAkVZsVftrDRpvXZTAAE0BA",
"CAACAgUAAx0Cd9xEawACEQhmLuvFeujHQdaxeDtr3MZThRXa1QACkgcAArZSuVfbJAABQq5pIc80BA",
"CAACAgUAAx0Cd9xEawACEQdmLuvFQdwX-ySKIrmq-JPWItfhhgACwQUAAi9GuVfYV7lLP7xl4zQE",
"CAACAgUAAx0Cd9xEawACEQVmLuuiUNrymw5wWSie-agvZ-_MdgACNAQAAi9GsFf3M2dSfxH-YDQE",
"CAACAgUAAx0Cd9xEawACEQNmLuuKwCEUmunIPFoxUL1Kr2Dp1AAChQgAApAXsFeIwfQvrfbmjjQE",
"CAACAgUAAx0Cd9xEawACEQJmLut22O_5LobAKvCBNlOHbCnQcQAC8gQAAmRQsVdeP26A2AJofzQE",
"CAACAgUAAx0Cd9xEawACEQABZi7rYhnPjPsm_g37JvqoH7qB10gAAsgEAAJWgShXcBbC69nedAY0BA",
"CAACAgUAAx0Cd9xEawACEP9mLutgBdWYCVPqQ_kvUGgYoNVIVwACrAYAAof0IFc6sUwgfJZw6zQE",
"CAACAgEAAx0Cd9xEawACEPtmLusPo3kBvdEigRxbcqGOMSF9cgAC8wMAAqpT6UU55jSF8wAByTc0BA",
"CAACAgEAAx0Cd9xEawACEPpmLusJTIEch-TXN5KsPkvdfnypNgACbwIAAkoY6UUP_O3RGOXeSTQE",
"CAACAgEAAx0Cd9xEawACEPlmLusBSvWNswwz99iOXBMIos0s_QACGAMAAtfI6EX4deIoUongJDQE",
"CAACAgEAAx0Cd9xEawACEPdmLuropCmTrN0Xv4_C7plvS45D3gACrwIAAqyx6EVOdFVb4d8VsDQE",
"CAACAgUAAx0Cd9xEawACEOhmLurMc76ZYy9ZWB0dcuWfNJVSzQACLwUAAk-LuVelZAHYP-pxnTQE",
"CAACAgUAAx0Cd9xEawACEOZmLuq8MMZnoz-txKJ9QEow9qDKxQACKwQAAvbXuVf7GDiuoypXFzQE",
"CAACAgUAAx0Cd9xEawACEORmLuq3Mm3dzamR5W8JZhZHgbPWKwACJwcAAvQcsFefMIzhat8ZtDQE",
"CAACAgUAAx0Cd9xEawACEONmLuqxMsLOLjCsMIf86_QuZH0AAaAAAusMAAIRzNhVUrENdULkjis0BA",
"CAACAgUAAx0Cd9xEawACEOFmLuqryqMN4_7KPq_LLZNIq0OPEgACJAwAAm5mwVXkZ2Ycjy1rRjQE",
"CAACAgUAAx0Cd9xEawACEN9mLuqlG8RAw-L8e1Pv3909WrYMhgACwBUAAh-sOVQ3vSSCUJbSYzQE",
]


START_IMG_URL = ["https://telegra.ph/file/8fb11f38033d3195c9c8c.jpg",
                 "https://telegra.ph/file/106167c80a3fc3ab9f1e8.jpg",
                 "https://telegra.ph/file/89070543c0f7f2e51118d.jpg",
                 "https://telegra.ph/file/3a0afc7a07f35747684eb.jpg",
                 "https://telegra.ph/file/0db46c5fca2c69829a7d4.jpg",
                 "https://telegra.ph/file/f7e5522656c24abf1bd90.jpg",
                 "https://telegra.ph/file/621f76810deb42513f345.jpg",
                 "https://telegra.ph/file/095d4d1a638bd42e54189.jpg",
                 "https://telegra.ph/file/0a6cf2af7eead7fcb0745.jpg"]
    
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/12959de7fe4e4bca30356.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/1d01c99fa880ead2166d8.jpg"
STATS_IMG_URL = "https://telegra.ph/file/010586648d250dba1b940.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/492a3bb2e880d19750b79.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/492a3bb2e880d19750b79.jpg"
STREAM_IMG_URL = "https://unitedcamps.in/Images/file_3061.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e8730fdece86a1166f608.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:360"))


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
