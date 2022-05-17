import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/46247f00eecfb587117c0.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
˚₊· ͟͟͞͞➳❥ ʜᴇʟʟᴏ, ɪ ᴀᴍ ᴀʟɪsʜᴀ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [𝗦Aʜᴀʟᴀᴍ](https://t.me/OPSAHALAM88)
┣★ ᴄʀᴇᴀᴛᴏʀ : [𝗩Iʀ]    (https://t.me/ITZVIR99)
┣★ ᴜᴘᴅᴀᴛᴇs : [𝗦ᴜᴘᴘᴏʀᴛ 𝗖ʜᴀɴɴᴇʟ](https://t.me/OPVIRSUPPORT)
┣★ sᴜᴘᴘᴏʀᴛ : [Aʟɪsʜᴀ Cʜᴀᴛ](https://t.me/Shayri_Music_Lovers)
┗━━━━━━━━━━━━━━━━━┛

・❥・Iғ Yᴏᴜ Hᴀᴠᴇ Aɴʏ Dᴏᴜʙᴛs Tʜᴇɴ Jᴏɪɴ Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ Aɴᴅ Rᴇᴘᴏʀᴛ Tᴏ Aᴅᴍɪɴs
🕊.⋆Sᴜᴘᴘᴏʀᴛ・❥・ (https://t.me/OPVIRSUPPORT) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴊᴏɪɴ ʜᴇʀᴇ ғᴏʀ ᴜᴘᴅᴀᴛᴇs ❱ ➕", url=f"https://t.me/OPVIRSUPPORT")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "OPVIRMUSIC"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "・❥・ ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 🕊.⋆", url=f"https://t.me/Shayri_Music_Lovers")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b69ed5a82792d310b841e.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "・❥・ ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 🕊.⋆", url=f"https://github.com/OPSAHALAM22/SAHALAMVIRXMUSIC")
                ]
            ]
        ),
    )
