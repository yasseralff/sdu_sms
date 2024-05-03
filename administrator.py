from person import Person
from student import Course


class Administrator(Person):
    def __init__(self, admin_id, password, name, email):
        super().__init__(name, email)
        self.__admin_id = admin_id
        self.__password = password
        self.students = []

    def get_id(self):
        return self.__admin_id

    def get_pass(self):
        return self.__password

    def add_student(self, student):
        self.students.append(student)

    def update_student(self, student_id, name, email):
        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                student.email = email
                return
        print("Student not found")

    def add_report(self, student_id, course_id, course_name, credits, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_course(Course(course_id, course_name, credits, grade))
                return
        print("Student not found")

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return
        print("Student not found")

    def get_gpa(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(f"Student Report: {student.name} ({student.id_number()})")
                print(f"  GPA: {student.get_gpa()}/4.0")
                print("  Courses:")
                for course in student.get_courses():
                    print(f"    {course.course_name} ({course.credits} credits, Grade: {course.grade}/4.0)")
                return
        print("Student not found")
