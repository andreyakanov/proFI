from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from loguru import logger
import json

from bot.data.config import TEXT_KB, PATH_QUESTIONS, SUPPORT
from bot.keyboards.reply import menu
from bot.states.work_state import NewWork

router = Router()

@router.message(F.text)
@logger.catch
async def cmd_new_customer(message: Message, state: FSMContext):
    await state.clear()

    with open(PATH_QUESTIONS, 'r') as file:
        questions = json.load(file)

    try:
       await message.answer(questions[message.text]) 
    except KeyError:
        await message.answer(f'Напишите менеджеру, чтобы узнать ответ на вопрос @{SUPPORT[0]}')