import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures


# Create synthetic data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Reshape for sklearn
y = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180, 200])  # Linear relationship with some noise
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

poly = PolynomialFeatures(degree=6)
X_poly = poly.fit_transform(X_train)

# Split data into training and testing sets
# Fit a linear regression model
poly_model = LinearRegression()
poly_model.fit(X_poly, y_train)
X_test_poly = poly.transform(X_test)
y_test_pred = poly_model.predict(X_test_poly)
rmse_poly = np.sqrt(mean_squared_error(y_test, y_test_pred))
print("Root Mean Squared Error (Polynomial Model):", rmse_poly)

X_range = np.linspace(1, 10, 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)
y_range_pred = poly_model.predict(X_range_poly)

# Plot the data and the model's predictions
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_range, y_range_pred, color='green', label='Polynomial Fit')
# plt.scatter(X_test, y_test_pred, color='red', label='Polynomial Predictions')
plt.title('Overfitting Example')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

