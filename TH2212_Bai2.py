a, b, c = map(int, input().split())
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print(f"GTLN là {max_val}")
min_val = a
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
print(f"GTNN là {min_val}")
