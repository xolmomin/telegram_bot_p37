# import asyncio
#
# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command, CommandStart
# from aiogram.types import Message, InputFile, FSInputFile
#
# TOKEN = '8359753576:AAHeVGWO71W5Pk2V77IfdbZY3Fs5_pKh8e0'
#
# dp = Dispatcher()
# # @p37_group_bot
# ADMIN_ID = 514411336
#
#
# @dp.message(CommandStart())
# async def command_start_handler(message: Message, bot: Bot) -> None:
#     # text = f"{message.from_user.id}\nXabar: {message.text}"
#     # await bot.send_message(ADMIN_ID, text)
#     await bot.send_document(message.from_user.id, FSInputFile('main.py', 'darslik.py'))
#     await bot.send_document(message.from_user.id, "https://daryo.uz/image/960x540?url=https%3A%2F%2Fdata.daryo.uz%2Fmedia%2F2026%2F02%2F17%2F1771317135608463862_960X540%20UZ.jpg")
#     await bot.send_photo(message.from_user.id, "https://daryo.uz/image/960x540?url=https%3A%2F%2Fdata.daryo.uz%2Fmedia%2F2026%2F02%2F17%2F1771317135608463862_960X540%20UZ.jpg")
#     # await message.answer("Adminga yuborildi")
#
#
# @dp.message()
# async def command_start_handler(message: Message, bot: Bot) -> None:
#     file_id = message.document.file_id
#     print(message.content_type)
#     file = await bot.get_file(file_id)
#     await bot.download(file, message.document.file_name)
#     await message.answer("Adminga yuborildi")
#
#
# async def main() -> None:
#     bot = Bot(token=TOKEN)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
import logging
import sys
from pathlib import Path

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ContentType
from aiogram.filters import CommandStart
from aiogram.types import Message, InputPollOption, InputFile, FSInputFile, URLInputFile

TOKEN = '8359753576:AAHeVGWO71W5Pk2V77IfdbZY3Fs5_pKh8e0'

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    await message.answer_dice()
    # message.answer_poll()
    # message.answer_photo()
    # await message.answer_location(41.227806, 69.236273)
    # await message.answer_contact("+998919222345", "Ali")
    # options = [
    #     InputPollOption(text="Ha"),
    #     InputPollOption(text="Yuq")
    # ]
    # await message.answer_poll("dars buladimi?", options=options)
    # await message.answer_document(FSInputFile('main.py'))
    # await message.answer_audio(FSInputFile('main.py'))
    # await message.answer_audio(URLInputFile('https://uzhits.net/uploads/files/2026-02/ziyoda-kora-olmaysiz_(uzhits.net).mp3', filename='zor qoshiq.mp3'))
    # await message.answer_audio('https://uzhits.net/uploads/files/2026-02/ziyoda-kora-olmaysiz_(uzhits.net).mp3', caption="nimadir")
    # message.answer_media_group()
    # message.answer_paid_media()


    # await message.answer_game('MathBattle')
    # bot.send_contact()
    # bot.send_poll(message.from_user.id)
    # options = [
    #     InputPollOption(text="aniqmas"),
    #     InputPollOption(text="borolmayman"),
    #     InputPollOption(text="boraman"),
    #     InputPollOption(text="qoshilmayman"),
    # ]
    # await message.answer_poll("Ertaga dars bo'ladimi?", options, protect_content=True)

    # await bot.send(message.chat.id, f"Hello, {message.from_user.full_name}!")
    # await message.answer(f"Hello, {message.from_user.full_name}!")


@dp.message(lambda msg: msg.content_type == ContentType.PHOTO)
async def photo_handler(message: Message) -> None:
    await message.answer('rasm keldi')


@dp.message(lambda msg: msg.content_type == ContentType.DOCUMENT)
async def document_handler(message: Message) -> None:
    await message.answer('document keldi')

@dp.message()
async def document_handler(message: Message) -> None:
    message
    await message.answer('document keldi')


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
