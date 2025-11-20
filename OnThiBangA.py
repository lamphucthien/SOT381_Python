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

n = int(input().strip()) # In bảng cửu chương n
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 6. In chữ số lớn nhất và nhỏ nhất của n 
n = int(input().strip())
max_val = 0
min_val = 9
while n > 0:
    digit = n % 10
    if digit > max_val:
        max_val = digit
    if digit < min_val:
        min_val = digit
    n //= 10
print(max_val, min_val)

#Tổng chữ số
n = int(input().strip())
tong = 0
while n > 0:
    degit = n % 10
    n //= 10
    tong += degit
print(tong)

# Fibonacci

# Dạng a — In n số đầu tiên

n = int(input())
a = 0
b = 1
i = 0
while i < n:
    print(a, end=' ')
    c = a + b
    a = b
    b = c
    i += 1

# Dạng b — Tìm số thứ n

n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a = 0
    b = 1
    i = 2
    while i <= n:
        c = a + b
        a = b
        b = c
        i += 1
    print(b)

#Ước Chung Lớn Nhất (UCLN)
a = int(input().strip())
b = int(input().strip())

# Lặp khi a và b chưa bằng nhau
while a != b:
    if a > b:
        a = a - b  # Nếu a lớn hơn, cắt bớt a
    else:
        b = b - a  # Nếu b lớn hơn, cắt bớt b

# Khi vòng lặp dừng, a và b bằng nhau và chính là UCLN
print(a)
