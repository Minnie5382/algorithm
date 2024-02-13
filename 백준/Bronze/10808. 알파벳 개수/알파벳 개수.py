S = input()
answer = [0 for c in range(ord('a'), ord('z')+1)]

for s in S:
    answer[ord(s) - 97] += 1
for a in answer:
    print(a, end=" ")