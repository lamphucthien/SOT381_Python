import math
a, b, c = map(float, input().split())
chu_vi = a + b + c
dien_tich = math.sqrt(chu_vi*(chu_vi - a)*(chu_vi - b)*(chu_vi - c))
print(f"Chu vi tam giác là {chu_vi}")
print(f"Diện tích tam giác là {dien_tich}")
