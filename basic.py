# If creating DB first time please run it with below command too
#from CustomerFrequency.DataBase.schema import * 
from CustomerFrequency.DataBase import SqlHandler 
from CustomerFrequency.Logger import CustomFormatter
import pandas as pd

Inst = SqlHandler('temp', 'menu')  
data = pd.read_csv('Data/menu_data.csv') 
Inst.insert_many(data) 
Inst.close_cnxn()

Inst1 = SqlHandler('temp', 'employees') 
data1 = pd.read_csv('Data/employee_data.csv') 
print(data1)
Inst1.insert_many(data1) 
Inst1.close_cnxn()

Inst2 = SqlHandler('temp', 'customers') 
data2 = pd.read_csv('Data/customer_data.csv') 
Inst2.insert_many(data2) 
Inst2.close_cnxn()

Inst3 = SqlHandler('temp', 'orders') 
data3 = pd.read_csv('Data/order_data.csv') 
Inst3.insert_many(data3) 
Inst3.close_cnxn()

Inst4 = SqlHandler('temp', 'transaction1') 
data4 = pd.read_csv('Data/transactions_data.csv') 
Inst4.insert_many(data4) 
Inst4.close_cnxn()

Inst5 = SqlHandler('temp', 'segmentation')
data5 = pd.read_csv('Data/Customer_Transaction_with_Satisfaction.csv')
Inst5.insert_many(data5) 
Inst5.close_cnxn()

Inst6 = SqlHandler('temp', 'rfm_table')
data6 = pd.read_csv('Data/rfm_scores.csv')
Inst6.insert_many(data6) 
Inst6.close_cnxn()
