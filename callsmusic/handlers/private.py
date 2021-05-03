from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""This is my private music vc bot.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    
                    InlineKeyboardButton(
                        'Channel', url='https://t.me/lovemelikeyourfather',
                    ),
                ],
            ],
        ),
    )
