import math
from Domain.student import Student
from Domain.course import Course

def input_students(students):
    num_student = int(input("Enter number of students: "))
    for i in range(num_student):
        print(f"\nInformation of student {i+1}:")
        s_id = input("Student ID: ")
        s_name = input("Full name: ")
        s_dob = input("Date of birth: ")
        student = Student(s_id, s_name, s_dob)
        students.append(student)

def input_courses(courses):
    num_course = int(input("Enter number of courses: "))
    for i in range(num_course):
        print(f"\nInformation of course {i+1}:")
        c_name = input("Course name: ")
        c_id = input("Course ID: ")
        c_credits = int(input("Number of credits: "))
        course = Course(c_name, c_id, c_credits)
        courses.append(course)

def input_marks(courses, students, marks):
    print("\n=== Enter Marks for Courses ===")
    for course in courses:
        print(f"\nEntering marks for course: {course.name} (ID: {course.id})")
        marks[course.id] = {}
        for student in students:
            raw_mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
            rounded_mark = math.floor(raw_mark * 10) / 10  # Round down to one decimal place
            marks[course.id][student.id] = rounded_mark