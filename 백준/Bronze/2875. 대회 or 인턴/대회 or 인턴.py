N, M, K = map(int, input().split())
for i in range(K):
    if N < 2*M:
        M -= 1
    else:
        N -= 1
print(min(N//2, M))
