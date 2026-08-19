#  Check if a number is prime 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


#  Largest number using *args 
def find_largest(*args):
    if not args:
        return None
    largest = args[0]
    for num in args:
        if num > largest:
            largest = num
    return largest


#  Student info using **kwargs 
def print_student_info(**kwargs):
    print("Student Information:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


#  CHALLENGE: max, min, average, sum of a list
def analyze_numbers(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = total / len(numbers)
    return {
        "maximum": maximum,
        "minimum": minimum,
        "average": average,
        "sum": total
    }


#DEMO / TEST CASES
if __name__ == "__main__":
    # Task 1
    print("=== Prime Check ===")
    for n in [2, 15, 17, 1, 29]:
        print(f"{n} is prime: {is_prime(n)}")

    # Task 2
    print("\n=== Largest Number (*args) ===")
    print("Largest of 4, 9, 2, 17, 5 ->", find_largest(4, 9, 2, 17, 5))
    print("Largest of -3, -10, -1 ->", find_largest(-3, -10, -1))

    # Task 3
    print("\n=== Student Info (**kwargs) ===")
    print_student_info(name="Riya", age=21, course="Python", grade="A")

    # Challenge
    print("\n=== List Analysis (max, min, avg, sum) ===")
    nums = [12, 45, 7, 23, 56, 9]
    result = analyze_numbers(nums)
    print(f"Numbers: {nums}")
    print(f"Maximum: {result['maximum']}")
    print(f"Minimum: {result['minimum']}")
    print(f"Average: {result['average']:.2f}")
    print(f"Sum: {result['sum']}")