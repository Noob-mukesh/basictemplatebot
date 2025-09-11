from projects import app
from .start import start_command
from pyrogram import filters

@app.on_message(filters.regex("Back"))
async def back_button_handler(client, message):
    await start_command(client, message)
