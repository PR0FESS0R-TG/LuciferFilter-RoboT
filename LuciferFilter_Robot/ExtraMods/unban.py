from pyrogram import Client, filters
from LuciferFilter_Robot.helper.admin_check import admin_check
from LuciferFilter_Robot.helper.extract import extract_time, extract_user                               


@Client.on_message(filters.command(["unban", "unmute"]))
async def un_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return
    user_id, user_first_name = extract_user(message)
    try:
        await message.chat.unban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Okay, Changed now...."
                f"{user_first_name} To"
                "You Can Join The Group..!"
            )
        else:
            await message.reply_text(
                "Okay, Changed Now...."
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a> To "
                "You Can Join The Group..!"
            )
