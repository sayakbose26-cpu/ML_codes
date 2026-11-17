import numpy as np
import pandas as pd
data ={
    'STUDENT NAME': ['Alice', 'Bob', 'Charlie', 'David', 'Eva','rose'],
    'PYTHON MARKS': [25, 30, 35, 40, 45, 50],
    'JAVA MARKS': [50, 60, 70, 80, 90, 100],
    'ML MARKS': [37, 60, 70, 80, 90, 100],
}
df = pd.DataFrame(data)
total = df['PYTHON MARKS'] + df['JAVA MARKS'] + df['ML MARKS']
df['TOTAL MARKS'] = total
print(df.head())
print(df['ML MARKS'].mean())
print(df[df['ML MARKS'] > 80])
print(df.isnull().sum())
print(df[df['TOTAL MARKS'] == df['TOTAL MARKS'].max()])
x = df[['PYTHON MARKS', 'JAVA MARKS', 'ML MARKS']]
X = x.to_numpy()
print(X)
