""" Userbot initialization. """

# Ported By Sendi

import logging
import os
import re
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from math import ceil
from pathlib import Path
from sys import version_info

from dotenv import load_dotenv
from git import Repo
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from requests import get
from telethon import Button
from telethon.errors import UserIsBlockedError
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, custom, events
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

from .storage import Storage


def STORAGE(n):
    return Storage(Path("data") / n)

load_dotenv("config.env")

StartTime = time.time()
repo = Repo()
branch = repo.active_branch.name

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
ENABLE_KILLME = True
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
ZALG_LIST = {}
CMD_LIST = {}
CMD_HELP = {}
SUDO_LIST = {}
INT_PLUG = ""
LOAD_PLUG = {}

load_dotenv("config.env")

StartTime = time.time()

# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
logging.getLogger("telethon.network.connection.connection").setLevel(logging.ERROR)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 9:
    LOGS.info(
        "Anda HARUS memiliki python setidaknya versi 3.9."
        "Beberapa fitur tergantung versi python ini. Bot berhenti."
    )
    sys.exit(1)


# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

CONFIG_CHECK = (os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________") or None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    sys.exit(1)

while 0 < 6:
    _DEVS = get(
        "https://raw.githubusercontent.com/Cangcimenn//master/DEVS.json"
    )
    if _DEVS.status_code != 200:
        if 0 != 5:
            continue
        DEVS = []
        break
    DEVS = _DEVS.json()
    break

del _DEVS

SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
BL_CHAT = {int(x) for x in os.environ.get("BL_CHAT", "").split()}


# Telegram App KEY and HASH
API_KEY = int(os.environ.get("API_KEY") or None)
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)
STRING_2 = os.environ.get("STRING_2", None)
STRING_3 = os.environ.get("STRING_3", None)
STRING_4 = os.environ.get("STRING_4", None)
STRING_5 = os.environ.get("STRING_5", None)

# Load or No Load modules
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "").split()

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", ""))

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Send .chatid in any group with all your administration bots (added)
G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", "")
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

# Heroku Credentials for updater.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/Cangcimenn/Skyla-Userbot")
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "Skyla-Userbot")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Chrome Driver and Headless Google Chrome Binaries
CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY") or "Bekasi"

# For MONGO based DataBase
MONGO_URI = os.environ.get("MONGO_URI", None)

# set blacklist_chats where you do not want userbot's features
UB_BLACK_LIST_CHAT = os.environ.get("UB_BLACK_LIST_CHAT", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Untuk Perintah .skyalive
SKYLA_TEKS_KUSTOM = os.environ.get("SKYLA_TEKS_KUSTOM") or "**Hi I'am Alive...**"

# Default .alive Name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile Module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# bit.ly Module
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)

# Bot Name
TERM_ALIAS = os.environ.get("TERM_ALIAS", "Skyla-Userbot")

# Bot Version
BOT_VER = os.environ.get("BOT_VER", "1.1.5")

# Default .alive Username
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)

# Sticker Custom Pack Name
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# Cmd Handler Costum
CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."

SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"$")

# Support
GROUP = os.environ.get("GROUP", "SkylaChats")
CHANNEL = os.environ.get("CHANNEL", "Xgrovy_id")

# Default .alive Logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/fc0dbed4ddceac4240589.jpg"

# Default .helpme Logo
INLINE_PIC = os.environ.get(
    "INLINE_PIC") or "https://telegra.ph/file/b2dc33fdd56e3b58ee9c0.jpg"

# Default emoji help
EMOJI_HELP = os.environ.get("EMOJI_HELP") or "☃️"

# Default .alive Instagram
IG_ALIVE = os.environ.get("IG_ALIVE") or "instagram.com/ikyxyzu"

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO") or "Skyla-Userbot"

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)

lastfm = None
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    try:
        lastfm = LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    except Exception:
        pass


TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")

# Genius Lyrics  API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN") or None

# Quotes API Token
QUOTES_API_TOKEN = os.environ.get("QUOTES_API_TOKEN", None)

# Wolfram Alpha API
WOLFRAM_ID = os.environ.get("WOLFRAM_ID") or None

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN") or None
BOT_USERNAME = os.environ.get("BOT_USERNAME") or None


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# Jangan di hapus Nanti ERROR
while 0 < 6:
    _BLACKLIST = get(
        "https://raw.githubusercontent.com/Cangcimenn//master/blacklist.json"
    )
    if _BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        blacklist = []
        break
    blacklist = _BLACKLIST.json()
    break

del _BLACKLIST

# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)


async def check_botlog_chatid() -> None:
    if not BOTLOG_CHATID:
        LOGS.warning(
            "var BOTLOG_CHATID kamu belum di isi. Buatlah grup telegram dan masukan bot @MissRose_bot lalu ketik /id Masukan id grup nya di var BOTLOG_CHATID"
        )
        sys.exit(1)


async def update_restart_msg(chat_id, msg_id):
    message = (
        f"**Skyla-Userbot v{BOT_VER} is back up and running!**\n\n"
        f"**Telethon:** {version.__version__}\n"
        f"**Python:** {python_version()}\n"
        f"**User:** {owner}"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True


try:
    from userbot.modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    with bot:
        try:
            bot.loop.run_until_complete(
                update_restart_msg(
                    int(chat_id), int(msg_id)))
        except BaseException:
            pass
    delgvar("restartstatus")
except AttributeError:
    pass


if BOT_TOKEN is not None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 6
    number_of_cols = 2
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(f"{EMOJI_HELP}", x, f"{EMOJI_HELP}"),
            data="ub_modul_{}".format(x),
        )
        for x in helpable_modules
    ]
    pairs = list(
        zip(
            modules[::number_of_cols],
            modules[1::number_of_cols],
        )
    )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⪻", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "ʙᴀᴄᴋ", data="{}_close({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "⪼", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


with bot:
    try:
        from userbot.modules.sql_helper.bot_blacklists import check_is_black_list
        from userbot.modules.sql_helper.bot_pms_sql import add_user_to_db, get_user_id
        from userbot.utils import reply_id

        dugmeler = CMD_HELP
        user = bot.get_me()
        uid = user.id
        owner = user.first_name
        asst = tgbot.get_me()
        botusername = asst.username
        logo = ALIVE_LOGO
        kyylogo = INLINE_PIC
        cmd = CMD_HANDLER
        tgbotusername = BOT_USERNAME
        BTN_URL_REGEX = re.compile(
            r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)"
        )

        main_help_button = [
            [
                Button.inline("ᴍᴏᴅᴜʟᴇs 📚", data="reopen"),
                Button.inline("ᴠᴄ ᴍᴇɴᴜ 📎", data="skyla_inline"),
            ],
            [
                Button.url("sᴇᴛᴛɪɴɢs ⚙️", f"t.me/{botusername}"),
            ],
            [Button.inline("ʙᴀᴄᴋ", data="close")],
        ]

        @tgbot.on(events.NewMessage(incoming=True,
                  func=lambda e: e.is_private))
        async def bot_pms(event):
            chat = await event.get_chat()
            if check_is_black_list(chat.id):
                return
            if chat.id != uid:
                msg = await event.forward_to(uid)
                try:
                    add_user_to_db(
                        msg.id, get_display_name(chat), chat.id, event.id, 0, 0
                    )
                except Exception as e:
                    LOGS.error(str(e))
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            f"**ERROR:** Saat menyimpan detail pesan di database\n`{str(e)}`",
                        )
            else:
                if event.text.startswith("/"):
                    return
                reply_to = await reply_id(event)
                if reply_to is None:
                    return
                users = get_user_id(reply_to)
                if users is None:
                    return
                for usr in users:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    user_name = usr.first_name
                    break
                if user_id is not None:
                    try:
                        if event.media:
                            msg = await event.client.send_file(
                                user_id,
                                event.media,
                                caption=event.text,
                                reply_to=reply_msg,
                            )
                        else:
                            msg = await event.client.send_message(
                                user_id,
                                event.text,
                                reply_to=reply_msg,
                                link_preview=False,
                            )
                    except UserIsBlockedError:
                        return await event.reply(
                            "❌ **Bot ini diblokir oleh pengguna.**"
                        )
                    except Exception as e:
                        return await event.reply(f"**ERROR:** `{e}`")
                    try:
                        add_user_to_db(
                            reply_to,
                            user_name,
                            user_id,
                            reply_msg,
                            event.id,
                            msg.id)
                    except Exception as e:
                        LOGS.error(str(e))
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                f"**ERROR:** Saat menyimpan detail pesan di database\n`{e}`",
                            )

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"reopen")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                buttons = paginate_help(0, dugmeler, "helpme")
                text = f"**Skyla-Userbot ɪɴʟɪɴᴇ ᴍᴇɴᴜ**\n\n✣ **ᴏᴡɴᴇʀ** [{user.first_name}](tg://user?id={user.id})\n✣ **ᴊᴜᴍʟᴀʜ** `{len(dugmeler)}` **Modules**"
                await event.edit(
                    text,
                    file=kyylogo,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@SkylaChats"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = await event.builder.photo(
                    file=kyylogo,
                    link_preview=False,
                    text=f"**Skyla-Userbot ɪɴʟɪɴᴇ ᴍᴇɴᴜ**\n\n✣ **ᴏᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id})\n✣ **ᴊᴜᴍʟᴀʜ** `{len(dugmeler)}` **Modules**",
                    buttons=main_help_button,
                )
            elif query.startswith("repo"):
                result = builder.article(
                    title="Repository",
                    description="Repository Skyla-Userbot",
                    url="https://t.me/SkylaChats",
                    thumb=InputWebDocument(
                        INLINE_PIC,
                        0,
                        "image/jpeg",
                        []),
                    text="**Skyla-Userbot**\n➖➖➖➖➖➖➖➖➖➖\n✣ **ᴏᴡɴᴇʀ ʀᴇᴘᴏ :** [iky](https://t.me/)\n✣ **sᴜᴘᴘᴏʀᴛ :** @SkylaChats\n✣ **ʀᴇᴘᴏsɪᴛᴏʀʏ :** [Skyla-Userbot](https://github.com/Cangcimenn/Skyla-Userbot)\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url(
                                "ɢʀᴏᴜᴘ",
                                "https://t.me/SkylaChats"),
                            custom.Button.url(
                                "ʀᴇᴘᴏ",
                                "https://github.com/Cangcimenn/Skyla-Userbot"),
                        ],
                    ],
                    link_preview=False,
                )
            elif query.startswith("Inline buttons"):
                markdown_note = query[14:]
                prev = 0
                note_data = ""
                buttons = []
                for match in BTN_URL_REGEX.finditer(markdown_note):
                    n_escapes = 0
                    to_check = match.start(1) - 1
                    while to_check > 0 and markdown_note[to_check] == "\\":
                        n_escapes += 1
                        to_check -= 1
                    if n_escapes % 2 == 0:
                        buttons.append(
                            (match.group(2), match.group(3), bool(
                                match.group(4))))
                        note_data += markdown_note[prev: match.start(1)]
                        prev = match.end(1)
                    elif n_escapes % 2 == 1:
                        note_data += markdown_note[prev:to_check]
                        prev = match.start(1) - 1
                    else:
                        break
                else:
                    note_data += markdown_note[prev:]
                message_text = note_data.strip()
                tl_ib_buttons = ibuild_keyboard(buttons)
                result = builder.article(
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="Skyla-Userbot",
                    description="Skyla - Userbot | Telethon",
                    url="https://t.me/",
                    thumb=InputWebDocument(
                        INLINE_PIC,
                        0,
                        "image/jpeg",
                        []),
                    text=f"**Skyla-Userbot**\n➖➖➖➖➖➖➖➖➖➖\n✣ **ᴏᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id})\n✣ **ᴀssɪsᴛᴀɴᴛ:** {tgbotusername}\n➖➖➖➖➖➖➖➖➖➖\n**ᴜᴘᴅᴀᴛᴇs:** @\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url(
                                "ɢʀᴏᴜᴘ",
                                "https://t.me/SkylaChats"),
                            custom.Button.url(
                                "ʀᴇᴘᴏ",
                                "https://github.com/Cangcimenn/Skyla-Userbot"),
                        ],
                    ],
                    link_preview=False,
                )
            await event.answer(
                [result], switch_pm="👥 USERBOT PORTAL", switch_pm_param="start"
            )

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = (
                    f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:  # @Kyy-Userbot
                # https://t.me/TelethonChat/115200
                await event.edit(
                    file=kyylogo,
                    link_preview=True,
                    buttons=main_help_button)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"gcback")
            )
        )
        async def gback_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:  # @Kyy-Userbot
                # https://t.me/TelethonChat/115200
                text = (
                    f"**Skyla-Userbot ɪɴʟɪɴᴇ ᴍᴇɴᴜ**\n\n✣ **ᴏᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id})\n✣ **ᴊᴜᴍʟᴀʜ** `{len(dugmeler)}` **Modules**")
                await event.edit(
                    text,
                    file=kyylogo,
                    link_preview=True,
                    buttons=main_help_button)

        @tgbot.on(events.CallbackQuery(data=b"skyla_inline"))
        async def about(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                await event.edit(f"""
Voice chat group menu untuk {owner}
""",
                                 buttons=[
                                     [
                                         Button.inline("ᴠᴄ ᴘʟᴜɢɪɴ ⚙️",
                                                       data="vcplugin"),
                                         Button.inline("ᴠᴄ ᴛᴏᴏʟs ⚙️",
                                                       data="vctools")],
                                     [custom.Button.inline(
                                         "ʙᴀᴄᴋ", data="gcback")],
                                 ]
                                 )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"vcplugin")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"""
✘ **Commands available in vcplugin** ✘
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}play` <Judul Lagu/Link YT>
  ↳ : Untuk Memutar Lagu di voice chat group dengan akun kamu
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}vplay` <Judul Video/Link YT>
  ↳ : Untuk Memutar Video di voice chat group dengan akun kamu
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}end`
  ↳ : Untuk Memberhentikan video/lagu yang sedang putar di voice chat group
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}skip`
  ↳ : Untuk Melewati video/lagu yang sedang di putar
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}pause`
  ↳ : Untuk memberhentikan video/lagu yang sedang diputar
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}resume`
  ↳ : Untuk melanjutkan pemutaran video/lagu yang sedang diputar
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}volume` 1-200
  ↳ : Untuk mengubah volume (Membutuhkan Hak admin)
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}playlist`
  ↳ : Untuk menampilkan daftar putar Lagu/Video
""")
                await event.edit(
                    text,
                    file=kyylogo,
                    link_preview=True,
                    buttons=[Button.inline("ʙᴀᴄᴋ", data="skyla_inline")])
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"vctools")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"""
✘ **Commands available in vctools** ✘
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}startvc`
  ↳ : Untuk Memulai voice chat group
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}stopvc`
  ↳ : Untuk Memberhentikan voice chat group
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}vctitle` <title vcg>
  ↳ : Untuk Mengubah title/judul voice chat group
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}vcinvite`
  ↳ : Mengundang Member group ke voice chat group
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}joinvc`
  ↳ : Melakukan Fake voice chat group
  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `{cmd}leavevc`
  ↳ : Memberhentikan Fake voice chat group
""")
                await event.edit(
                    text,
                    file=kyylogo,
                    link_preview=True,
                    buttons=[Button.inline("ʙᴀᴄᴋ", data="skyla_inline")])
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            buttons = [
                (custom.Button.inline("ᴍᴀɪɴ ᴍᴇɴᴜ", data="gcback"),),
            ]
            await event.edit("**ᴍᴇɴᴜ ᴅɪᴛᴜᴛᴜᴘ!**", file=kyylogo, buttons=buttons)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_modul_(.*)")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 950:
                    help_string = (
                        str(CMD_HELP[modul_name])
                        .replace("`", "")
                        .replace("**", "")[:950]
                        + "..."
                        + "\n\nBaca Teks Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = (str(CMD_HELP[modul_name]).replace(
                        "`", "").replace("**", ""))

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} Tidak ada dokumen yang telah ditulis untuk modul.".format(
                        modul_name
                    )
                )
                await event.edit(
                    reply_pop_up_alert, buttons=[Button.inline("ʙᴀᴄᴋ", data="reopen")]
                )

            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "Help Mode Inline Bot Mu Tidak aktif. Tidak di aktifkan juga tidak apa-apa. "
            "Untuk Mengaktifkannya Buat bot di @BotFather Lalu Tambahkan var BOT_TOKEN dan BOT_USERNAME. "
            "Pergi Ke @BotFather lalu settings bot » Pilih mode inline » Turn On. ")
