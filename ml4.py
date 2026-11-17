from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
data = {
    'STUDY HOURS':[2, 3, 4, 5, 6, 7],
    'ATTENDENCE':[80, 85, 90, 95, 100, 100],
    'MARKS':[50, 60, 70, 80, 90, 100]
}
df = pd.DataFrame(data)
X = df[['STUDY HOURS', 'ATTENDENCE']]
y = df['MARKS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training set:")
print(X_train.shape)
print(y_train.shape)
print("\nTest set:")
print(X_test.shape)
print(y_test.shape)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("\nScaled Training set:")
print(X_train_scaled.shape)
print("\nScaled Test set:")
print(X_test_scaled.shape)
model = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])
model.fit(X_train, y_train)
prediction = model.predict(X_test)
print("\nPredictions:")
print(prediction)