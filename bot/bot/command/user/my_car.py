from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from loguru import logger

from bot.data.config import TEXT_KB
from bot.database import select_db


router = Router()

@router.message(F.text == TEXT_KB['my_car'])
@router.message(F.text == '/my_car')
@logger.catch
async def cmd_my_car(message: Message, state: FSMContext):
    await state.clear()

    cars = await select_db.select_cars_user(message.from_user.id)

    text = "Ваши автомобили\n\n"
    for car in cars:
        text += f"Id: {car.car_id}\n" + \
                f"Бренд: {car.brend}\n" + \
                f"Модель: {car.model}\n" + \
                f"Номер: {car.number}\n" + \
                f"Цвет: {car.color}\n\n"
        
    await message.answer(text)

