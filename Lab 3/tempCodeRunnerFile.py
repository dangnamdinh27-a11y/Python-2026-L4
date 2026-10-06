from input import input_students, input_courses, input_marks
from output import (
    display_students,
    display_courses,
    display_marks_for_course,
    display_ranked_students
)

def main():
    # Khởi tạo 3 "chiếc giỏ" lưu trữ dữ liệu chính cho toàn bộ chương trình
    students = []
    courses = []
    marks = {}

    while True:
        print("\n================ MEUN QUẢN LÝ SINH VIÊN ================")
        print("1. Nhập danh sách sinh viên")
        print("2. Nhập danh sách môn học")
        print("3. Nhập điểm môn học")
        print("4. Hiển thị danh sách sinh viên")
        print("5. Hiển thị danh sách môn học")
        print("6. Xem bảng điểm theo môn học")
        print("7. Hiển thị Bảng xếp hạng sinh viên (GPA)")
        print("0. Thoát chương trình")
        print("========================================================")

        choice = input("Lựa chọn của bạn (0-7): ")

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
            print("Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

# Cú pháp giúp Python nhận diện đây là điểm xuất phát chính của chương trình
if __name__ == "__main__":
    main()