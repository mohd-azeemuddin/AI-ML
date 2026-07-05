# Create a function to return a square
# def square(number):
#     return number ** 2
# result = square(7)
# print(result)

# check num is even
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# res = is_even(17)
# print(res)

''' Calculator
num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter second number: "))

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Error: Division by zero!"
    return n1 / n2

if operator == "+":
    result = add(num1, num2)
    print(f"Result: {result}")

elif operator == "-":
    result = sub(num1, num2)
    print(f"Result: {result}")

elif operator == "*":
    result = mul(num1, num2)
    print(f"Result: {result}")

elif operator == "/":
    result = div(num1, num2)
    print(f"Result: {result}")

else:
    print("Invalid operator!")'''

'''def factorial(n):
    result = 1
    
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  
print(factorial(0))'''


def calculate_total(marks_list):
    return sum(marks_list)

def calculate_average(total, count):
    return total / count

def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

marks = []
n = int(input("How many subjects do you want to enter? "))

for i in range(n):
    score = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(score)

total_marks = calculate_total(marks)
average_marks = calculate_average(total_marks, n)
final_grade = assign_grade(average_marks)

print("\n--- Student Report Card ---")
print(f"Total Marks:   {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Final Grade:   {final_grade}")