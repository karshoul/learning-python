from datetime import datetime

namSinh = int (input("Mời bạn nhập vào năm sinh: "))
namHienTai = datetime.now().year
tuoi = namHienTai - namSinh
print(f"Tuổi của bạn là: {tuoi}")