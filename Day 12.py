import matplotlib.pyplot as plt
import numpy as np
#Dataset
students=["Amit","Riya","John"]
math=[85,92,78]
science=[76,88,91]
english=[90,85,70]
# Bar chart
plt.bar(students,math,color="skyblue",edgecolor="black")
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
#Group bar chart(Bonus)
x=np.arange(3)
plt.bar(x-0.25,math,0.25,label="Math",color="skyblue")
plt.bar(x,   science,0.25,label="Science",color="orange")
plt.bar(x+0.25,english,0.25,label="English",color="green")
plt.xticks(x,students)
plt.title("Student performance - All Subjects")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.show()
print("Done!")