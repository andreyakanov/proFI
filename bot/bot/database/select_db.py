from sqlalchemy.orm import sessionmaker, Query

from loguru import logger

from bot.loader.load import engine
from bot.database import datab_model


@logger.catch
async def select_user(user_id: int):
    session = sessionmaker(bind=engine)
    with session() as s:
        user = s.query(datab_model.Users).filter(datab_model.Users.user_id == user_id).first()
    session.close_all()
    return user

@logger.catch
async def select_users():
    session = sessionmaker(bind=engine)
    with session() as s:
        users = s.query(datab_model.Users)
    session.close_all()
    return users

@logger.catch
async def select_cars_user(user_id: int):
    session = sessionmaker(bind=engine)
    with session() as s:
        cars = s.query(datab_model.Cars).filter(datab_model.Cars.user_id == user_id).all()
    session.close_all()
    return cars

@logger.catch
async def select_works_user(user_id: int):
    session = sessionmaker(bind=engine)
    with session() as s:
        cars = s.query(datab_model.Works).filter(datab_model.Works.user_id == user_id).all()
    session.close_all()
    return cars