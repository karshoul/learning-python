from datetime import datetime

tuoi = int (input("Mời bạn nhập vào tuổi: "))
namHienTai = datetime.now().year
namSinh = namHienTai - tuoi
print(f"Năm sinh của bạn là: {namSinh}")