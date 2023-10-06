strInit = print("hello")
strInit_array = ['h', 'e', 'l', 'o', 'he', 'hl', 'ho', 
                 'eh', 'el', 'eo', 'lh', 'le', 'll', 'lo', 
                 'oh', 'oe', 'ol', 'oo']
strInput = input("Mời bạn nhập vào một chuỗi để kiểm tra: ")

if (strInput in strInit_array):
    print("Ok")
else:
    print("Not")


