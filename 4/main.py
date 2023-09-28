a = input('Mời bạn nhập số a = ')

if a.isdigit() == False:
    print("Dữ liệu bạn nhập không phải là số.")
    exit()
b = input('Mời bạn nhập số b = ')

if b.isdigit() == False:
    print("Dữ liệu bạn nhập không phải là số.")
    exit()
else:
    s = int(a) * int(b)
    print(f'Tích hai số nguyên {a} x {b} = ', s)