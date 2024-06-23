def gcd(a, b):
    while a%b != 0:
        tmp = a%b
        a = b
        b = tmp
    return b

def lcm(a, b):
    return a*b//gcd(a, b)


N = input()
seq = list(map(int, input().split()))
seq.sort()
answer = 0
for i in range(len(seq)-1):
    if gcd(seq[i], seq[i+1]) != 1:
        for j in range(seq[i]+1, seq[i+1]):
            if gcd(seq[i], j) == 1 and gcd(j, seq[i+1]) == 1:
                answer += 1
                break
        else:
            answer += 2
print(answer)