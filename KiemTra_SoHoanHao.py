n = int(input())
tong_uoc = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        tong_uoc += i
if tong_uoc == n:
    print("YES")
else:
    print("NO")