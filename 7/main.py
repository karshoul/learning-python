a = input('Mời bạn nhập cạnh hình vuông: ')

if a.isdigit() == False:
    print("Dữ liệu bạn nhập không phải là số.")
    exit()
else:
    s = int(a) * 4
    print(f'Chu vi hình vuông là: ', s)