def func3(a, b, m):
    if b==1: return a%m
    val = func3(a, int(b/2), m)
    val = val * val % m
    if b%2 == 0: return val
    return val * a % m


a, b, m = map(int, input().split())
print(func3(a, b, m))