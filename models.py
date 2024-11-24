from sqlalchemy import Column,Integer , String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base() # it is database class



class Form(Base):
    __tablename__ = "userDetails"
    id = Column(Integer, primary_key=True)
    Firstname = Column(String, nullable=False)
    Lastname = Column(String, nullable=True)
    age = Column(String , nullable=False)
    email = Column(String,nullable=False)
    Address = Column(String, nullable=False)
    

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name =Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer,primary_key=True)