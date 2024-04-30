import pandas as pd # < > CustomerFrequency

# data=pd.read_csv('Data/customer_data.xlsx')

# print(data.head())

# # import CustomerFrequency

# from CustomerFrequency.DataPreparation.schema import * 

import os
import glob 

PATH='Data'

mapping={
        'customer_data.csv': 'customers',
        'menu_data.csv': 'customers',
        'employee_data.csv': 'customers',
        'transactions_data.csv': 'customers',
        'order_data.csv': 'customers'
         
         }

from CustomerFrequency.DataBase.sql_interactions import SqlHandler




# files=glob.glob(PATH+'/*.csv')

# def bulk_insert_from_csv(files:list):
#     for i in files:
#         inst=SqlHandler('')
#         print(pd.read_csv(i).head())
#         print(os.path.basename(i))

