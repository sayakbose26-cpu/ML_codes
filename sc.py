from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

data = {
    "hours": [2, 3, None, 5, 6],
    "marks": [55, 65, 75, 85, 95]
}
df = pd.DataFrame(data)
X = df[["hours"]].to_numpy()
y = df["marks"].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])
model.fit(X_train, y_train)
predicted_marks = model.predict(X_test)
print("Predicted marks for", X_test[0][0], "hours of study:", predicted_marks[0])
print("actual marks for", X_test[0][0], "hours of study:", y_test[0])
mae=mean_absolute_error(y_test, predicted_marks)
mse=mean_squared_error(y_test, predicted_marks)
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)