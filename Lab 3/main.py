from input import input_students, input_courses, input_marks
from output import (
    display_students,
    display_courses,
    display_marks_for_course,
    display_ranked_students
)

def main():
    students = []
    courses = []
    marks = {}

    while True:
        print("\n================ STUDENT MANAGEMENT ================")
        print("1. Input student list")
        print("2. Input course list")
        print("3. Input course marks")
        print("4. Display student list")
        print("5. Display course list")
        print("6. View mark sheet by course")
        print("7. Display ranked students by GPA")
        print("0. Exit program")
        print("========================================================")

        choice = input("Your choice (0-7): ")

        if choice == '1':
            input_students(students)
        elif choice == '2':
            input_courses(courses)
        elif choice == '3':
            input_marks(courses, students, marks)
        elif choice == '4':
            display_students(students)
        elif choice == '5':
            display_courses(courses)
        elif choice == '6':
            display_marks_for_course(courses, students, marks)
        elif choice == '7':
            display_ranked_students(students, courses, marks)
        elif choice == '0':
            print("Exited program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")


if __name__ == "__main__":
    main()