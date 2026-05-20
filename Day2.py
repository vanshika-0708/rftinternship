MARKS=[78,85,90,67,85,92]
def calculate_average(marks):
    return sum(marks)/len(marks)
def calculate_highest(marks):
    return max(marks)
def calculate_lowest(marks):
    return min(marks)
def count_above_average(marks,average):
    return sum(1 for mark in marks if mark>average)
def grade_distribution(marks):
    grades = {'A': 0, 'B': 0, 'C': 0, 'FAIL': 0}
    for mark in marks:
        if mark >= 85:
            grades['A'] += 1
        elif mark >= 70:
            grades['B'] += 1
        elif mark >= 50:
            grades['C'] += 1
        else:
            grades['FAIL'] += 1
    return grades

def analyze_scores(marks):
    print("=" * 40)
    print("      STUDENT SCORE ANALYZER")
    print("=" * 40)
    print(f"Marks: {marks}")
    print("-" * 40)

    average = calculate_average(marks)
    highest = calculate_highest(marks)
    lowest = calculate_lowest(marks)
    above_avg_count = count_above_average(marks, average)
    grades = grade_distribution(marks)

    print(f"Average Score : {average:.2f}")
    print(f"Highest Score : {highest}")
    print(f"Lowest Score  : {lowest}")
    print(f"Students Above Average: {above_avg_count}")
    print("-" * 40)
    print("Grade Distribution:")
    for grade, count in grades.items():
        print(f"  {grade:>4} : {count} student(s)")
    print("=" * 40)

analyze_scores(MARKS)
    