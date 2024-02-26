import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    num = ""
    for c in input().rstrip():
        if c.isalpha():
            num += " "
        else:
            num += c
    num = num.split()
    for n in num:
        nums.append(int(n))
for num in sorted(nums):
    print(num)