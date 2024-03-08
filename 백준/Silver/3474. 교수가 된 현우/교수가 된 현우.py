import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    num = int(input())
    count = 0
    while num >= 5:
        num //= 5
        count += num
    print(count)