N, M, K = map(int, input().split())

count = 0
for i in range(50):
    if N-2 >= 0 and M-1 >= 0:
        N -= 2
        M -= 1
        count += 1
    else:
        break

if (N+M) >= K:
    print(count)
else:
    count -= (K-(N+M)+2)//3
    print(count)