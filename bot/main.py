import asyncio

from loguru import logger

from aiogram.dispatcher.dispatcher import Dispatcher

from bot.command.user import start
from bot.command.user import new_work, new_car, my_car, my_work, questions

from bot.states import work_state, new_car_state
from bot.loader.load import dp, bot

from bot.database import datab_model


async def on_startup(dispatcher: Dispatcher):
    logger.info('Bot on')

    dp.include_routers(start.router,
                       new_work.router,
                       my_car.router,
                       work_state.router,
                       new_car_state.router,
                       new_car.router,
                       my_work.router,
                       questions.router)

async def on_shutdown(dispatcher: Dispatcher):
    logger.info('Bot off')

@logger.catch
async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await datab_model.create_tables()

    await dp.start_polling(bot)


if __name__ == "__main__":    
    asyncio.run(main())