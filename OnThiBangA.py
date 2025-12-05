n = int(input().strip())

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
    for j in range(2, int(i**0.5)):
        if i % j == 0:
            la_nt = False
            break
    if la_nt:
        dem += 1
print(dem)

# 3. Kiểm tra n có phải số nguyên tố không → YES/NO
n = int(input())
if n <= 1:
    print("NO")
elif n == 2:
    print("YES")
else:
     for i in range(2, n+1):
    la_nt = True
    for j in range(2, int(i**0.5)):
        if i % j == 0:
            la_nt = False
            break
    print("YES" if kiem_tra else "NO")
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
if n == 0:
    print(0, 0)
else:
    while n > 0:
        digit = n % 10
        if digit > max_val:
            max_val = digit
        if digit < min_val:
            min_val = digit
        n //= 10
    print(max_val, min_val)

#7 Đảo ngược số nguyên
n = int(input())
r = 0
while n > 0:
    digit = n % 10
    r = r * 10 + digit
    n = n // 10
print(r)

#8 Tổng chữ số
n = int(input().strip())
tong = 0
while n > 0:
    digit = n % 10
    n //= 10
    tong += digit
print(tong)

#9 Fibonacci

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
a = 0
b = 1
i = 2
while i <= n:
    c = a + b
    a = b
    b = c
    i += 1
print(b)

#10 Ước Chung Lớn Nhất (UCLN)
import sys
def main():
    a, b = map(int, sys.stdin.readline().split())
    while b:
        a, b = b, a%b
    print(a)
main()

#11 Tính 1+2+3...+n
n = int(input().strip())
tong = n * (n + 1) // 2
print(tong)

#12 In tam giác vuông
h = int(input().strip())

for i in range(1, h + 1):
    print('*' * i)

#13 kiểm tra số đối xứng ( kết hợp đảo ngược số và rẽ nhánh )
n = int(input())
temp = n # BẮT BUỘC PHẢI LƯU BIẾN TẠM TRONG BÀI NÀY
r = 0
while temp > 0:
    digit = temp % 10
    r = r * 10 + digit
    temp //= 10
if n == r: #
    print("YES")
else:
    print("NO")

# Bài FOR8 Ntucoder
n = int(input())
MOD = 10**9 + 7

u1, u2 = 1, 1

for i in range(n - 2):
    u1, u2 = u2, (3 * u2 - u1) % MOD

print(u2)

#14 Kiểm tra số chính phương
import math
a = int(input())
can = math.sqrt(a) # Căn a 
can_nguyen = round(can) # Làm tròn số vừa căn
if can_nguyen * can_nguyen == a: # nhân ngược lại xem có bằng số cần kiểm tra
    print("YES")
else:
    print("NO")

#15 Đếm số lượng số 0 sau N!
import sys
n = int(sys.stdin.read())
dem = 0
while n >= 5:
    n //= 5
    dem += n
print(dem)
