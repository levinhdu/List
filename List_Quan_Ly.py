students = [
    ["001","Lê Vinh Dự","Nam","Quảng Nam","75","90"],
    ["002","Ngô Mỹ Uyên","Nữ","Quảng Nam","65","90"]
]

def students_list(students):
    id = input("Nhập mã số: ")
    full_name = input("Nhập họ tên: ")
    gender = input("Nhập giới tính: ")
    province = input("Nhập Tỉnh/Thành phố: ")
    theory = input("Nhập điểm lý thuyết: ")
    practice = input("Nhập điểm thực hành: ")
    new_student = []
    new_student.extend((id,full_name,gender,province,theory,practice))
    students.append(new_student)
    return students
def show_header():
    print(f"{'Mã số':<10}{'Họ tên':^20}{'Giới tính':^10}{'Tỉnh/Thành phố':<20}{'Điểm thi lý thuyết':<20}{'Điểm thi thực hành':<20}")


def show_students_list(students):
    show_header()
    for i in range(len(students)):
        id = students[i][0]
        full_name = students[i][1]
        gender = students[i][2]
        province = students[i][3]
        theory = students[i][4]
        practice = students[i][5]
        print(f"{id:<10}{full_name:^20}{gender:^10}{province:<20}{theory:<20}{practice:<20}")


def remove_students(students):
    remove_id = input("Nhập mã số sinh viên muốn xóa thông tin: ")
    for lst in students:
        for id in lst:
             if id == remove_id:
                students.remove(lst)
                break
    return students
def show_menu():
    print("""
    Hãy chọn tính năng muốn thực hiện.
    1. Thêm thông tin học viên vào bộ nhớ
    2. Hiển thị danh sách tất cả học viên
    3. Xóa thông tin của học viên
    4. Thoát chương trình
    """)

def get_choice():
    return input("Lựa chọn của bạn: ")


while  True:
    show_menu()
    use_choice = get_choice()
    print("Bạn đã chọn " + use_choice)
    if use_choice == "4":
        break
    elif use_choice == "1":
        students = students_list(students)
    elif use_choice == "2":
        show_students_list(students)
    elif use_choice == "3":
        students = remove_students(students)

