import pandas as pd
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva','rose'],
    'age': [25, None, 35, 40, 45, 50],
    'salary': [50000, 60000, 70000, 80000, 90000, 100000]
}
df = pd.DataFrame(data)
df["age"] = df["age"].fillna(df["age"].median())
print(df)
print(df.head())
print(df.tail())
print(df.shape[0])
print(df.describe())
print(df.info())
print(df.groupby('name')['salary'].mean())