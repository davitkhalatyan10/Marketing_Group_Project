import pandas as pd # < > CustomerFrequency

# data=pd.read_csv('Data/customer_data.xlsx')

# print(data.head())

# # import CustomerFrequency

# from CustomerFrequency.DataPreparation.schema import * 

import os
import glob 

PATH='Data'

mapping={'customer_data.csv': 'customers',
         
         }

from CustomerFrequency.DataBase.sql_interactions import SqlHandler




files=glob.glob(PATH+'/*.csv')

for i in files:
    inst=SqlHandler('')
    print(pd.read_csv(i).head())
    print(os.path.basename(i))