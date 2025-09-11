from projects import app
from pyrogram import filters
from .separate_numbers import show_options_reply
from .whatsapp import check_whatsapp_status_ask
from .generate_emails import ask_for_email_details_reply

@app.on_message(filters.regex(r"^(Separate Numbers|Check WhatsApp Status|Generate Emails)$"))
async def main_menu_handler(client, message):
    text = message.text
    if text == "Separate Numbers":
        await show_options_reply(client, message)
    elif text == "Check WhatsApp Status":
        await check_whatsapp_status_ask(client, message)
    elif text == "Generate Emails":
        await ask_for_email_details_reply(client, message)
