a, b, c = map(int, input().split())
max_val = 0
if a > b and a > c:
    max_val = a
    print(f"Số lớn nhất là {max_val}")
if b > c and b > a:
    max_val = b
    print(f"Số lớn nhất là {max_val}")
if c > a and c > b:
    max_val = c
    print(f"Số lớn nhất là {max_val}")
