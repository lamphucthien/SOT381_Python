n = int(input(""))
tong = 0
dem = 0
t = 1
i = 2

while t <= n: # Tính tổng các số từ 1 đến n chia hết cho 3 hoặc 5
    if t % 3 == 0 or t % 5 == 0:
        tong += t
    t += 1
print(tong)

while i <= n : # Đếm số lượng số nguyên tố từ 2 đến n
    kiem_tra = True
    j = 2

    while j < i:
        if i % j == 0:
            kiem_tra = False
            break
        j += 1
    if kiem_tra:
        dem += 1
    i += 1

print(dem)

if n <= 1: # Kiểm tra n có phải số nguyên tố hay không
    print("NO")
else:
    kiem_tra = True
    j = 2

    while j < n:
        if n % j == 0:
            kiem_tra = False
            break
        j += 1
    if kiem_tra:
        print("YES")
    else:
        print("NO")
