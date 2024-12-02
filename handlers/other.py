import logging

from aiogram import Router
from aiogram.types import Message

from filters.filters import MyTrueFilter
from lexicon.lexicon import LEXICON_RU

logger = logging.getLogger(__name__)

other_router = Router()

@other_router.message(MyTrueFilter())
async def send_echo(message: Message):
    logger.debug("Вошли в эхо хендлер")
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU["no_echo"])

    logger.debug("Выходим из эхо хендлера")
