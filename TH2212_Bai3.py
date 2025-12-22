def so_ln(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val
def so_nn(a, b, c):
    min_val = a
    if b < min_val:
        min_val = b
    if c < min_val:
        min_val = c
    return min_val
x, y, z = map(int, input().split())
max_value = so_ln(x, y, z)
min_value = so_nn(y, x, z)
print(f"GTLN: {max_value}, GTNN: {min_value}")