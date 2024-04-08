# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

# Simulate data or load your dataset
df = pd.read_csv("../Data/order_data.csv")
print(df)
X = df.drop('quantity_ordered', axis=1)


X['year_of_order'] = pd.to_datetime(df['date_of_order']).dt.year
X = X.drop('date_of_order', axis=1)  

X = X.drop(['order_id', 'menu_id', 'customer_id'], axis=1)

# Define the target variable y
y = df['quantity_ordered']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions and evaluate the model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print(f"The Mean Squared Error of the model is: {mse}")

