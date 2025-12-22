a, b, c = map(int, input().split())
chu_vi = a + b + c
dien_tich = (chu_vi*(chu_vi - a)*(chu_vi - b)*(chu_vi - c))**0,5
print(chu_vi, dien_tich)