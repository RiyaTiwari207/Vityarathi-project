students = []
attendance = {}

def add_student():
    name = input("Enter student name: ")
    if name not in students:
        students.append(name)
        attendance[name] = []
        print(f"{name} added successfully.")
    else:
        print("Student already exists.")

def mark_attendance():
    if len(students) == 0:
        print("No students added yet!")
        return
    
    print("\nMark Attendance (P = Present, A = Absent, L = Leave)")
    for name in students:
        status = input(f"{name}: ").upper()
        while status not in ["P", "A", "L"]:
            print("Invalid input! Enter P/A/L only.")
            status = input(f"{name}: ").upper()
        attendance[name].append(status)

    print("\nAttendance recorded successfully.\n")

def view_attendance():
    if len(attendance) == 0:
        print("No attendance available!")
        return

    print("\n--- Attendance Report ---")
    for name in attendance:
        print(f"{name}: {attendance[name]}")
    print()

def update_attendance():
    name = input("Enter student name to update: ")
    
    if name not in students:
        print("Student not found!")
        return

    print(f"Attendance history: {attendance[name]}")
    day = int(input("Enter day number to update: ")) - 1

    if day < 0 or day >= len(attendance[name]):
        print("Invalid day!")
        return

    new_status = input("Enter new value (P/A/L): ").upper()
    while new_status not in ["P", "A", "L"]:
        print("Invalid input! Enter P/A/L only.")
        new_status = input("Enter new value (P/A/L): ").upper()

    attendance[name][day] = new_status
    print("Attendance updated successfully.\n")


def menu():
    while True:
        print("""
========= SMART ATTENDANCE SYSTEM =========
1. Add Student
2. Mark Attendance
3. Update Attendance
4. View Attendance Report
5. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            update_attendance()
        elif choice == "4":
            view_attendance()
        elif choice == "5":
            print("Saving & Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


menu()
