n = int(input())
if n >= 2:
    kiem_tra = True
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            kiem_tra = False
            break
    print("YES" if kiem_tra else "NO")
else:
    print("NO")