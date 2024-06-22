from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from loguru import logger

from bot.data.config import TEXT_KB
from bot.keyboards.reply import menu
from bot.states.new_car_state import NewCar

router = Router()

@router.message(F.text == TEXT_KB['new_car'])
@router.message(F.text == '/new_car')
@logger.catch
async def cmd_new_car(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(NewCar.brend)
    await message.answer("Введите бренд машины", reply_markup=menu(message))