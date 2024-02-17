N = int(input())
M = int(input())
mats = list(map(int, input().split()))
mats.sort()

left = 0
right = N - 1
count = 0
while left < right:
    sum = mats[left] + mats[right]
    if sum < M:
        left += 1
    elif sum > M:
        right -= 1
    elif sum == M:
        count += 1
        left += 1
        right -= 1

print(count)