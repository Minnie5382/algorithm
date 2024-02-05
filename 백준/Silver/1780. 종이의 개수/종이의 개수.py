import sys
input = sys.stdin.readline

n = int(input())
mtx = [list(map(int, input().split())) for _ in range(n)]
m, z, o = 0, 0, 0

def check(x, y, length):
    global m, z, o
    for i in range(x, x + length): # 가로 시작점 ~ 종이 끝
        for j in range(y, y + length): # 세로 시작점 ~ 종이 끝
            if mtx[x][y] != mtx[i][j]: # 첫번째 칸 숫자와 나머지 칸 숫자들을 모두 비교 -> 같지 않다면 (한 장이 아니라면)
                for a in range(3):
                    for b in range(3): # 가로 3등분, 세로 3등분하여
                        check(x + length // 3 * a, y + length // 3 * b, length // 3) # 시작점을 각 등분의 첫번째 칸으로 지정, 한 변의 길이는 3으로 나눠서 지정
                return # 이거는 왜 있는걸까?

    # 한 장이라면 오는 곳
    if mtx[x][y] == -1: # -1이면
        m += 1 # -1에 개수 한 개 추가
    elif mtx[x][y] == 0:
        z += 1
    elif mtx[x][y] == 1:
        o += 1

check(0, 0, n) # 시작점과 종이 한 변의 길이
print(m)
print(z)
print(o)