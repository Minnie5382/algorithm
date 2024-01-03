import sys
input = sys.stdin.readline

N = int(input())
list = [int(input()) for x in range(N)]

count = 0
for i in range(len(list)-1, 0, -1):
  if list[i-1] >= list[i]:
    count += list[i-1] - list[i] + 1
    list[i-1] = list[i] - 1

print(count)
  