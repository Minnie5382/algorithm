# 1931번
import sys
input = sys.stdin.readline
N = int(input())
list = [list(map(int, input().split())) for x in range(N)]

list.sort(key=lambda x: (x[1], x[0]))

t = 0 # 현재 시점
count = 0

for i in range(N):
  if list[i][0] >= t:
    t = list[i][1]
    count += 1

print(count)