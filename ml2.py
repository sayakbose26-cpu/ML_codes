import numpy as np
import pandas as pd
data = {
    'NAME': ['A', 'B', 'C', 'D', 'D','C'],
    'AGE': [25, None, 35, 40, 45, 50],
    'SALARY': [50000, 60000, 70000, None, 90000, 100000],
    'DEPARTMENT': ['HR', 'IT', 'SALES', 'IT', None, 'Finance'],
}
df = pd.DataFrame(data)
print(df.isnull().sum())
print(df[df.isnull().any(axis=1)])
df['AGE'] = df['AGE'].fillna(df['AGE'].median())
df['SALARY'] = df['SALARY'].fillna(df['SALARY'].median())
df['DEPARTMENT'] = df['DEPARTMENT'].fillna(df['DEPARTMENT'].mode()[0])   
df = df.drop_duplicates()
df = pd.get_dummies(df, columns=['DEPARTMENT'], dtype=int)
df['AVERAGE SALARY'] = df['SALARY'].mean()
print(df)

