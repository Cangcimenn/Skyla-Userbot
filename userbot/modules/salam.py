from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.pe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐬𝐬𝐚𝐥𝐚𝐦𝐮'𝐚𝐥𝐚𝐢𝐤𝐮𝐦...")


@register(outgoing=True, pattern='^.atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇....SAYANG!!!!")


@register(outgoing=True, pattern='^.wa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐖𝐚'𝐚𝐥𝐚𝐢𝐤𝐮𝐦𝐬𝐚𝐥𝐚𝐦...")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇......")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("BISMILLAH SLEEPCALL...😁")


@register(outgoing=True, pattern='^D(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("BISMILLAH DAPET KAMU..")


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


@register(outgoing=True, pattern="^.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


@register(outgoing=True, pattern="^.perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`𝙃𝙖𝙞 𝙂𝙪𝙮𝙨 , 𝙋𝙚𝙧𝙠𝙚𝙣𝙖𝙡𝙠𝙖𝙣 𝙉𝙖𝙢𝙖 𝙂𝙬 {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`𝙂𝙬 𝙏𝙞𝙣𝙜𝙜𝙖𝙡 𝘿𝙞 {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`𝙎𝙖𝙡𝙖𝙢 𝙆𝙚𝙣𝙖𝙡...`")
    sleep(2)
    await event.edit("`𝙐𝙙𝙖𝙝 𝙂𝙞𝙩𝙪 𝘼𝙟𝙖 :𝙫`")


CMD_HELP.update({
    "salam":
    ".pe\
\nUsage: Untuk Memberi salam.\
\n\n.wa\
\nUsage: Untuk Menjawab Salam.\
\n\nS\
\nUsage: Cari Sleepcall.\
\n\nD\
\nUsage: Dapet Kamu.\
\n\n.p\
\nUsage: Memberi Salam Arab.\
\n\n.l\
\nUsage: Menjawab Salam Arab"
})


CMD_HELP.update({
    "salam2":
    ".atg\
\nUsage: Istighfar 1.\
\n\n.ast\
\nUsage: Istighfaf 2.\
\n\n.istigfar\
\nUsage: Istighfaf Arab.\
\n\n.perkenalan\
\nUsage: Untuk Memperkenalkan"
})
