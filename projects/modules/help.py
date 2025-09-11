# -----------CREDITS -----------
# telegram : @itz_legendcoder
# github : noob-mukesh
from projects import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove)
# New handler for the "Back" button
@app.on_message(filters.regex("Back"))
async def back_button_handler(client, message):
    await start_command(client, message)

# Handler for ReplyKeyboardMarkup buttons from the start command
@app.on_message(filters.regex(r"^(Separate Numbers|Check WhatsApp Status|Generate Emails)$"))
async def main_menu_handler(client, message):
    text = message.text
    if text == "Separate Numbers":
        await show_options_reply(client, message)
    elif text == "Check WhatsApp Status":
        await check_whatsapp_status_ask(client, message)
    elif text == "Generate Emails":
        await ask_for_email_details_reply(client, message)
