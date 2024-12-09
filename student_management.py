import os
import subprocess

# Main Program Logic
def student_management():
    import os

    # File to store student records
    FILE_NAME = "students.txt"

    # Initialize data structure
    students = {}

    # Load students from file
    def load_students():
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    student_id, name, age, grade_level, *grades = data
                    students[student_id] = {
                        "Name": name,
                        "Age": int(age),
                        "Grade Level": grade_level,
                        "Grades": list(map(float, grades)) if grades else []
                    }

    # Save students to file
    def save_students():
        with open(FILE_NAME, "w") as file:
            for student_id, details in students.items():
                record = [
                    student_id,
                    details["Name"],
                    str(details["Age"]),
                    details["Grade Level"],
                    *map(str, details["Grades"])
                ]
                file.write(",".join(record) + "\n")

    # Add a new student
    def add_student():
        student_id = input("Enter Student ID: ").strip()
        if student_id in students:
            print("Student ID already exists!")
            return
        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        grade_level = input("Enter Grade Level: ").strip()
        students[student_id] = {
            "Name": name,
            "Age": age,
            "Grade Level": grade_level,
            "Grades": []
        }
        print("Student added successfully!")

    # Enter grades for a student
    def enter_grades():
        student_id = input("Enter Student ID: ").strip()
        if student_id not in students:
            print("Student not found!")
            return
        subjects = ["Informatique", "Math", "Science", "English", "Droit", "Electrotechnique", "Technologie"]
        grades = []
        print("Enter grades for each subject:")
        for subject in subjects:
            grade = float(input(f"{subject}: "))
            grades.append(grade)
        students[student_id]["Grades"] = grades
        print("Grades entered successfully!")

    # Calculate average and grade category
    def calculate_average(student_id):
        if student_id not in students:
            print("Student not found!")
            return None, None
        grades = students[student_id]["Grades"]
        if not grades:
            print("No grades available for this student!")
            return None, None
        average = sum(grades) / len(grades)
        if average >= 90:
            category = "A"
        elif average >= 80:
            category = "B"
        elif average >= 70:
            category = "C"
        elif average >= 60:
            category = "D"
        else:
            category = "F"
        return average, category

    # Display all student records
    def display_all_students():
        if not students:
            print("No students found!")
            return
        for student_id, details in students.items():
            print(f"ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grade Level: {details['Grade Level']}")
            if details["Grades"]:
                average, category = calculate_average(student_id)
                print(f"  Grades: {details['Grades']}")
                print(f"  Average: {average:.2f}, Category: {category}")
            else:
                print("  No grades available.")

    # Search for a student
    def search_student():
        query = input("Search by ID or Name: ").strip().lower()
        found = False
        for student_id, details in students.items():
            if query == student_id.lower() or query == details["Name"].lower():
                found = True
                print(f"ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grade Level: {details['Grade Level']}")
                if details["Grades"]:
                    average, category = calculate_average(student_id)
                    print(f"  Grades: {details['Grades']}")
                    print(f"  Average: {average:.2f}, Category: {category}")
                else:
                    print("  No grades available.")
        if not found:
            print("Student not found!")

    # Main menu
    def main_menu():
        load_students()
        while True:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. Enter Grades")
            print("3. Calculate Average")
            print("4. Display All Student Records")
            print("5. Search for a Student")
            print("6. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                add_student()
            elif choice == "2":
                enter_grades()
            elif choice == "3":
                student_id = input("Enter Student ID: ").strip()
                average, category = calculate_average(student_id)
                if average is not None:
                    print(f"Average: {average:.2f}, Category: {category}")
            elif choice == "4":
                display_all_students()
            elif choice == "5":
                search_student()
            elif choice == "6":
                save_students()
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

    main_menu()

# Automatic EXE File Creation
def create_exe():
    print("Creating EXE file...")
    if not os.path.exists("student_management.py"):
        print("Script file 'student_management.py' not found! Save the script as 'student_management.py'.")
        return
    subprocess.run(["pyinstaller", "--onefile", "student_management.py"], check=True)
    print("EXE file created in the 'dist' folder.")

if __name__ == "__main__":
    action = input("Enter 'run' to run the program or 'build' to create the EXE file: ").strip().lower()
    if action == "run":
        student_management()
    elif action == "build":
        create_exe()
    else:
        print("Invalid option!")
