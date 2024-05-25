from aiogram import Bot, Dispatcher,executor, types
import logging
from downloader import YouTubeDownloader, PlayOnYouTube
import os

logging.basicConfig(level=logging.INFO)

bot = Bot("5904607271:AAH-edy50mxak7BhgfeCB-9oLnlrK5QMPiM")
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")

@dp.message_handler()
async def func(message: types.Message):
    await message.answer("Musiqa qidirilmoqda...")
    search = PlayOnYouTube(message.text)
    YouTubeDownloader(search)
    with open("audio.mp3", "rb") as audio:
        await message.answer_audio(audio=audio)
    os.remove("audio.mp3")


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=False)