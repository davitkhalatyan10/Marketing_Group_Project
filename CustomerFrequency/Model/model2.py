import pandas as pd
import statsmodels.api as sm
from stepwise_regression import step_reg

data=pd.read_csv("../Data/order_data.csv")

data_numeric = data.select_dtypes(exclude=["object"])
data_object = data.select_dtypes(include=["object"])

data_full = pd.concat((data_numeric, pd.get_dummies(data_object, drop_first=True)), axis=1)

Y_linear=data_full["price"]
X_linear=data_full.drop("price", axis=1)

X_linear=sm.add_constant(X_linear)

model_linear= sm.OLS(Y_linear,X_linear)

results=model_linear.fit()

results.summary()

backselect = step_reg.backward_regression(X_linear, Y_linear, 0.05,verbose=False)
backselect