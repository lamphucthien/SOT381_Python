s = input()
so_mu = len(s)
tong = 0

for x in s:
    tong += int(x) ** so_mu

if tong == int(s):
    print("YES")
else:
    print("NO")