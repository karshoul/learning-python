thang = int (input("Mời bạn nhập vào tháng: "))

import array as arr
tenThang_array = ["Tháng một", "Tháng hai", "Tháng ba", "Tháng bốn",
    "Tháng năm", "Tháng sáu", "Tháng bảy", "Tháng tám",
    "Tháng chín", "Tháng mười", "Tháng mười một", "Tháng mười hai"]

if (thang < 1 or thang > 12):
        print("Số nguyên không được nhỏ hơn 1 và lớn hơn 12 ")
        exit()
if (thang == 1):
        print(tenThang_array[0])
if (thang == 2):
        print(tenThang_array[1])
if (thang == 3):
        print(tenThang_array[2])
if (thang == 4):
        print(tenThang_array[3])
if (thang == 5):
        print(tenThang_array[4])
if (thang == 6):
        print(tenThang_array[5])
if (thang == 7):
        print(tenThang_array[6])
if (thang == 8):
        print(tenThang_array[7])
if (thang == 9):
        print(tenThang_array[8])
if (thang == 10):
        print(tenThang_array[9])
if (thang == 11):
        print(tenThang_array[10])
if (thang == 12):
        print(tenThang_array[11])

