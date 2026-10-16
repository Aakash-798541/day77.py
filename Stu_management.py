
students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")

        if student_id in students:
            print("Student ID already exists!")
        else:
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            marks = float(input("Enter Student Marks: "))

            students[student_id] = {
                "name": name,
                "age": age,
                "marks": marks
            }

            print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\n===== STUDENT RECORDS =====")

            for student_id, details in students.items():
                print("Student ID:", student_id)
                print("Name:", details["name"])
                print("Age:", details["age"])
                print("Marks:", details["marks"])
                print("----------------------")

    elif choice == "3":
        student_id = input("Enter Student ID to search: ")

        if student_id in students:
            details = students[student_id]
            print("Name:", details["name"])
            print("Age:", details["age"])
            print("Marks:", details["marks"])
        else:
            print("Student not found!")

    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")

        if student_id in students:
            del students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
