a, b, c, d, e, f = list(map(int, input().split()))
flag = False
for x in range(-999,1000):
    for y in range(-999,1000):
        if x*a + y*b == c and x*d + y*e == f:
            print(x, y)
            flag = True
            break
    if flag:
        break