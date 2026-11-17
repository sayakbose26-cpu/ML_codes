from xgboost import XGBClassifier
import pandas as pd
data = {
    "hours": [2, 3, 4, 5, 6],
    "marks":[0, 1, 1, 1, 0]
}
df = pd.DataFrame(data)
X = df[["hours"]].to_numpy()
Y = df[["marks"]].to_numpy()
model = XGBClassifier(
    n_estimators=50,
    learning = 0.1,
    max_depth=3,
    eval_metric="logloss"
)
model.fit(X,Y)
prediction = model.predict([[7]])
print(prediction[0])