import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temps = list(map(int, input().split()))

max = sum(temps[:K])
total = sum(temps[:K])
for i in range(K, N):
    total -= temps[i-K]
    total += temps[i]
    if total > max:
        max = total
print(max)