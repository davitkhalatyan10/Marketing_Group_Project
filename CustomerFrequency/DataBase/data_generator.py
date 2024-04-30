from faker import Faker
import pandas as pd
import random
import logging
from ..Logger import CustomFormatter
import os
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

fake = Faker()

dish_names = [
    "Caffè Latte", "Caffè Misto", "Caffè Mocha", "Cappuccino", "Caramel Macchiato",
    "Cinnamon Dolce Latte", "Espresso", "Espresso con Panna", "Espresso Macchiato",
    "Flat White", "Honey Almondmilk Flat White", "Oleato Caffe Latte w/ Oatmilk*",
    "White Chocolate Mocha", "Black Tea", "Matcha Tea Latte", "Royal English Breakfast Tea Latte",
    "Teavana London Fog Tea", "Caffè Vanilla Frappuccino", "Caramel Frappuccino",
    "Caramel Ribbon Crunch Crème Frappuccino", "Caramel Ribbon Crunch Frappuccino",
    "Chai Crème Frappuccino", "Chocolate Cookie Crumble Crème Frappuccino",
    "Double Chocolaty Chip Crème Frappuccino", "Espresso Frappuccino", "Java Chip Frappuccino",
    "Matcha Crème Frappuccino", "Mocha Cookie Crumble Frappuccino", "Mocha Frappuccino",
    "Strawberry Crème Frappuccino", "Vanilla Bean Crème Frappuccino", "White Chocolate Crème Frappuccino",
    "White Chocolate Mocha Frappuccino", "Chocolate Cream Cold Brew", "Cinnamon Caramel Cream Cold Brew",
    "Cinnamon Caramel Cream Nitro Cold Brew", "Cold Brew", "Cold Brew Coffee with Milk",
    "Iced Blonde Vanilla Latte", "Iced Brown Sugar Oatmilk Shaken Espresso", "Iced Caffe Americano",
    "Iced Caffè Latte", "Iced Cinnamon Dolce Latte", "Iced Espresso", "Iced Flat White",
    "Iced Hazelnut Oatmilk Shaken Espresso", "Iced Honey Almondmilk Flat White", "Iced Mocha",
    "Iced Shaken Espresso", "Iced White Chocolate Mocha", "Salted Caramel Cream Cold Brew",
    "Vanilla Sweet Cream Cold Brew", "Vanilla Sweet Cream Nitro Cold Brew", "Iced Black Tea",
    "Iced Black Tea Lemonade", "Iced Chai Tea Latte", "Iced Green Tea", "Iced Matcha Tea Lemonade",
    "Iced Passion Tango Tea", "Iced Passion Tango Tea Lemonade", "Iced Peach Green Tea",
    "Iced Peach Green Tea Lemonade", "Iced Royal English Breakfast Tea", "Chocolate Chip Cookie",
    "Featured / Seasonal Cookie", "Vanilla Cookie"
]
def generate_armenian_phone_number():
   
    area_code = random.randint(10, 99)  # Random 2-digit area code
    subscriber_number = ''.join(random.choices('0123456789', k=6))  # Random 6-digit subscriber number

    return f"+374 ({area_code}) {subscriber_number}"

def generate_employee(employee_id):
    # Generate Armenian-style phone number
    phone_number = generate_armenian_phone_number()
    
    return {
        "employee_Id": employee_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "builidingID": random.randint(3000, 10000),
        "phone_number": phone_number,
    }

    

def generate_customer(customer_id):
    phone_number = generate_armenian_phone_number()
    return {
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone_number":phone_number
    }

def generate_menu(menu_id):
    return {
        "menu_id": menu_id,
        "name": random.choice(dish_names),
        "price": random.choice(["350", "400", "450", "500","550", "600", "650","750","900","1200"]),
        "size": random.choice(["0.25", "0.5", "0.75"])
    }

from datetime import datetime
def generate_orders(order_id,menu_id,customer_id):
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = fake.date_time_between_dates(start_date, end_date)
    

    return {
        "order_id": order_id,
        "date_of_order": random_date,
        "quantity_ordered": random.randint(1,20),
        "menu_id": menu_id,
        "customer_id": customer_id,
        "price": random.randrange(0,30000,10)
        

    }


def generate_transactions(transaction_id,customer_id, employee_id):
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = fake.date_time_between_dates(start_date, end_date)
    transaction_type = random.choice(["cash", "visa", "mastercard","applepay"])
    

    return {
        "transaction_id": transaction_id,
        "date_of_payment": random_date,
        "customer_id": customer_id,
        "employee_id": employee_id,
        "amount": random.randrange(0,30000,10),
        "type": transaction_type
    }



