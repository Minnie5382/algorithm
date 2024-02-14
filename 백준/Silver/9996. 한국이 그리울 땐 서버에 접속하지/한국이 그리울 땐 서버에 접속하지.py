N = int(input())
start, end = input().split('*')
names = [input() for _ in range(N)]

for name in names:
    flag = False
    if name.startswith(start):
        name = name[len(start):]
        if name.endswith(end):
            flag = True
    if flag:
        print("DA")
    else:
        print("NE")