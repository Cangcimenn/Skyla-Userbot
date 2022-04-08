
from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot




async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/b2dc33fdd56e3b58ee9c0.jpg",
                caption="⚡ **Skyla UserBot Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 1.1.5@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @SkylaChats ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/SkylaChats"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
