from CustomerFrequency.data_preparation import SqlHandler 
from CustomerFrequency.logger import CustomFormatter
import pandas as pd
Inst = SqlHandler('temp', 'menu') 
data = pd.read_csv('menu_data.csv') 
Inst.insert_many(data) 
Inst.close_cnxn()
