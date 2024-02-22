import sys
input = sys.stdin.readline
while True:
    try:
        N = int(input())
        dividend = "1"
        while True:
            if int(dividend)%N == 0:
                print(len(dividend))
                break
            dividend += "1"
    except:
        break