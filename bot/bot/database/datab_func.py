from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from loguru import logger

from bot.loader.load import engine
from bot.database import datab_model, select_db, delete_db


@logger.catch
async def decrement_balance(user_id: int, amount: int):
    """decrement balance"""
    session = sessionmaker(bind=engine)
    with session() as s:
        user = s.query(datab_model.Users).filter(datab_model.Users.user_id == user_id).first()
        if user.balance - amount >= 0:
            try:
                user.balance -= amount
                s.commit()
                return True
            except Exception as e:
                logger.error(str(e))
                return None
            finally:
                session.close_all()
    return False

@logger.catch
async def subs_user_update_day(user_id: int):
    session = sessionmaker(bind=engine)
    with session() as s:
        sub_user = s.query(datab_model.SubsUsers).filter(datab_model.SubsUsers.user_id == user_id).first()
    sub = await select_db.sub_select(sub_user.subs_id)
    with session() as s:
        sub_user = s.query(datab_model.SubsUsers).filter(datab_model.SubsUsers.user_id == user_id).first()
        if sub_user is None: return None
        if sub_user.time_day <= 0:
            try:
                sub_user.subs_state = False
                sub_user.amount_send = 0
                sub_user.time_day = 0
                sub_user.subs_id = 0
                s.commit()
                return False
            except Exception as e:
                logger.error(str(e))
                return None
            finally:
                session.close_all()
        try:
            sub_user.time_day -= 1
            sub_user.amount_send = sub.amount_send
            s.commit()
            return True
        except Exception as e:
            logger.error(str(e))
            return None
        finally:
                session.close_all()

@logger.catch
async def add_balance(user_id: int, amount: int):
    """add balance to amount"""
    session = sessionmaker(bind=engine)
    with session() as s:
        user = s.query(datab_model.Users).filter(datab_model.Users.user_id == user_id).first()
        try:
            user.balance += amount
            s.commit()
            return True
        except Exception as e:
            logger.error(str(e))
            return None
        finally:
                session.close_all()
    return False

@logger.catch
async def check_balance(user_id: int, amount: int) -> bool:
    """if balance >= amount return True"""
    session = sessionmaker(bind=engine)
    with session() as s:
        balance = s.query(datab_model.Users).filter(datab_model.Users.user_id == user_id).first().balance
    session.close_all()
    if balance >= amount:
        return True
    else:
        return False

@logger.catch
async def check_referal(user_id: int, invited_id: int):
    session = sessionmaker(bind=engine)
    with session() as s:
        referal_line = s.query(datab_model.Referals).filter(datab_model.Referals.user_id == user_id and datab_model.Referals.invited_id == invited_id).first()
        session.close_all()
        if referal_line is not None:
            return True
    return False

@logger.catch
async def use_promo_code(id: int):
    session = sessionmaker(bind=engine)
    with session() as s:
        promo_code = s.query(datab_model.PromoCodes).filter(datab_model.PromoCodes.id == id).first()
        if promo_code.amount_use - 1 >= 0:
            try:
                promo_code.amount_use -= 1
                s.commit()
                return True
            except Exception as e:
                logger.error(str(e))
                return None
            finally:
                session.close_all()
        else:
            await delete_db.delete_promo_code(id)
    session.close_all()
    return False

@logger.catch
async def all_cheques_amount_payment():
    session = sessionmaker(bind=engine)
    with session() as s:
        cheques = s.query(func.sum(datab_model.Cheques.amount_payment).label('amount_payment')).first()
    session.close_all()
    return cheques

@logger.catch
async def all_purchases_amount_pay():
    session = sessionmaker(bind=engine)
    with session() as s:
        purchases = s.query(func.sum(datab_model.Purchases.amount_pay).label('amount_pay')).first()
    session.close_all()
    return purchases

@logger.catch
async def count_subs_users():
    session = sessionmaker(bind=engine)
    with session() as s:
        subs_users = s.query(datab_model.SubsUsers).filter(datab_model.SubsUsers.subs_state != False).count()
    session.close_all()
    return subs_users