from sklearn.model_selection import train_test_split
import pandas as pd
data = {
    'AREA':[1000, 1500, 2000, 2500, 3000, 3500],
    'BEDROOMS':[2, 3, 3, 4, 4, 5],
    'PRICE':[200000, 250000, 300000, 350000, 400000, 450000]
}
df = pd.DataFrame(data)
X = df[['AREA', 'BEDROOMS']]
y = df['PRICE']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training set:")
print(X_train.shape)
print(y_train.shape)
print("\nTest set:")
print(X_test.shape)
print(y_test.shape)
