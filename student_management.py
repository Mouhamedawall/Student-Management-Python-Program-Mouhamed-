import tkinter as tk
from tkinter import messagebox, simpledialog
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
    student_id = simpledialog.askstring("Add Student", "Enter Student ID:")
    if student_id in students:
        messagebox.showerror("Error", "Student ID already exists!")
        return
    name = simpledialog.askstring("Add Student", "Enter Name:")
    age = simpledialog.askinteger("Add Student", "Enter Age:")
    grade_level = simpledialog.askstring("Add Student", "Enter Grade Level:")
    students[student_id] = {
        "Name": name,
        "Age": age,
        "Grade Level": grade_level,
        "Grades": []
    }
    messagebox.showinfo("Success", "Student added successfully!")


# Enter grades for a student
def enter_grades():
    student_id = simpledialog.askstring("Enter Grades", "Enter Student ID:")
    if student_id not in students:
        messagebox.showerror("Error", "Student not found!")
        return
    subjects = ["Informatique", "Math", "Science", "English", "Droit", "Electrotechnique", "Technologie"]
    grades = []
    for subject in subjects:
        grade = simpledialog.askfloat("Enter Grades", f"Enter grade for {subject}:")
        grades.append(grade)
    students[student_id]["Grades"] = grades
    messagebox.showinfo("Success", "Grades entered successfully!")


# Calculate average and grade category
def calculate_average(student_id):
    grades = students[student_id]["Grades"]
    if not grades:
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
        messagebox.showinfo("Info", "No students found!")
        return
    output = ""
    for student_id, details in students.items():
        output += f"ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grade Level: {details['Grade Level']}\n"
        if details["Grades"]:
            average, category = calculate_average(student_id)
            output += f"  Grades: {details['Grades']}\n"
            output += f"  Average: {average:.2f}, Category: {category}\n"
        else:
            output += "  No grades available.\n"
    messagebox.showinfo("All Students", output)


# Search for a student
def search_student():
    query = simpledialog.askstring("Search", "Search by ID or Name:").strip().lower()
    found = False
    output = ""
    for student_id, details in students.items():
        if query == student_id.lower() or query == details["Name"].lower():
            found = True
            output += f"ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grade Level: {details['Grade Level']}\n"
            if details["Grades"]:
                average, category = calculate_average(student_id)
                output += f"  Grades: {details['Grades']}\n"
                output += f"  Average: {average:.2f}, Category: {category}\n"
            else:
                output += "  No grades available.\n"
    if found:
        messagebox.showinfo("Search Results", output)
    else:
        messagebox.showerror("Error", "Student not found!")


# Exit the program
def exit_program():
    save_students()
    root.destroy()


# GUI Application
root = tk.Tk()
root.title("Student Management System")

load_students()

tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="Enter Grades", command=enter_grades).pack(pady=5)
tk.Button(root, text="Display All Students", command=display_all_students).pack(pady=5)
tk.Button(root, text="Search for a Student", command=search_student).pack(pady=5)
tk.Button(root, text="Exit", command=exit_program).pack(pady=5)

root.mainloop()
