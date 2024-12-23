from sqlalchemy import  Column, Integer, String
from database.postgresql.base import Base


class Users(Base):
    __tablename__ = "users"
  
    username = Column(String, primary_key=True)
    password = Column(String)
    