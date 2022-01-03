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
        photo=f"https://telegra.ph/file/9155c4436e60c2d8523d3.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs 𝙼𝚈 𝙲𝚁𝙴𝙰𝚃𝙴𝚁 𝙱𝙷𝙰𝚃𝙰𝙺𝚃𝙸_𝙰𝚃𝙼𝙰 𝙷𝙰𝚃𝙴𝚁,𝚂 𝙲𝙰𝙻𝙻 𝙼𝙴 𝙳𝙰𝙳 ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [𝙱𝙷𝙰𝚃𝙰𝙺𝚃𝙸_𝙰𝚃𝙼𝙰 ʜᴀʟᴅᴇʀ](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK)
┣★ ᴜᴘᴅᴀᴛᴇs : [𝙱𝙷𝙰𝚃𝙰𝙺𝚃𝙸 sᴇʀᴠᴇʀ](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK)
┣★ sᴜᴘᴘᴏʀᴛ : [𝙱𝙷𝙰𝚃𝙰𝙺𝚃𝙸 ᴅɪsᴄᴜs](https://t.me/ABOUT_BHATAKTI)
┣★ sᴏᴜʀᴄᴇ › : [ɢᴇᴛ ʀᴇᴘᴏ ʜᴇʀᴇ](https://t.me/ABOUT_BHATAKTI/175)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ 𝚈𝙾𝚄 𝙰𝙽𝚈 𝚀𝚄𝙴𝚂𝚃𝙸𝙾𝙽 𝙳𝙼 𝚃𝙾 𝙼𝚈 𝙾𝚆𝙽𝙴𝚁 𝙱𝙷𝙰𝚃𝙰𝙺𝚃𝙸_𝙰𝚃𝙼𝙰🤓
👉 𝚈𝙾𝚄𝚁 𝙳𝙰𝙳 [ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴊᴏɪɴ ʜᴇʀᴇ ғᴏʀ ᴜᴘᴅᴀᴛᴇs ❱ ➕", url=f"https://t.me/ABOUT_BHATAKTI")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "𝙱𝙷𝙰𝚃𝙰𝙺𝚃𝙸_𝙰𝚃𝙼𝙰 "]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d050c171dd9c5c96ec24b.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 💞", url=f"https://t.me/ABOUT_BHATAKTI")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d050c171dd9c5c96ec24b.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 💞", url=f"https://t.me/ABOUT_BHATAKTI/175")
                ]
            ]
        ),
    )
