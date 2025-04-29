import os
import random
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from TEAMZYRO import app
from config import OWNER_USERNAME, LOGGER_ID, SUPPORT_CHANNEL, SUPPORT_CHAT 
from TEAMZYRO.utils.formatters import get_readable_time
from TEAMZYRO.utils.inline import help_pannel, private_panel, start_panel

NEXI_VID = [
    "https://envs.sh/I8B.mp4",
    "https://envs.sh/I8B.mp4",
    "https://envs.sh/I8B.mp4"
]

START_TIME = time.time()

@app.on_callback_query(filters.regex("^host$"))
async def show_management_help_menu(client, query: CallbackQuery):
    time.sleep(0.5)
    
    buttons = [
        [InlineKeyboardButton("⬅ Back", callback_data="mbot_cb")]
    ]

    await query.message.edit_text(
        """✨ Bᴏᴛ Hᴏsᴛɪɴɢ Aᴠᴀɪʟᴀʙʟᴇ!

➡️Wᴀɪғᴜ – ₹𝟻𝟶𝟶/ᴍᴏɴᴛʜ 
➡️Mᴜsɪᴄ – ₹𝟸𝟶𝟶/ᴍᴏɴᴛʜ 
➡️Fɪʟᴇ Sʜᴀʀᴇ – ₹𝟷𝟶𝟶/ᴍᴏɴᴛʜ 
➡️Fɪʟᴇ Rᴇɴᴀᴍᴇ – ₹𝟷𝟶𝟶/ᴍᴏɴᴛʜ 
➡️Mᴀɴᴀɢᴇᴍᴇɴᴛ – ₹𝟽𝟻𝟶/ᴍᴏɴᴛʜ
➡️Mᴜsɪᴄ + 𝟹𝟻% Mᴀɴᴀɢᴇᴍᴇɴᴛ – ₹𝟹𝟻𝟶/ᴍᴏɴᴛʜ

➡️Sᴘᴀᴍ Bᴏᴛ – ₹𝟷𝟶𝟶/ᴍᴏɴᴛʜ
➡️Cʜᴀᴛ Bᴏᴛ – ₹𝟷𝟶𝟶/ᴍᴏɴᴛʜ

➡️AI Bᴏᴛ – (Cᴏᴍɪɴɢ Sᴏᴏɴ)

➡️Usᴇʀʙᴏᴛ - (Cᴏᴍɪɴɢ Sᴏᴏɴ)
➡️Usᴇʀ Cʜᴀᴛ Bᴏᴛ - (Cᴏᴍɪɴɢ Sᴏᴏɴ)

🌐 𝟸𝟺/𝟽 Sᴜᴘᴘᴏʀᴛ
❤️DM - @Sukuna_dev
❤️DM - @xeno_kakarot""",
       reply_markup=InlineKeyboardMarkup(buttons)
    )


