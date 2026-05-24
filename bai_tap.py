order_list = ["GE001", "GE002", "GE003", "GE004"]


while True:
    print("""
    ========== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
    1. Hiển thị danh sách đơn hàng
    2. Thêm đơn hàng mới
    3. Xóa đơn hàng theo mã
    4. Thoát chương trình
    """)
    choice = input("Nhập lựa chọn của bạn")
    if choice.strip() == "1":
        print("===Danh sách đơn hàng hiện tại===")
        if len(order_list) == 0:
            print("----Danh sách đang trống----")
        elif len(order_list) > 0:
            for orders in range(0 , len(order_list)):
                 print(f"{orders + 1} - {order_list[orders]}")
    elif choice.strip() == "2":
        order_name = input("Nhập mã đơn hàng mới")
        if order_name.strip() == "":
            print("Đề nghị không được bỏ trống!")
        elif order_name.upper() in order_list:
            print(f"Đơn hàng {order_name} đã tồn tại!")
        else:
            order_list.append(order_name.upper())
            print(f"Đã nhập hàng {order_name} vào order!!")

    elif choice.strip() == "3":
        order_namedelete = input("Nhập đơn hàng bạn muốn xóa")
        if order_namedelete.strip() == "":
            print("Vui lòng không được để trống thông tin")
        elif order_namedelete.upper().strip() in order_list:
            found_order_index = order_list.index(order_namedelete.upper())
            order_list.pop(found_order_index)
        else:
            print("Vui lòng nhập đúng tên đơn hàng")
    elif choice.strip() == "4":
        print("-------- Thoát chương trình ------")
        break
    else:
        print("Vui lòng nhập đúng lựa chọn")