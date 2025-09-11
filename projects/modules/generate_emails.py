from projects import app
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from .start import start_command
import asyncio

@app.on_message(filters.regex("Generate Emails"))
async def ask_for_email_details_reply(client: Client, message):
    try:
        email_response = await client.ask(chat_id=message.chat.id, text="Please send me the base email address (e.g., username@domain.com).", reply_markup=ReplyKeyboardRemove())
        base_email = email_response.text
        await message.reply_text(
            "How many emails would you like to generate?",
            reply_markup=ReplyKeyboardMarkup(
                [
                    [KeyboardButton("20"), KeyboardButton("50"), KeyboardButton("100")],
                    [KeyboardButton("Back")]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )
        amount_response = await client.ask(chat_id=message.chat.id,text="click on button 20|50|100|Back", filters=filters.regex("^(20|50|100|Back)$"), timeout=60)
        if amount_response.text == "Back":
            await start_command(client, amount_response)
            return
        amount = int(amount_response.text)
        await send_emails(client, amount_response, base_email, amount)
    except asyncio.TimeoutError:
        await message.reply_text("You took too long to reply. Please try again.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")

async def send_emails(client, message, base_email, amount):
    await message.reply_text("Generating emails...", reply_markup=ReplyKeyboardRemove())
    if '@' not in base_email:
        await message.reply_text("Invalid email format. Please include a '@'.")
        return
    username, domain = base_email.split('@', 1)
    case_combinations = set()
    for i in range(1 << len(username)):
        new_username = ""
        for j in range(len(username)):
            if (i >> j) & 1:
                new_username += username[j].upper()
            else:
                new_username += username[j].lower()
        case_combinations.add(new_username)
    generated_emails = []
    for combo in case_combinations:
        if len(generated_emails) >= amount:
            break
        generated_emails.append(f"{combo}@{domain}")
    emails_text = "\n".join(generated_emails)
    await message.reply_text(f"**Result:**\n{emails_text}")
    await start_command(client, message)
