from projects import app
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import re
from .start import start_command

@app.on_message(filters.regex("Separate Numbers"))
async def show_options_reply(client: Client, message):
    await message.reply_text(
        "What would you like to do with the numbers?",
        reply_markup=ReplyKeyboardMarkup(
            [
                [KeyboardButton("Add +"), KeyboardButton("Add Link")],
                [KeyboardButton("Filter Prefix")],
                [KeyboardButton("Back")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

@app.on_message(filters.regex(r"^(Add \+|Add Link|Filter Prefix)$"))
async def handle_reply_button(client: Client, message):
    action_text = message.text.lower().replace(" ", "_")
    try:
        response = await client.ask(chat_id=message.chat.id,text="Please send me the text containing the numbers you want to process.", timeout=60)
        numbers = re.findall(r'\b\d{10,}\b', response.text)
        if not numbers:
            await response.reply_text("No numbers found in the provided text.")
            return
        new_text = ""
        if "add_+" in action_text:
            new_text = "\n".join([f"+{num}" for num in numbers])
        elif "add_link" in action_text:
            new_text = "\n".join([f"https://t.me/{num}" for num in numbers])
        elif "filter_prefix" in action_text:
            new_text = "\n".join([num for num in numbers if num.startswith('5917')])
        await response.reply_text(f"**Updated Numbers:**\n{new_text}")
        await start_command(client, message)
    except asyncio.TimeoutError:
        await message.reply_text("You took too long to reply. Please try again.")
