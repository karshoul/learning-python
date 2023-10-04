numBer = int (input("Mời bạn nhập một số: "))
i = 0

print(f"Các số lẻ từ 1 đến {numBer} là: ")
while(i <= numBer):
    i+=1
    if(i % 2 != 0):
        print(i)

