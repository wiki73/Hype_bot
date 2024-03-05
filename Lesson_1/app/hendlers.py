from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from Lesson_1.app.keyboards import main

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет', reply_markup=main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Это команда  help')


@router.message(F.text == "Как дела?")
async def h_a_y(message: Message):
    await  message.answer('Ок')
