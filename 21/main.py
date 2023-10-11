chuoi = input("Mời bạn nhập vào một chuỗi: ")
kyTuTrungNhau_array = [] #danh sách để lưu các ký tự trùng nhau

for kyTu in chuoi:

    # Kiểm tra xem ký tự đã xuất hiện trước đó trong danh sách ký tự trùng nhau chưa
    # và ký tự đó xuất hiện nhiều hơn một lần trong chuỗi 

    if chuoi.count(kyTu) > 1 and kyTu not in kyTuTrungNhau_array:
        kyTuTrungNhau_array.append(kyTu) # # Nếu thỏa điều kiện, thêm ký tự vào danh sách ký tự trùng nhau
    
print("Các ký tự trùng nhau trong chuỗi: ", kyTuTrungNhau_array)