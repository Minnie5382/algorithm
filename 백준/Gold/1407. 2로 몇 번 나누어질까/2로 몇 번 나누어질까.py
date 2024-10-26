def func(a, N):
    i = 0
    answer = N
    while N > 0:
        N //= a
        answer += N * a**i
        i += 1
    return answer
num1, num2 = map(int, input().split())
print(func(2, num2)-func(2, num1-1))