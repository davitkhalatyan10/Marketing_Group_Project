
# from ..logger import CustomFormatter
import logging
import os
from ..Logger import CustomFormatter


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
    phone_number = Column(String)

class Customers(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)


class Menu(Base):
    __tablename__ = "Menu"

    menu_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    size = Column (String)


# Define the Order table
class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    date_of_order = Column(DateTime)
    quantity_ordered = Column(Integer)
    menu_id = Column(Integer, ForeignKey('Menu.menu_id'))
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    price = Column (Integer)


# Define the Sales table
class Transaction(Base):
    __tablename__ = "transaction1"

    transaction_id = Column(Integer, primary_key=True)
    date_of_payment = Column(DateTime)
    amount = Column(Integer)
    type = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
   

    # order = relationship("Order")
    customer = relationship("Customers")
    employee = relationship("Employees")
    # menu = relationship("Menu")


class CustomerSegmentation(Base):
    __tablename__='segmentation'

    id = Column(Integer,primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    satisfaction_score = Column(Integer) 
    transaction_count = Column(Integer)
    customer_segment = Column(String)


    segmentation = relationship("segmentation")

class CustomerSegmentation(Base):
    __tablename__='rfm_table'

    id = Column(Integer,primary_key=True)
    CustomerId = Column(Integer, ForeignKey('customers.customer_id'))
    Recency = Column(Integer) 
    Frequency = Column(Integer)
    Monetary = Column(Integer)
    R_Quartile= Column(Integer) 
    F_Quartile = Column(Integer)
    M_Quartile = Column(Integer)
    RFMScore = Column(Integer)

    rfm_table = relationship("rfm_table")


Base.metadata.create_all(engine)

