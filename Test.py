n = int(input())
tong = 0
i = 2

while i <= n:
    kiem_tra = True #Kiểm tra số nguyên tố
    j = 2

    while j < i:
        if i % j == 0:
            kiem_tra = False
            break
        j += 1

    if kiem_tra:
        tong += i
    i += 1

print(tong)