n = int(input())
a = 0
b = 1
tong = 0
for i in range(n):
    print(a, end=' ')
    tong += a
    a, b = b,a + b
print(f"Tổng: {tong}")