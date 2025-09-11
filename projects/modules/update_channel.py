from projects import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import UPDATE_CHNL
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

@app.on_message(filters.incoming & filters.private, group=-1)
async def UPDATE_CHNL_channel(bot, msg: Message):
    if not UPDATE_CHNL:
        return
    try:
        try:
            await bot.get_chat_member(UPDATE_CHNL, msg.from_user.id)
        except UserNotParticipant:
            if UPDATE_CHNL.isalpha():
                link = "https://t.me/" + UPDATE_CHNL
            else:
                chat_info = await bot.get_chat(UPDATE_CHNL)
                link = chat_info.invite_link
            try:
                await msg.delete()
                await msg.reply(f"Hey @{msg.from_user.username} ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ  [ᴛʜɪs ᴄʜᴀɴɴᴇʟ]({link}) ᴛᴏ ᴜsᴇ ᴍᴇ. Aғᴛᴇʀ ᴊᴏɪɴɢ ᴛʀʏ ᴀɢᴀɪɴ /start or /help!",disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ UPDATE_CHNL ᴄʜᴀᴛ : {UPDATE_CHNL} !")
