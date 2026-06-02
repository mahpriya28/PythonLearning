import pandas as pd 
import sklearn

df=pd.read_csv("student_performance.csv")
print(df.head())
X=df[["Hours_Studied", "Attendance"]]
y=df["Pass"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("X_train:\n", X_train.head())
print("y_train:\n", y_train.head())
print("X_test:\n", X_test.head())
print("y_test:\n", y_test.head())
