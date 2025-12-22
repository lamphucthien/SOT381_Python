n = int(input("Nhập số lượng bài hát: "))
dsBaiHat = []
for i in range(n):
    tenBai = input(f"Tên bài thứ {i}: ")
    dsBaiHat.append(tenBai)

print("DANH SÁCH BÀI HÁT:")
for i in range(n):
    ten = dsBaiHat[i]
    print(f"Bài {i}: {ten}")

print("DANH SÁCH IN HOA:")
for i in range(n):
    ten = dsBaiHat[i]
    TEN = ten.upper()
    print(f"Bài {i}: {TEN}")

print("CÁC BÀI CÓ TỪ 'YÊU':")
for i in range(n):
    ten = dsBaiHat[i]
    if "yêu" in ten.lower():
        print(f"Bài {i}: {ten}")

print("BÀI CÓ TÊN DÀI NHẤT:")
tenBaiDaiNhat = dsBaiHat[0]
soTuCuaBaiDaiNhat = len(tenBaiDaiNhat.split())
vitriCuaBai = 0
for i in range(n):
    tenBai = dsBaiHat[i]
    soTu = len(tenBai.split())

    if soTu > soTuCuaBaiDaiNhat:
        vitriCuaBai = i
        tenBaiDaiNhat = tenBai
        soTuCuaBaiDaiNhat = soTu
print(f"Bài: '{tenBaiDaiNhat}' ở vị trí {vitriCuaBai} có {soTuCuaBaiDaiNhat} từ")