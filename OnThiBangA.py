n = int(input(""))
tong = 0
dem = 0
t = 1
i = 2

while t <= n:             # Tính tổng các số từ 1 đến n chia hết cho 3 hoặc 5
    if t % 3 == 0 or t % 5 == 0:
        tong += t
    t += 1
print(tong)

while i <= n :            # Đếm số lượng số nguyên tố từ 2 đến n
    kiem_tra = True  #Bắt đầu kiểm tra số nguyên tố
    j = 2

    while j < i:
        if i % j == 0:  # TH không phải là số nguyên tố
            kiem_tra = False 
            break
        j += 1
    if kiem_tra:
        dem += 1
    i += 1
print(dem)

if n <= 1:                 #Kiểm tra n có phải số nguyên tố hay không
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

tich = 1              # Tính giai thừa
k = 1
while k <= n:
    tich *= k #
    k += 1
    
max_val = 0     # min_val = n + 1      # Nhập số nguyên n. Tìm số lớn nhất từ 1 → n chia hết cho 2 và 3 nhưng không chia hết cho 5. Nếu không có số nào thì in 0.
l = 1
while l <= n:
    if l % 2 == 0 and l % 3 == 0 and l % 5 != 0:
        if l > max_val: # i < min_val
            max_val = l # min_val = i

    l += 1

print(max_val) # print(min_val)


max_digit = 0 # Nhập số nguyên n. In ra chữ số lớn nhất và chữ số nhỏ nhất của n.Input:482915 Output:9 1 (max = 9 ; min = 1)
min_digit = 9
while n > 0: #
    digit = n % 10 #
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    n //= 10 #
print(max_digit, min_digit)
