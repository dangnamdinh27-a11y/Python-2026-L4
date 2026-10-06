import numpy as np

def calculate_gpa(student_id, courses, marks):
    student_marks = []
    student_credits = []
    
    for course in courses:
        if course.id in marks and student_id in marks[course.id]:
            student_marks.append(marks[course.id][student_id])
            student_credits.append(course.credits)
            
    if not student_marks:
        return 0.0
        
    marks_array = np.array(student_marks)
    credits_array = np.array(student_credits)
    gpa = np.average(marks_array, weights=credits_array)
    
    return round(float(gpa), 2)

def display_students(students):
    print("\n=== STUDENT LIST ===")
    if not students:
        print("No students found!")
        return
    for s in students:
        print(f"ID: {s.id} | Name: {s.name} | Date of Birth: {s.dob}")

def display_courses(courses):
    print("\n=== COURSE LIST ===")
    if not courses:
        print("No courses found!")
        return
    for c in courses:
        print(f"ID: {c.id} | Course Name: {c.name} | Credits: {c.credits}")

def display_marks_for_course(courses, students, marks):
    c_id = input("\n Enter the course ID to view marks: ")
    if c_id in marks:
        print(f"\n--- MARKS SHEET FOR COURSE {c_id} ---")
        for s in students:
            mark = marks[c_id].get(s.id, "N/A")
            print(f"Student: {s.name} (ID: {s.id}) -> Mark: {mark}")
    else:
        print("This course has no marks available!")

def display_ranked_students(students, courses, marks):
    if not students:
        print("\nNo students found!")
        return

    # 1. Tính và cập nhật GPA trực tiếp vào thuộc tính .gpa của từng đối tượng Student
    for s in students:
        s.gpa = calculate_gpa(s.id, courses, marks)
        
    # 2. Sắp xếp danh sách sinh viên theo GPA giảm dần
    students.sort(key=lambda s: s.gpa, reverse=True)
    
    # 3. In bảng xếp hạng
    print("\n=== RANKING TABLE BY GPA (DESCENDING) ===")
    for idx, s in enumerate(students, start=1):
        print(f"Rank {idx} | Student: {s.name} (ID: {s.id}) | GPA: {s.gpa}")