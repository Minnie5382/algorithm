N = int(input())
serial = list(map(int, input().split()))
result = [-1] * N
stack = [0] # 인덱스

for i in range(1, N):
    while stack and serial[stack[-1]] < serial[i]:
        result[stack.pop()] = serial[i]
    stack.append(i)
print(*result)