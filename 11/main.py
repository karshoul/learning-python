numBer = int (input("Mời bạn nhập một số bất kì: "))
tong = 0
i = 1

while i <= numBer:
    tong+=i
    i+=1

print(f"Tổng các số từ 1 đến {numBer} là: ", tong)