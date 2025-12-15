m = 3
n = 0
while n < m:
    r = m - n
    inf = input(f"Hãy nhập Y hoặc y, bạn còn {r} lần nhập: ")
    if inf.lower() == 'y':
        print("Login success!")
        break
    else:
        n += 1
        if n < m:
            print(f"Vui lòng nhập lại")
        else:
            print("Đăng nhập thất bại. Bạn đã hết số lần nhập.")
            break