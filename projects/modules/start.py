# -----------CREDITS -----------
# telegram : @itz_legendcoder
# github : noob-mukesh

from projects import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove)
from config import UPDATE_CHNL

# Import all handlers
from .allcode import *


@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "Hello! I'm a bot that can help with various tasks. Please select an option from the keyboard below:",
        reply_markup=ReplyKeyboardMarkup(
            [
                [KeyboardButton("Separate Numbers"), KeyboardButton("Check WhatsApp Status")],
                [KeyboardButton("Generate Emails")],
            ],
            resize_keyboard=True,
            one_time_keyboard=False 
        )
    )
