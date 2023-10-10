chuoi = input("Mời bạn nhập vào một chuỗi: ") 
soLuongSo = 0 

for kyTu in chuoi:
    if kyTu.isdigit(): # Kiểm tra xem ký tự có phải là số không
        soLuongSo+=1 # Nếu là số, tăng biến soLuongSo lên 1

print("Số lượng ký tự số của chuỗi là: ", soLuongSo)