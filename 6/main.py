a = input(("Mời bạn nhập chiều dài và chiều rộng của hình vuông: "))
if a.isdigit() == False:
 print("Dữ liệu bạn nhập không phải là số.")
 exit()
else:
 s = int(a) * int(a)
print(f" Diện tích hình vuông: {a} x {a} = {s}")