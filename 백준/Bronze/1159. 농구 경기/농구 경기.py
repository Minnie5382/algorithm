N = int(input())
names = [input() for _ in range(N)]
alphabet = [0 for _ in range(ord('a'), ord('z')+1 )]
for name in names:
    alphabet[ord(name[0])-ord('a')] += 1

flag = True
for idx, a in enumerate(alphabet):
    if a >= 5:
        flag = False
        print(chr(idx + ord('a')), end="")

if flag:
    print("PREDAJA")