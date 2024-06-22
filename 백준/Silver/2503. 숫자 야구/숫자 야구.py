TC = int(input())

hints = [list(input().split()) for _ in range(TC)]

answer = []
count = 0
flag = False
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a==b or b==c or c==a: continue

            hit = True
            for tried, strike, ball in hints:
                strike = int(strike)
                ball = int(ball)
                tried_a = int(tried[0])
                tried_b = int(tried[1])
                tried_c = int(tried[2])

                if a == tried_a: strike -= 1
                if b == tried_b: strike -= 1
                if c == tried_c: strike -= 1

                if a in (tried_b, tried_c): ball -= 1
                if b in (tried_c, tried_a): ball -= 1
                if c in (tried_a, tried_b): ball -= 1

                if strike != 0 or ball != 0:
                    hit = False
            if hit:
                answer.append(100*a+10*b+c)

print(len(answer))

