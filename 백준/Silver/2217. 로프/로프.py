# 2217번
N = int(input())
list = [int(input()) for x in range(N)]
list.sort()

max = 0
for i in range(N): 
  temp = list[i]* (N-i)
  if temp > max:
    max = temp

print(max)