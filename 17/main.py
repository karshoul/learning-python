def hideMidCharacters(strInput):
    if len(strInput) < 3:
        return strInput  # Không làm gì cả nếu chuỗi có ít hơn 3 ký tự

    first_char = strInput[0]
    last_char = strInput[-1]
    middle_chars = '*' * (len(strInput) - 2)

    return first_char + middle_chars + last_char

# Nhập chuỗi từ người dùng
strInput = input("Nhập vào một chuỗi: ")

# Gọi hàm và in ra kết quả
resultStr = hideMidCharacters(strInput)
print(resultStr)


