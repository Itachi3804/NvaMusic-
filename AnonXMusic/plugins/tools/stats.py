import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import InputMediaPhoto, Message
from pytgcalls.__version__ import __version__ as pytgver

import config
from AnonXMusic import app
from AnonXMusic.core.userbot import assistants
from AnonXMusic.misc import SUDOERS, mongodb
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from AnonXMusic.utils.decorators.language import language, languageCB
from AnonXMusic.utils.inline.stats import back_stats_buttons, stats_buttons
from config import BANNED_USERS

# Stats command (Global stats)
@app.on_message(filters.command(["stats", "gstats"]) & filters.group & ~BANNED_USERS)
@language
async def stats_global(client, message: Message, _):
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    
    # Image ko quote format mein bhejna bina kisi caption ke
    await message.reply_photo(
        photo=config.STATS_IMG_URL
    )
    
    # Phir text aur buttons ek alag message mein bhejna
    await message.reply_text(
        _["gstats_2"].format(app.mention),
        reply_markup=upl
    )

# Callback for stats back button
@app.on_callback_query(filters.regex("stats_back") & ~BANNED_USERS)
@languageCB
async def home_stats(client, CallbackQuery, _):
    upl = stats_buttons(_, True if CallbackQuery.from_user.id in SUDOERS else False)
    
    # Pehle image bina caption ke bhejni hai
    await CallbackQuery.message.reply_photo(
        photo=config.STATS_IMG_URL
    )
    
    # Phir text aur buttons bhejne hain
    await CallbackQuery.message.reply_text(
        text=_["gstats_2"].format(app.mention),
        reply_markup=upl
    )

# Callback for overall stats button
@app.on_callback_query(filters.regex("TopOverall") & ~BANNED_USERS)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    await CallbackQuery.answer()
    
    # Back button ke liye options
    upl = back_stats_buttons(_)

    # Pehle image bhejni bina caption ke
    await CallbackQuery.message.reply_photo(photo=config.STATS_IMG_URL)

    # Phir text aur buttons bhejne hain
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_3"].format(
        app.mention,
        len(assistants),
        len(BANNED_USERS),
        served_chats,
        served_users,
        len(ALL_MODULES),
        len(SUDOERS),
        config.AUTO_LEAVING_ASSISTANT,
        config.DURATION_LIMIT_MIN,
    )
    await CallbackQuery.message.reply_text(
        text,
        reply_markup=upl
    )

# Sudo bot stats callback
@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def bot_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id not in SUDOERS:
        return await CallbackQuery.answer(_["gstats_4"], show_alert=True)
    
    upl = back_stats_buttons(_)

    # Image bhejni bina caption ke
    await CallbackQuery.message.reply_photo(photo=config.STATS_IMG_URL)

    # Phir text aur buttons ke saath stats bhejne hain
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)} GHz"
        else:
            cpu_freq = f"{round(cpu_freq, 2)} MHz"
    except:
        cpu_freq = "Failed to fetch"
    
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    used = hdd.used / (1024.0**3)
    free = hdd.free / (1024.0**3)
    call = await mongodb.command("dbstats")
    datasize = call["dataSize"] / 1024
    storage = call["storageSize"] / 1024
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    
    text = _["gstats_5"].format(
        app.mention,
        len(ALL_MODULES),
        platform.system(),
        ram,
        p_core,
        t_core,
        cpu_freq,
        pyver.split()[0],
        pyrover,
        pytgver,
        str(total)[:4],
        str(used)[:4],
        str(free)[:4],
        served_chats,
        served_users,
        len(BANNED_USERS),
        len(await get_sudoers()),
        str(datasize)[:6],
        storage,
        call["collections"],
        call["objects"],
    )
    await CallbackQuery.message.reply_text(
        text,
        reply_markup=upl
    )