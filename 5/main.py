# Khương đẹp zai !
a = int (input('Mời bạn nhập số a = '))
b = int (input('Mời bạn nhập số b = '))
if b == 0:
    print("Số chia không được nhập số 0")
    exit()
else:
    s = float (a / b)
    print(f"Thương của hai số nguyên {a} / {b} =  ",s)