import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create synthetic data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Reshape for sklearn
y = np.array([40, 50, 60, 70, 80, 90, 100, 110, 120, 130])  # Linear relationship with some noise
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Split data into training and testing sets
# Fit a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict using the model
y_pred = model.predict(X_test)
rmse_linear = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error (Linear Model):", rmse_linear)

# Plot the data and the model's predictions
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', label='Simple Line')
plt.title('Underfitting Example')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()