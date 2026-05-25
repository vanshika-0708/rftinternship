import pandas as pd

# 1. CREATE DATASET
data = {
    'Name':    ['Amit', 'Riya', 'John'],
    'Math':    [80, 90, 60],
    'Science': [70, 88, 65],
    'English': [85, 92, 70]
}

df = pd.DataFrame(data)
print("Student Data:")
print(df)

# 2. CALCULATE AVERAGE MARKS PER STUDENT
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
print("\nAverage Marks:")
print(df[['Name', 'Average']])

# 3. FIND TOPPER
topper = df.loc[df['Average'].idxmax(), 'Name']
print("\nTopper:", topper)

# 4. COUNT STUDENTS ABOVE AVERAGE
overall_avg = df['Average'].mean()
above_avg = df[df['Average'] > overall_avg]
print("Overall Average:", round(overall_avg, 2))
print("Students above average:", len(above_avg))
print(above_avg[['Name', 'Average']])

# BONUS - ADD GRADE COLUMN
def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Average'].apply(get_grade)
print("\nWith Grade Column:")
print(df)

# BONUS - SUBJECT WISE AVERAGE
print("\nSubject-wise Average:")
print("Math   :", round(df['Math'].mean(), 2))
print("Science:", round(df['Science'].mean(), 2))
print("English:", round(df['English'].mean(), 2))