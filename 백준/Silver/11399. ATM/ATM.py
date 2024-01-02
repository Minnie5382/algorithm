N = int(input())
waits = list(map(int, input().split()))
waits.sort()

answer = 0
tmp_sum = 0
for p in waits:
  tmp_sum += p
  answer += tmp_sum

print(answer)