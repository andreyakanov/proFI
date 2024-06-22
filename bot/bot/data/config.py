import configparser
import os

import os.path

# Пути до файлов
PATH_LOGS = os.path.abspath('bot/data/logs/log.log')
PATH_DATABASE = os.path.abspath('bot/data/database.db')
PATH_SETTINGS = os.path.abspath('settings.ini')

PATH_TOKENS = os.path.abspath('bot/data/tokens')
PATH_CREDENTIALS = os.path.abspath('bot/data/credentials.json')
PATH_DATABASE = os.path.abspath('bot/data/database.db')
PATH_QUESTIONS = os.path.abspath('bot/data/questions.json')

read_config = configparser.ConfigParser()
read_config.read(PATH_SETTINGS)

# Переменные из настроек
ADMINS = read_config['settings']['admins'].strip().split(' ') # админы
TOKEN = read_config['settings']['token'] # Токен бота
BOT_VERSION = read_config['settings']['bot_version'] # Версия бота
SUPPORT = read_config['settings']['support'].strip().split(' ') # админы

TEXT_KB = {
    'start' : '🔁 Перезапуск',
    'new_work' : '🔧 Запись на прием',
    'menu' : '🏠 Главное меню',
    'new_car' : '🚙 Новая машина',
    'my_car' : '🚗 Автомобили',
    'my_work' : '📄 Заявки',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
}

TEXT = {
    'yes' : '✅ Да',
    'no' : '❌ Нет',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
    # '' : '',
}