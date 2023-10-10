chuoi = input("Mời bạn nhập vào một chuỗi: ")
chuoiMoi = ''

for kyTu in chuoi:
    if not kyTu.isdigit(): #Kiểm tra xem ký tự phải là số không
        chuoiMoi += kyTu # Nếu không phải là số, thêm ký tự vào chuỗi mới

print("Chuỗi mới đã loại bỏ số: ", chuoiMoi)