from pyrogram import filters
from pyrogram.types import Message

from Shigaraki import app
from Shigaraki.core.call import Shigaraki
from Shigaraki.utils.database import is_music_playing, music_off
from Shigaraki.utils.decorators import AdminRightsCheck
from Shigaraki.utils.inline import close_markup
from config import filter


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~filter)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Shigaraki.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
