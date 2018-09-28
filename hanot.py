def hano(n,a,b,c):
    global i
    if n==1:
        i += 1
        print(i, ":", a, "-->", b)
        return None
    if n==2:
        i += 1
        print(i, ":", a, "-->", b)
        i += 1
        print(i, ":", a, "-->", c)
        i += 1
        print(i, ":", a, "-->", c)
        return None
    hano(n-1, a, c, b)
    i += 1
    print(i, ":", a, "-->", b)
    hano(n-1, b, a, c)


a = "A"
b = "B"
c = "C"
n = 1
while n >= 0:

    n = int(input("input:"))
    if n == 0:
        print("This Progrom End")
        break
    i = 0
    hano(n, a, b, c)