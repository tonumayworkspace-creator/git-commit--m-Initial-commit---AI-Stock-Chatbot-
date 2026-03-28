# app/models/item.py

from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    stock = Column(Integer)
    price = Column(Integer)