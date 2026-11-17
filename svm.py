from sklearn.svm import SVC
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
data = {
    "hours": [2, 3, 4, 5, 6],
    "marks":['Fail', 'Pass', 'Pass', 'Pass', 'Pass']
}
df = pd.DataFrame(data)
X = df[["hours"]].to_numpy()
y = df["marks"].to_numpy()
model = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('classifier', SVC(kernel = "linear"))
])
model.fit(X, y)
predicted_marks = model.predict([[7]])
print("Predicted marks for 4 hours of study:", predicted_marks[0])
