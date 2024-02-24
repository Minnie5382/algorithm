import sys
input = sys.stdin.readline
testcase = int(input())

for _ in range(testcase):
    PS = input().rstrip()
    while True:
        PS = PS.replace("()", "")
        try:
            PS.index("()")
        except:
            break
    if len(PS) != 0:
        print("NO")
    else:
        print("YES")
