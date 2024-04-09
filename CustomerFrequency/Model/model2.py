import pandas as pd
import statsmodels.api as sm
from stepwise_regression import step_reg

# Load the data
data = pd.read_csv("../Data/order_data.csv")

# Convert 'date_of_order' to datetime and extract year, month, and day
data['date_of_order'] = pd.to_datetime(data['date_of_order'])
data['order_year'] = data['date_of_order'].dt.year
data['order_month'] = data['date_of_order'].dt.month
data['order_day'] = data['date_of_order'].dt.day

# Remove the original 'date_of_order' column if it's no longer needed
data = data.drop('date_of_order', axis=1)

# Prepare the variables for regression analysis
Y_linear = data["price"]
X_linear = data.drop("price", axis=1)

# Add a constant to the predictor variables
X_linear = sm.add_constant(X_linear)

# Fit the OLS linear regression model
model_linear = sm.OLS(Y_linear, X_linear)
results = model_linear.fit()

# Print the summary of the regression results
print(results.summary())

# Optional: Perform backward stepwise regression if needed
backselect = step_reg.backward_regression(X_linear, Y_linear, 0.05, verbose=False)
print(backselect)