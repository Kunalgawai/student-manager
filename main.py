def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    with open("students.txt", "a") as f:
        f.write(f"{name},{age},{course}\n")

    print("✅ Student added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as f:
            data = f.readlines()
            if not data:
                print("No students found.")
                return
            for i, line in enumerate(data, start=1):
                name, age, course = line.strip().split(",")
                print(f"{i}. Name: {name}, Age: {age}, Course: {course}")
    except FileNotFoundError:
        print("No data file found.")


def search_student():
    name_to_search = input("Enter name to search: ")
    found = False

    with open("students.txt", "r") as f:
        for line in f:
            name, age, course = line.strip().split(",")
            if name.lower() == name_to_search.lower():
                print(f"Found: {name}, {age}, {course}")
                found = True

    if not found:
        print("Student not found.")


def delete_student():
    name_to_delete = input("Enter name to delete: ")
    lines = []

    with open("students.txt", "r") as f:
        lines = f.readlines()

    with open("students.txt", "w") as f:
        for line in lines:
            name, age, course = line.strip().split(",")
            if name.lower() != name_to_delete.lower():
                f.write(line)

    print("✅ Student deleted (if existed).")


def main():
    while True:
        print("\n--- Student Manager ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
