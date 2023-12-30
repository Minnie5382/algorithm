import sys
input = sys.stdin.readline

N, K = map(int, input().split()) 

list = [int(input()) for i in range(N)]
list.sort(reverse=True)

count = 0
for l in list:
    if K//l > 0:
      count += K//l
      K = K%l
print(count)