import sys
input = sys.stdin.readline
N, M = map(int, input().split())
list = list(map(int, input().split()))

for i in range(M):
  list.sort()
  temp = list[0]+list[1]
  list[0] = temp
  list[1] = temp
print(sum(list))