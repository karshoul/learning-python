a = input('Moi ban nhap so a = ')

if a.isdigit() == False:
    print("Dữ liệu bạn nhập không phải là số.")
    exit()
b = input('Moi ban nhap so b = ')

if b.isdigit() == False:
    print("Dữ liệu bạn nhập không phải là số.")
    exit()
else:
    s = int(a) + int(b)
    print(f'Tong hai so nguyen {a} + {b} = ', s)