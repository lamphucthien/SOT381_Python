a, b, c = map(int, input().split())
chu_vi = a + b + c
dien_tich = (chu_vi*(chu_vi - a)*(chu_vi - b)*(chu_vi - c))**0,5
print(f"Chu vi tam giác là {chu_vi},Diện tích tam giác là {dien_tich}")
