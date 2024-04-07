
# from ..logger import CustomFormatter

import logging
import os

import logging
from ..logger import CustomFormatter

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


from sqlalchemy import create_engine,Column,Integer,String,Float, DATE, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

engine = create_engine('sqlite:///temp.db')

Base= declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    builidingID = Column(Integer)
    phonenumber = Column(Integer)

class Customers(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phonenumber = Column(Integer)


class Menu(Base):
    __tablename__ = "Menu"

    menu_id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column (String)
    price = Column(Integer)


# Define the Order table
class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    date_of_order = Column(DateTime)
    status = Column(String)
    price_of_order = Column (Integer)
    quantity_ordered = Column(Integer)
    menu_id = Column(Integer, ForeignKey('Menu.menu_id'))
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))

# Define the Sales table
class Transaction(Base):
    __tablename__ = "transaction"

    transaction_id = Column(Integer, primary_key=True)
    date_of_payment = Column(DateTime)
    amount = Column(Integer)
    type = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
   

    order = relationship("Order")
    customer = relationship("Customers")
    employee = relationship("Employee")
    menu = relationship("Menu")
    transaction = relationship("Transaction")

Base.metadata.create_all(engine)