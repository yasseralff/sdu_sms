from administrator import Administrator
from student import Student


def main():
    admin = Administrator("admin1", "12345678", "Inter Group", "intergroup@sdu.edu.kz")

    print("SDU University - Student Information System")
    print("Login")
    while True:
        userin = input("Enter username: ")
        passin = input("Enter password: ")
        if (userin == admin.get_id()) and (passin == admin.get_pass()):
            print(f"Welcome {admin.name}!")
            while True:
                print("1. Add Student")
                print("2. Update Student")
                print("3. Delete Student")
                print("4. Add Report")
                print("5. Generate Report")
                print("6. Quit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    student_id = input("Enter student ID: ")
                    name = input("Enter student name: ")
                    email = input("Enter student email: ")
                    student = Student(student_id, name, email)
                    admin.add_student(student)
                elif choice == "2":
                    student_id = input("Enter student ID: ")
                    name = input("Enter new student name: ")
                    email = input("Enter new student email: ")
                    admin.update_student(student_id, name, email)
                elif choice == "3":
                    student_id = input("Enter student ID: ")
                    admin.delete_student(student_id)
                elif choice == "4":
                    student_id = input("Enter student ID: ")
                    course_id = input("Enter course ID: ")
                    course_name = input("Enter course name: ")
                    credits = int(input("Enter number of credits: "))
                    grade = float(input("Enter grade: "))
                    admin.add_report(student_id, course_id, course_name, credits, grade)
                    print("Course added successfully")
                elif choice == "5":
                    student_id = input("Enter student ID: ")
                    admin.get_gpa(student_id)
                elif choice == "6":
                    break
                else:
                    print("Invalid choice. Please try again.")
            break

        else:
            print("Credential does not match!")



