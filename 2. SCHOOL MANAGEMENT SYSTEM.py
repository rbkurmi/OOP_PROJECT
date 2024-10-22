class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def assign_course(self, course):
        course.assign_teacher(self)
        print(f"Teacher {self.name} has been assigned to the course '{course.name}'.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll_in_course(self, course):
        self.courses.append(course)
        course.add_student(self)
        print(f"Student {self.name} has enrolled in the course '{course.name}'.")


class Course:
    def __init__(self, name):
        self.name = name
        self.teacher = None
        self.students = []

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def add_student(self, student):
        self.students.append(student)


# Function to simulate user interaction
def main():
    # Create teacher
    teacher_name = input("Enter teacher's name: ")
    teacher_age = int(input(f"Enter {teacher_name}'s age: "))
    subject = input(f"Enter {teacher_name}'s subject: ")
    teacher = Teacher(teacher_name, teacher_age, subject)

    # Create course
    course_name = input(f"Enter the name of the course to assign to {teacher.name}: ")
    course = Course(course_name)

    # Assign teacher to the course
    teacher.assign_course(course)

    # Enroll students
    num_students = int(input("How many students are enrolling? "))
    for _ in range(num_students):
        student_name = input("Enter student's name: ")
        student_age = int(input(f"Enter {student_name}'s age: "))
        student_id = input(f"Enter {student_name}'s student ID: ")
        student = Student(student_name, student_age, student_id)
        student.enroll_in_course(course)

    # Display course details
    print(f"\nCourse: {course.name}")
    print(f"Teacher: {course.teacher.name} (Subject: {course.teacher.subject})")
    print("Enrolled Students:")
    for student in course.students:
        print(f"- {student.name} (ID: {student.student_id})")


# Run the interactive simulation
if __name__ == "__main__":
    main()
