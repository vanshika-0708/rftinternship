import pandas as pd
data={
    "Name":['A','B','C','D'],
    'Dept':['IT','HR','IT','HR'],
    'Salary':[50000,40000,60000,45000]
}
df=pd.DataFrame(data)
print("Employee Data:")
print(df)
#2 Average salary per department
avg_salary=df.groupby('Dept')['Salary'].mean()
print("\nAverage Salary per Department:")
print(avg_salary)
#3 Highest Paid Employeement per department
highest_paid=df.loc[df.groupby('Dept')['Salary'].idxmax()]
print("\n Highest Paid Employee per Department:")
print(highest_paid)
#BONUS-COUNT EMPLOYEES PER DEPARTMENT
emp_count=df.groupby('Dept')['Name'].count()
print("\nEmployee Count per Department:")
print(emp_count)
#BONUS-SORT DEPARTMENT BY AVG SALARY
sorted_avg=avg_salary.sort_values(ascending=False)
print("\nDepartments Sorted by Avg Salary:")
print(sorted_avg)
