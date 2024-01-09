l = sorted(input(), reverse = True)
list_int = list(map(int, l))

if sum(list_int)%3 == 0 and list_int[-1] == 0:
    print("".join(l))
else:
    print(-1)