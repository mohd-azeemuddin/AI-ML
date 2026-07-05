# num = []
# for i in range(5):
#     user = int(input("Enter the number:"))
#     num.append(user)
# print(sum(num))
# print(max(num))
# print(min(num))


students = []

# Add Student
def add_student():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    course = input("Enter your course: ")

    students.append({
        "Name": name,
        "Age": age,
        "Course": course
    })

    print("Student added successfully!")

def display_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print(student)

def search_student():
    search_name = input("Enter student name to search: ")

    for student in students:
        if student["Name"].lower() == search_name.lower():
            print(student)
            return

    print("Student not found.")

while True:

    user = input(
        "\nEnter feature (add, display, search, exit): "
    ).lower()

    if user == "add":
        add_student()

    elif user == "display":
        display_students()

    elif user == "search":
        search_student()

    elif user == "exit":
        print("Program ended.")
        break

    else:
        print("Invalid option.")



