candy = int(input())
count = 0
for A in range(1, candy-1):
    for B in range(1, candy-1):
        for C in range(1, candy-1):
            if A+B+C == candy and C>=B+2 and A%2 == 0:
                count += 1
print(count)