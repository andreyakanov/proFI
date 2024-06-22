from aiogram.types import ReplyKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from bot.data.config import ADMINS, TEXT_KB

def main_kb(message: Message) -> ReplyKeyboardMarkup:
    if str(message.from_user.id) in ADMINS:
        kb = ReplyKeyboardBuilder()
        kb.button(text=TEXT_KB['start'])
        kb.button(text=TEXT_KB['new_work'])
        kb.button(text=TEXT_KB['new_car'])
        kb.button(text=TEXT_KB['my_car'])
        kb.button(text=TEXT_KB['my_work'])
        kb.adjust(2)
        return kb.as_markup(resize_keyboard=True)
    
def menu(message: Message) -> ReplyKeyboardMarkup:
    if str(message.from_user.id) in ADMINS:
        kb = ReplyKeyboardBuilder()
        kb.button(text=TEXT_KB['menu'])
        return kb.as_markup(resize_keyboard=True)
    
def yes_no_kb(message: Message) -> ReplyKeyboardMarkup:
    if str(message.from_user.id) in ADMINS:
        kb = ReplyKeyboardBuilder()
        kb.button(text='✅ Да')
        kb.button(text='❌ Нет')
        return kb.as_markup(resize_keyboard=True)
    
def three(message: Message) -> ReplyKeyboardMarkup:
    if str(message.from_user.id) in ADMINS:
        kb = ReplyKeyboardBuilder()
        kb.button(text='💵 Наличный')
        kb.button(text='💳 Безналичный')
        kb.button(text='📦 Материал')
        return kb.as_markup(resize_keyboard=True)