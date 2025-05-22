from QuanLySinhVien import QuanLySinhVien

qlsv=QuanLySinhVien()
while(1==1):
    print("\n CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("*************************MENU*******************************")
    print("** 1. Thêm sinh viên                                      **")
    print("** 2. Cập nhật thông tin sinh viên bởi ID                 **")
    print("** 3. Xóa sinh viên bởi ID                                **")
    print("** 4. Tìm kiếm sinh viên theo tên                         **")
    print("** 5. Sắp xếp sinh viên theo điểm trung bình              **")
    print("** 6. Sắp xếp sinh viên theo tên                          **")
    print("** 7. Hiển thị danh sách sinh viên                        **")
    print("** 0. Thoát                                               **")
    print("************************************************************")

    key=int(input("Nhập tùy chọn: "))
    if(key==1):
        print("\n1. Thêm sinh viên")
        qlsv.nhapSinhVien()
        print("\n Thêm sinh viên thành công")
    elif key==2:
        if qlsv.soLuongSinhVien()>0:
            print("\n2. Cập nhật thông tin sinh viên ")
            print("\n Nhập ID:")
            ID=int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên trống!")
    elif(key==3):
        if qlsv.soLuongSinhVien()>0:
            print("\n3. Xóa sinh viên")
            print("\n Nhập ID: ")
            ID=int(input())
            qlsv.deleteByID(ID)
        else:
            print("\nDanh sách trống")
    elif(key==4):
        if(qlsv.soLuongSinhVien()>0):
            print("\n4. Tìm kiếm sinh viên theo tên")
            print("\n Nhập tên để tìm kiếm: ")
            name=input()
            searchResult=qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên trống")
    elif key==5:
        if(qlsv.soLuongSinhVien()>0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình (GPA)")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách trống")
    elif key==6:
        if(qlsv.soLuongSinhVien()>0):
            print("\n5. Sắp xếp sinh viên theo tên")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách trống")
    elif key==7:
        if qlsv.soLuongSinhVien()>0:
            print("\n7. Hiển thị danh sách sinh viên")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách trống")
    elif key==0:
        print("\n Bạn đã chọn thoát khỏi chương trình")
        break
    else:
        print("\n Không có chức năng này!")
        print("\n Hãy chọn chức năng trong hộp menumenu")