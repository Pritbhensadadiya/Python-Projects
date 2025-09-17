student_grades = {}

def add_student(name, grade):
    if name in student_grades:
        print(f"{name} already exists with grade {student_grades[name]}")
    else:
        student_grades[name] = grade
        print(f"✅ Added {name} with grade {grade}")

def update_student(name, grade):
    if name in student_grades:
        old_grade = student_grades[name]
        student_grades[name] = grade
        print(f"🔄 Updated {name}: {old_grade} → {grade}")
    else:
        print(f"⚠️ {name} not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"🗑️ {name} has been deleted.")
    else:
        print(f"⚠️ {name} not found!")

def display_all_students():
    if student_grades:
        print("\n📋 All Students:")
        for name, grade in student_grades.items():
            print(f"- {name}: {grade}")
    else:
        print("⚠️ No students found!")

def main():
    while True:
        print("\n===== Student Grades Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            try:
                grade = float(input("Enter student grade: "))
            except ValueError:
                print("⚠️ Grade must be a number!")
                continue
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name: ")
            try:
                grade = float(input("Enter new grade: "))
            except ValueError:
                print("⚠️ Grade must be a number!")
                continue
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name to delete: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("👋 Exiting program...")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
