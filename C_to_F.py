def c_to_f(c):
    return c * 9/5 + 32
def c_to_k(c):
    return c + 273.15
while True:
 inf = input("Hãy nhập độ C, hoặc ấn f để dừng: ")
 if inf.lower() == 'f':
     print("Kết thúc")
     break
 try:
    C = float(inf)
    print("F= ", c_to_f(C))
    K = float(inf)
    print("K= ", c_to_k(K))
 except ValueError:
     print("Vui lòng nhập số hợp lệ: ")
