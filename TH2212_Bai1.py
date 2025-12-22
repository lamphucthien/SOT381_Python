w, h = map(int, input("Nhập độ dài 2 cạnh (w > 0, h <= 100: ").split())
chu_vi = (w + h)*2
dien_tich = w * h
if w < 0 and h > 100:
    print("Hãy nhập 2 độ dài hợp lệ: ")
else:
    print(f"Chu vi là {chu_vi}, Diện tích là {dien_tich}")