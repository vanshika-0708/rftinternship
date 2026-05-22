import matplotlib.pyplot as plt
categories=["FOOD","TRAVEL","SHOPPING"]
expenses=[500,300,200]
explode=(0.1,0,0)
#colors
colors=['yellow','green','blue']
plt.figure(figsize=(7,7))
plt.pie(expenses,labels=categories,
        autopct='%1.if%%',
        colors=colors,startangle=140,shadow=True)
plt.title("Category breakdown-Expense Distribution",fontsize=14,fontweight="bold")
plt.tight_layout()
plt.savefig("chart.png")
plt.show()