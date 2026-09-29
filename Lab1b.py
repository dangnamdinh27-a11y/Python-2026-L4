students = []
courses= []
marks = {}

#Student information
def input_student():
    num_student = int(input("Enter number of students: "))
    for i in range(num_student):
        print(f"\nInformation of student {i+1}:")
        s_id = input("Enter student ID: ")
        s_name = input("Enter student name: ")
        s_dob = input("Enter student date of birth: ")
        student_info = {"id": s_id, "name": s_name, "dob": s_dob}
        students.append(student_info)
input_student()

#Course information
def input_course():
    num_course = int(input("Enter number of courses: "))
    for i in range(num_course):
        print(f"\nInformation of course {i+1}:")
        c_name = input("Enter name of course: ")
        c_id = input("Enter ID of course: ")
        course_info = {"name": c_name, "id": c_id}
        courses.append(course_info)
input_course()

#Mark information
def mark_info():
    print(f"\nMark information:")
    for course in courses:
        c_id = course["id"]
        c_name = course["name"]
        print(f"\nEntering marks for course: {c_name} (ID: {c_id})")
        marks[c_id] = {}
        for student in students:
            s_id = student["id"]
            s_name = student["name"]
            mark = float(input(f"Enter mark for {s_name} (ID: {s_id}): "))
            marks[c_id][s_id] = mark
mark_info()

#Display functions
def list_students():
    print("\n=== LIST OF STUDENTS ===")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Date of Birth: {s['dob']}")

def list_courses():
    print("\n=== LIST OF COURSES ===")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def list_marks():
    print("\n=== LIST OF MARKS ===")
    course_id = input("Enter course ID to display marks: ")

    if course_id in marks:
        print(f"\nMarks for course ID {course_id}:")
        for s in students:
            s_id = s["id"]
            mark = marks[course_id].get(s_id, "N/A")
            print(f"Name: {s['name']} - ID: {s_id} - Mark: {mark}")
    else:
        print(f"No marks found for course ID {course_id}.")

list_students()
list_courses()
list_marks()