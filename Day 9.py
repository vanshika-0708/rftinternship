import pandas as pd

# 1. CREATE DATASET
data = {
    'Name':   ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age':    [25, 32, 28, 22, 35],
    'Salary': [60000, 45000, 55000, 70000, 48000]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# 2. FILTER - SALARY > 50000
sal_filter = df[df['Salary'] > 50000]
print("\nEmployees with Salary > 50000:")
print(sal_filter)

# 3. FILTER - AGE < 30
age_filter = df[df['Age'] < 30]
print("\nEmployees with Age < 30:")
print(age_filter)

# BONUS - COMBINE MULTIPLE CONDITIONS
combined = df[(df['Salary'] > 50000) & (df['Age'] < 30)]
print("\nSalary > 50000 AND Age < 30:")
print(combined)

# BONUS - SAVE FILTERED DATA TO NEW FILE
sal_filter.to_csv('salary_filtered.csv', index=False)
age_filter.to_csv('age_filtered.csv', index=False)
combined.to_csv('combined_filtered.csv', index=False)
print("\nFiltered data saved to CSV files!")