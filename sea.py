import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "students": ["A", "B", "C", "D", "E"],
    "hours": [2, 3, 4, 5, 6],
    "marks": [55,65,70,85,95],
    "attendence": [40,50,65,80,95]
}
df = pd.DataFrame(data)
correlation = df[["hours", "marks", "attendence"]].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
