N = int(input())

answer = []
divisor = 2
for divisor in range(2, int(N**0.5)+1):
    while N % divisor ==0:
        answer.append(divisor)
        N //= divisor
if N != 1: answer.append(N)     

# 정답 출력
print(len(answer))
print(*answer)