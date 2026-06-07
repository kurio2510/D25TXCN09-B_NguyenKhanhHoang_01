import json

students = []

def xep_loai(diem_tb):
    if diem_tb < 5:
        return "Yếu"
    elif diem_tb < 7:
        return "Trung Bình"
    elif diem_tb < 8:
        return "Khá"
    else:
        return "Giỏi"

def tinh_diem_tb(toan, ly, hoa):
    return round((toan + ly + hoa) / 3, 2)

def load_data():
    global students

    try:
        with open("data.json", "r", encoding="utf-8") as file:
            students = json.load(file)
    except:
        students = []

def save_data():
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)

def hien_thi():

    if len(students) == 0:
        print("Danh sach rong!")
        return

    print("-" * 90)
    print(
        f"{'Ma SV':<10}{'Ten':<25}{'Toan':<10}{'Ly':<10}{'Hoa':<10}{'TB':<10}{'Xep Loai'}")
    print("-" * 90)

    for sv in students:
        print(
            f"{sv['ma_sv']:<10}"
            f"{sv['ten']:<25}"
            f"{sv['toan']:<10}"
            f"{sv['ly']:<10}"
            f"{sv['hoa']:<10}"
            f"{sv['diem_tb']:<10}"
            f"{sv['xep_loai']}"
        )

def them_sinh_vien():
    ma_sv = input("Nhập mã sinh viên: ")

    for sv in students:
        if sv["ma_sv"] == ma_sv:
            print("Mã sinh viên đã tồn tại!")
            return

    ten = input("Nhập tên sinh viên: ")

    toan = float(input("Nhập điểm toán: "))
    ly = float(input("Nhập điểm lý: "))
    hoa = float(input("Nhập điểm hóa: "))

    if not (0 <= toan <= 10 and 0 <= ly <= 10 and 0 <= hoa <= 10):
        print("Điểm phải nằm trong khoảng 0-10!")
        return

    diem_tb = tinh_diem_tb(toan, ly, hoa)

    student = {
        "ma_sv": ma_sv,
        "ten": ten,
        "toan": toan,
        "ly": ly,
        "hoa": hoa,
        "diem_tb": diem_tb,
        "xep_loai": xep_loai(diem_tb)
    }

    students.append(student)

    save_data()
    print("Thêm sinh viên thành công!")

def cap_nhat():
    ma_sv = input("Nhập mã sinh viên cần sửa: ")

    for sv in students:
        if sv["ma_sv"] == ma_sv:

            sv["toan"] = float(input("Nhập điểm toán mới: "))
            sv["ly"] = float(input("Nhập điểm lý mới: "))
            sv["hoa"] = float(input("Nhập điểm hóa mới: "))

            sv["diem_tb"] = tinh_diem_tb(
                sv["toan"],
                sv["ly"],
                sv["hoa"]
            )

            sv["xep_loai"] = xep_loai(sv["diem_tb"])

            save_data()

            print("Cập nhật thành công!")
            return

    print("Không tìm thấy sinh viên!")

def xoa():
    ma_sv = input("Nhập mã sinh viên cần xóa: ")

    for sv in students:
        if sv["ma_sv"] == ma_sv:

            while True:
                confirm = input("Ban co chac muon xoa? (y/n): ").lower()
                if confirm == "y":
                    students.remove(sv)
                    save_data()
                    print("Da xoa thanh cong!")
                    return
                elif confirm == "n":
                    print("Da huy xoa!")
                    return
                else:
                    print("Vui long nhap y hoac n!")

def tim_kiem():
    keyword = input("Nhập tên hoặc mã sinh viên: ").lower()

    found = False

    for sv in students:
        if (keyword in sv["ten"].lower()
                or keyword == sv["ma_sv"].lower()):

            print(sv)
            found = True

    if not found:
        print("Không tìm thấy sinh viên!")

def sap_xep():
    print("1. Điểm TB giảm dần")
    print("2. Tên A-Z")

    choice = input("Chọn: ")

    if choice == "1":
        students.sort(
            key=lambda sv: sv["diem_tb"],
            reverse=True
        )
    elif choice == "2":
        students.sort(key=lambda sv: sv["ten"].lower())
    else:
        print("Lựa chọn không hợp lệ!")
        return

    print("Sắp xếp thành công!")
    hien_thi()

def thong_ke():
    gioi = 0
    kha = 0
    tb = 0
    yeu = 0

    for sv in students:

        if sv["xep_loai"] == "Giỏi":
            gioi += 1
        elif sv["xep_loai"] == "Khá":
            kha += 1
        elif sv["xep_loai"] == "Trung Bình":
            tb += 1
        else:
            yeu += 1

    print(f"Gioi: {gioi}")
    print(f"Kha: {kha}")
    print(f"Trung Binh: {tb}")
    print(f"Yeu: {yeu}")

def max_min():
    if len(students) == 0:
        print("Danh sách rỗng!")
        return
    max_sv = max(
        students,
        key=lambda sv: sv["diem_tb"]
    )
    min_sv = min(
        students,
        key=lambda sv: sv["diem_tb"]
    )
    print("\nSinh vien diem cao nhat:")
    print(max_sv)

    print("\nSinh vien diem thap nhat:")
    print(min_sv)

def phan_loai():
    for sv in students:
        print(
            f"{sv['ma_sv']} - "
            f"{sv['ten']} - "
            f"{sv['xep_loai']}"
        )

def menu():
    load_data()

    while True:
        print("""
========== QUẢN LÝ SINH VIÊN ==========
1. Hiển thị danh sách sinh viên
2. Thêm mới sinh viên
3. Cập nhật sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên
6. Sắp xếp danh sách
7. Thống kê điểm trung bình
8. Liệt kê điểm cao nhất/thấp nhất
9. Phân loại học lực
10. Thoát
=======================================""")
        choice = input("Nhập lựa chọn: ")
        if choice == "1":
            hien_thi()
        elif choice == "2":
            them_sinh_vien()
        elif choice == "3":
            cap_nhat()
        elif choice == "4":
            xoa()
        elif choice == "5":
            tim_kiem()
        elif choice == "6":
            sap_xep()
        elif choice == "7":
            thong_ke()
        elif choice == "8":
            max_min()
        elif choice == "9":
            phan_loai()
        elif choice == "10":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")
menu()
