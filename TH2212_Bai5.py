def main():
    n = int(input())
    if n < 2 :
        print("Hãy nhập n >= 2")
        return
    t = 0
    m = 0
    for i in range(1 , n + 1):
        t += i
        if i % 2 == 0:
            m += i
    s = t/m
    print(s)
main()
