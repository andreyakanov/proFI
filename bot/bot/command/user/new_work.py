from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from loguru import logger

# from bot.command.midleware.is_admin import IsAdmin
from bot.data.config import TEXT_KB
from bot.keyboards.reply import menu
from bot.states.work_state import NewWork
from bot.database import select_db

router = Router()
# router.message.middleware(IsAdmin())

@router.message(F.text == TEXT_KB['new_work'])
@router.message(F.text == '/new_work')
@logger.catch
async def cmd_new_work(message: Message, state: FSMContext):
    await state.clear()
    if await select_db.select_cars_user(message.from_user.id) == []:
        await message.answer("Перед тем как создать заявку, нужно добавить данные об автомобиле.")
        return
    await state.set_state(NewWork.description)
    await message.answer("Опишите поломку в автомобиле", reply_markup=menu(message))