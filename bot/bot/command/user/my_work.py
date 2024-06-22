from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from loguru import logger

from bot.data.config import TEXT_KB
from bot.database import select_db


router = Router()

@router.message(F.text == TEXT_KB['my_work'])
@router.message(F.text == '/my_work')
@logger.catch
async def cmd_my_work(message: Message, state: FSMContext):
    await state.clear()

    works = await select_db.select_works_user(message.from_user.id)

    text = "Ваши заявки\n\n"
    for work in works:
        text += f"Id: {work.car_id}\n" + \
                f"Номер авто: {work.car_id}\n" + \
                f"Время записи: {work.time}\n" + \
                f"Дата записи: {work.date}\n" + \
                f"Описание: {work.description}\n\n"
        
    await message.answer(text)

