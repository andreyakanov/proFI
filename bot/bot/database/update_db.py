from sqlalchemy.orm import sessionmaker

from loguru import logger

from bot.loader.load import engine
from bot.database import datab_model, delete_db, select_db

@logger.catch
async def update_subs_user(user_id: int, subs_id: int):
    session = sessionmaker(bind=engine)
    sub = await select_db.sub_select(subs_id)
    with session() as s:
        subs_user = s.query(datab_model.SubsUsers).filter(datab_model.SubsUsers.user_id == user_id).first()
        if subs_user is not None:
            try:
                if sub is not None:
                    subs_user.amount_send = sub.amount_send
                    subs_user.subs_id = sub.id
                    subs_user.subs_state = True
                    subs_user.time_day = sub.time_day
                    s.commit()
                    return True
                return False
            except Exception as e:
                logger.error(str(e))
                return None
            finally:
                session.close_all()
    return False

@logger.catch
async def update_subs_users_amount_send(user_id: int, amount: int):
    session = sessionmaker(bind=engine)
    with session() as s:
        subs_user = s.query(datab_model.SubsUsers).filter(datab_model.SubsUsers.user_id == user_id).first()
        if subs_user is not None:
            try:
                if subs_user.amount_send - amount >= 0:
                    subs_user.amount_send -= amount
                    s.commit()
                    return True
                else:
                    return False
            except Exception as e:
                logger.error(str(e))
                return None
            finally:
                session.close_all()
    return False

    
@logger.catch
async def update_auto_post(id: int):
    session = sessionmaker(bind=engine)
    with session() as s:
        auto_post = s.query(datab_model.AutoPosts).filter(datab_model.AutoPosts.id == id).first()
        if auto_post is not None:
            try:
                if auto_post.amount_send - 1 >= 0:
                    auto_post.amount_send -= 1
                    s.commit()
                    return True
                else:
                    await delete_db.delete_auto_post(auto_post.id)
                    return False
            except Exception as e:
                logger.error(str(e))
                return None
            finally:
                session.close_all()
    return False
