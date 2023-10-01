from datetime import datetime

namSinh = int (input("Mời bạn nhập vào năm sinh: "))
namHienTai = datetime().year
tuoi = namHienTai - namSinh
print(f"Tuổi của bạn là: {tuoi}")