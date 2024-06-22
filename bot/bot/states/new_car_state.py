from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from aiogram.types import Message

from loguru import logger

from bot.keyboards.reply import main_kb

from bot.database import insert_db

router = Router()

class NewCar(StatesGroup):
    brend = State()
    model = State()
    number = State()
    color = State()

@router.message(NewCar.brend)
@logger.catch
async def brend(message: Message, state: FSMContext) -> None:
    await message.answer("Напишите модель вашей машины")
    await state.update_data(brend=message.text)
    await state.set_state(NewCar.model)

@router.message(NewCar.model)
@logger.catch
async def model(message: Message, state: FSMContext) -> None:
    await message.answer("Напишите номер вашей машины")
    await state.update_data(model=message.text)
    await state.set_state(NewCar.number)

@router.message(NewCar.number)
@logger.catch
async def number(message: Message, state: FSMContext) -> None:
    await message.answer("Напишите цвет вашей машины")
    await state.update_data(number=message.text)
    await state.set_state(NewCar.color)

@router.message(NewCar.color)
@logger.catch
async def color(message: Message, state: FSMContext) -> None:
    await state.update_data(color=message.text)

    data = await state.get_data()

    brend = data['brend']
    model = data['model']
    number = data['number']
    color = data['color']

    logger.debug(number)

    await insert_db.insert_car(brend, model, number, color, message.from_user.id)

    await message.answer('Машина успешно добавлена!', reply_markup=main_kb(message))

    await state.clear()
    

