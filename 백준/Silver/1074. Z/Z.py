def func(N, r, c):
    half = 2**(N-1)
    if N == 0:
        return 0
    if r < half and c < half: # 왼쪽 상단
        return func(N-1, r, c)
    if r < half and c >= half: # 오른쪽 상단
        return half*half + func(N-1, r, c-half)
    if r >= half and c < half: # 왼쪽 하단
        return 2*half*half + func(N-1, r-half, c)
    if r >= half and c >= half: # 오른쪽 하단
        return 3*half*half + func(N-1, r-half, c-half)


n, r, c = map(int, input().split())
print(func(n, r, c))