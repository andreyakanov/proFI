from sqlalchemy import Column, Integer, String, Boolean, BIGINT
from bot.loader.load import Base, engine

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Works(Base):
    __tablename__ = 'works'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BIGINT, nullable=False)
    car_id = Column(Integer, nullable=False)
    time = Column(String, nullable=False)
    date = Column(String, nullable=False)
    description = Column(String, nullable=False)

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(BIGINT, primary_key=True, nullable=False)
    user_tag = Column(String(250), nullable=True)
    user_name = Column(String(250), nullable=True)
    date_create = Column(String(256), nullable=False)

class Cars(Base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    brend = Column(String, nullable=False)
    model = Column(String, nullable=False)
    number = Column(String, nullable=False)
    color = Column(String, nullable=False)
    user_id = Column(BIGINT, nullable=False)

async def create_tables():
    Base.metadata.create_all(engine)