import pandas as pd
path = 'Data/rfm_scores.csv'
df = pd.read_csv(path)
print(pd.read_csv(path))

print(df.dtypes)
first_r_score = type(df['R_score'].iloc[0])
print("First R_score value:", first_r_score)

# import CustomerFrequency.DataBase.sql_interactions as sql

# connector = sql.SqlHandler('temp','segmentation')

# get_coulnms_type = 'Select * from segmentation;'
# connector.cursor.execute(get_coulnms_type)
# data = connector.cursor.fetchall()
# print(data)