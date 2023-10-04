thang = int (input("Mời bạn nhập vào tháng: "))

import array as arr
tenThang_array = ["Tháng một", "Tháng hai", "Tháng ba", "Tháng bốn",
    "Tháng năm", "Tháng sáu", "Tháng bảy", "Tháng tám",
    "Tháng chín", "Tháng mười", "Tháng mười một", "Tháng mười hai"]

if (thang < 1 or thang > 12):
        print("Số nguyên không được nhỏ hơn 1 và lớn hơn 12 ")
        exit()

print(tenThang_array[thang-1])

