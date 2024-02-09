
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)
        print(f"{self.name} has enrolled in {course.course_name}.")


    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print("Enrolled Courses:")
        for course in self.courses:
            print(f" - {course.course_name}")

class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)
        course.set_teacher(self)
        print(f"{self.name} is now teaching {course.course_name}.")

    def display_info(self):
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")
        print("Courses Taught:")
        for course in self.courses_taught:
            print(f" - {course.course_name}")

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher = None
        self.students = []

    def set_teacher(self, teacher):
        self.teacher = teacher

    def add_student(self, student):
        self.students.append(student)

    def display_info(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        if self.teacher:
            print(f"Teacher: {self.teacher.name}")
        print("Enrolled Students:")
        for student in self.students:
            print(f" - {student.name}")

# Example usage
if __name__ == "__main__":
    # Creating instances of classes
    math_teacher = Teacher(1, "Mr. Smith", "Math")
    english_teacher = Teacher(2, "Ms. Johnson", "English")

    math_course = Course(101, "Mathematics")
    english_course = Course(102, "English Literature")

    student1 = Student(101, "John Doe", 10)
    student2 = Student(102, "Jane Smith", 11)

    # Assigning teachers to courses
    math_teacher.assign_course(math_course)
    english_teacher.assign_course(english_course)

    # Enrolling students in courses
    student1.enroll(math_course)
    student2.enroll(english_course)

    # Displaying information
    print("\nTeacher Information:")
    math_teacher.display_info()
    english_teacher.display_info()

    print("\nStudent Information:")
    student1.display_info()
    student2.display_info()

    print("\nCourse Information:")
    math_course.display_info()
    english_course.display_info()

