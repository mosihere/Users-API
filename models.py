from database import Base
from sqlalchemy import Column, Integer, String




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    gender = Column(String)