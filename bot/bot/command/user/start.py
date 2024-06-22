from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from loguru import logger

from bot.data.config import TEXT_KB
from bot.keyboards.reply import main_kb

from bot.database import select_db, insert_db

router = Router()

@router.message(F.text == TEXT_KB['start'])
@router.message(F.text == TEXT_KB['menu'])
@router.message(F.text == '/start')
@logger.catch
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()

    if await select_db.select_user(message.from_user.id) is None:
        await insert_db.insert_user(message.from_user.id, message.from_user.username, message.from_user.full_name)

    text = """
Здравствуйте! 👋 Добро пожаловать в автосервис "Профи"!

Мы рады предложить вам широкий спектр услуг по обслуживанию и ремонту вашего автомобиля. С нашим ботом вы можете легко и быстро:

📅 Записаться на сервис
🛠 Получить консультацию и ответы на интересующие вас вопросы

Для начала выберите нужный пункт меню или введите ваш вопрос. Если вам потребуется помощь, наша команда всегда готова вам помочь!

Спасибо, что выбрали нас. Желаем вам хорошего дня и безопасных дорог! 🚗💨
    """

    await message.answer(text, reply_markup=main_kb(message))