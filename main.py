from cgitb import text
import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
import imp
from aiogram.types import Message, InputFile, ContentType
from textbuttons import menu
from aiogram.dispatcher.filters import Command

bot_token = '5708786701:AAEHKh-U9XA5e4uO4uUkwbaRoQP8m-g8ns0'
admin_id = '1472714490'


loop = asyncio.get_event_loop()
bot = Bot(bot_token, parse_mode="HTML")
dp = Dispatcher(bot, loop)
@dp.message_handler(Command("start"))
async def send_on_start(message: Message):
    await message.answer("Здравствуй!")
                

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Меню: ничего здесь нет")
    
@dp.message_handler(text="Кнопка 1")
async def hide_menu(message: Message):
    #photo_byte = InputFile(path_or_bytesio='img/hi.jpg')
    #await bot.send_photo(chat_id=message.from_user.id, photo=photo_byte)
    await bot.send_message(chat_id=message.from_user.id, text="Внимание! Вы выбраны Гражданской Ассоциацией Восстановления Независимости Эльфов и теперь получите приз в 100 * (47 - (1055-1008)) галлеон!")



async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="<b>Бот запущен!</b>")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=send_to_admin)