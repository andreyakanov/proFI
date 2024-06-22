from sqlalchemy.orm import sessionmaker

from loguru import logger
from datetime import datetime

from bot.loader.load import engine
from bot.database import datab_model


@logger.catch
async def insert_user(user_id: int, user_tag: str, user_name: str):
    session = sessionmaker(bind=engine)
    with session() as s:
        cheque = datab_model.Users(user_id=user_id, user_tag=user_tag, user_name=user_name, date_create=datetime.now())
        try:
            s.add(cheque)
            s.commit()
            return True
        except Exception as e:
            logger.error(str(e))
            return None
        finally:
            session.close_all()

@logger.catch
async def insert_car(brend: str, model: str, number: str, color: str, user_id: int):
    session = sessionmaker(bind=engine)
    with session() as s:
        car = datab_model.Cars(brend=brend, model=model, number=number, color=color, user_id=user_id)
        try:
            s.add(car)
            s.commit()
            return True
        except Exception as e:
            logger.error(str(e))
            return None
        finally:
            session.close_all()

@logger.catch
async def insert_work(car_id: int, time: str, date: str, description: str, user_id: int):
    session = sessionmaker(bind=engine)
    with session() as s:
        work = datab_model.Works(user_id=user_id, car_id=car_id, time=time, date=date, description=description)
        try:
            s.add(work)
            s.commit()
            return True
        except Exception as e:
            logger.error(str(e))
            return None
        finally:
            session.close_all()