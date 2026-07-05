# import csv

# with open("students.csv", "w", newline="") as file:

#     writer = csv.writer(file)

#     writer.writerow(["Name", "Age"])

#     writer.writerow(["Azeem", 23])
# import csv

# with open("students.csv", "r") as file:

#     reader = csv.reader(file)

#     for row in reader:
#         print(row)
# with open("sample.txt", "a") as file:
#     file.write("\nNew Line")
# import json

# data = {
#     "name": "Azeem",
#     "age": 23
# }

# with open("data.json", "w") as file:
#     json.dump(data, file)
# Personal Diary System

# Personal Diary System in Python

def write_entry():
    entry = input("\nWrite your diary entry:\n")

    with open("diary.txt", "a") as file:
        file.write(entry + "\n")
        file.write("-" * 40 + "\n")
    print("Diary entry saved successfully!\n")


def view_entries():
    try:
        with open("diary.txt", "r") as file:
            content = file.read()

            if content:
                print("\n--- Previous Diary Entries ---")
                print(content)
            else:
                print("\nNo diary entries found.")

    except FileNotFoundError:
        print("\nDiary file not found. No entries yet.")


def main():
    while True:
        print("\n===== Personal Diary System =====")
        print("1. Write Diary Entry")
        print("2. View Previous Entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            write_entry()

        elif choice == "2":
            view_entries()

        elif choice == "3":
            print("Exiting Diary System...")
            break

        else:
            print("Invalid choice! Please try again.")

main()
