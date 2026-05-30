import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#Create student marks dataset
np.random.seed(42)
data={
    "Student_ID":range(1,101),
    "Marks":np.random.normal(loc=70,scale=12,size=100)
}
df=pd.DataFrame(data)
#Keep marks between 0 and 100
df["Marks"]=df["Marks"].clip(0,100)
#Display first 5 rows
print(df.head())
#Calculate Skewness
skewness=df["Marks"].skew()
print(f"\nSkewness of Marks:{skewness:2f}")
plt.figure(figsize=(10,6))
sns.histplot(
    data=df,
    x="Marks",
    bins=10,
    kde=True,
    color="skyblue"
)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid("True")
plt.show()
#identity distribution types
if skewness>0:
    print("The distribution is positively skewed(Right Skewed).")
elif skewness<0:
    print("The distribution is Negatively Skewed(Left Skewed).")
else:
    print("The distribution is approximately symmetric. ")
    