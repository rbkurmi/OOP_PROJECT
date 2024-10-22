class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id
        self.courses = []

    def enroll_in_course(self, course):
        self.courses.append(course)


class Professor(Person):
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)


class Course:
    def __init__(self, name, professor):
        self.name = name
        self.professor = professor
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# Function to create a student
def create_student():
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    student_id = input("Enter student ID: ")
    return Student(name, email, student_id)


# Function to create a professor
def create_professor():
    name = input("Enter professor name: ")
    email = input("Enter professor email: ")
    department = input("Enter department: ")
    return Professor(name, email, department)


# Function to create a course
def create_course(professor):
    name = input("Enter course name: ")
    return Course(name, professor)


# Main function to run the program
def main():
    print("Creating a new professor...")
    professor = create_professor()

    print("Creating a new course for the professor...")
    course = create_course(professor)

    print("Creating a new student...")
    student = create_student()

    # Enroll the student in the course and add the student to the course
    student.enroll_in_course(course)
    course.add_student(student)

    print(f"\nProfessor {professor.name} has created the course '{course.name}'.")
    print(f"Student {student.name} has been enrolled in '{course.name}'.")


if __name__ == "__main__":
    main()
