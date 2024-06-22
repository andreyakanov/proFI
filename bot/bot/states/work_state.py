from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from aiogram.types import Message

from loguru import logger

from bot.keyboards.reply import yes_no_kb, main_kb, three, menu
from bot.data.config import TEXT_KB, TEXT

from bot.loader.load import bot

from bot.database import insert_db
import re

router = Router()

class NewWork(StatesGroup):
    description = State()
    numberCar = State()
    time = State()
    date = State()

@router.message(NewWork.description)
@logger.catch
async def description(message: Message, state: FSMContext) -> None:
    await message.answer("Напишите номер авто, которое хотите записать")
    await state.update_data(description=message.text)
    await state.set_state(NewWork.numberCar)

@router.message(NewWork.numberCar)
@logger.catch
async def description(message: Message, state: FSMContext) -> None:
    await message.answer("Напишите время в формате чч:мм, когда вам удобно записаться на прием")
    await state.update_data(numberCar=message.text)
    await state.set_state(NewWork.time)

@router.message(NewWork.time)
@logger.catch
async def time(message: Message, state: FSMContext) -> None:
    if bool(re.match("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", message.text)):
        await message.answer("Напишите дату в формате дд.мм.гггг, когда вам удобно записаться на прием")
        await state.update_data(time=message.text)
        await state.set_state(NewWork.date)
    else:
        await message.answer("Напишите время в формате чч:мм")

@router.message(NewWork.date)
@logger.catch
async def date(message: Message, state: FSMContext) -> None:
    if bool(re.match("^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$", message.text)):
        await state.update_data(date=message.text)

        data = await state.get_data()

        description = data['description']
        numberCar = data['numberCar']
        time = data['time']
        date = data['date']

        await insert_db.insert_work(numberCar, time, date, description, message.from_user.id)
        await state.clear()
        await message.answer("Запись успешно создана!", reply_markup=main_kb(message))

    else:
        await message.answer("Напишите дату в формате дд.мм.гггг")