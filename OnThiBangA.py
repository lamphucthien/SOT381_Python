n = int(input())

# 1. Tổng các số từ 1 đến n chia hết cho 3 hoặc 5
tong = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        tong += i
print(tong)

# 2. Đếm số lượng số nguyên tố từ 2 đến n
dem = 0
for i in range(2, n+1):
    la_nt = True
    for j in range(2, i):
        if i % j == 0:
            la_nt = False
            break
    if la_nt:
        dem += 1
print(dem)

# 3. Kiểm tra n có phải số nguyên tố không → YES/NO
if n <= 1:
    print("NO")
else:
    la_nt = True
    for j in range(2, n):
        if n % j == 0:
            la_nt = False
            break
    print("YES" if la_nt else "NO")

# 4. Tính giai thừa n!
tich = 1
for i in range(1, n+1):
    tich *= i
print(tich)

# 5. Số lớn nhất ≤ n chia hết cho 2 và 3, nhưng KHÔNG chia hết cho 5 (nếu không có → 0)
max_val = 0
for i in range(1, n+1):
    if i % 2 == 0 and i % 3 == 0 and i % 5 != 0:
        max_val = i        # tự động giữ lại số lớn nhất vì duyệt từ nhỏ → lớn
print(max_val)

# 6. In chữ số lớn nhất và nhỏ nhất của n (xử lý cả n=0 và số âm)
if n == 0:
    print(0, 0)
else:
    s = str(abs(n))           # chuyển thành chuỗi, abs để xử lý số âm
    max_digit = max(s)        # max chuỗi là chữ số lớn nhất
    min_digit = min(s)        # min chuỗi là chữ số nhỏ nhất
    print(max_digit, min_digit)
