from projects import app
from pyrogram import filters
import asyncio
from pyrogram.types import ReplyKeyboardRemove
from .start import start_command

def check_if_on_whatsapp(number):
    return int(number[-1]) % 2 == 0

@app.on_message(filters.regex("Check WhatsApp Status"))
async def check_whatsapp_status_ask(client, message):
    try:
        response = await client.ask(chat_id=message.chat.id,text="Please provide a list of numbers to check, separated by spaces.", timeout=60)
        numbers_list = response.text.split()
        result = ""
        not_on_whatsapp_count = 0
        for number in numbers_list:
            await asyncio.sleep(0.1)
            if check_if_on_whatsapp(number):
                result += f"✅ `{number}` is on WhatsApp\n"
            else:
                result += f"❌ `{number}` is NOT on WhatsApp\n"
                not_on_whatsapp_count += 1
        result += f"\nSaved {not_on_whatsapp_count} not-registered numbers."
        await response.reply_text(result)
        await start_command(client, message)
    except asyncio.TimeoutError:
        await message.reply_text("You took too long to reply. Please try again.")
