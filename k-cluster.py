import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

data ={
    "spending":[10,20,30,40,50,100,2000,3210]
}
wcss=[]
df=pd.DataFrame(data)
for k in range(1,8):
    model = KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
    )
    model.fit(df[["spending"]])
    wcss.append(model.inertia_)
plt.plot(range(1,8),wcss,marker="o")
plt.show()