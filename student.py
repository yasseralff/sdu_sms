from person import Person


class Student(Person):
    def __init__(self, student_id, name, email):
        super().__init__(name, email)
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def get_courses(self):
        return self.courses

    def id_number(self):
        return self.student_id

    def get_gpa(self):
        # calculate GPA based on courses and grades
        total_credits = 0
        total_grade_points = 0
        for course in self.courses:
            total_credits += course.credits
            total_grade_points += course.grade * course.credits
        try:
            return total_grade_points / total_credits
        except ZeroDivisionError:
            return "No courses are registered."


class Course:
    def __init__(self, course_id, course_name, credits, grade=None):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.grade = grade / 100 * 4

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade
