import sys
from collections import deque

input = sys.stdin.readline

case = int(input())


for _ in range(case):
    col_size, row_size, chu = map(int, input().split())
    board = [[0 for r in range(col_size)] for c in range(row_size)]

    for i in range(chu):
        y, x = map(int, input().split())
        board[x][y] = 1

    count = 0
    queue = deque([])
    for x in range(row_size):
        for y in range(col_size):
            if board[x][y] == -1 or board[x][y] == 0: continue
            queue.append([x, y])
            board[x][y] = -1 # visited 찍기
            while queue:
                cx, cy = queue.pop()
                board[cx][cy] = -1
                if cx+1 < row_size and board[cx+1][cy] == 1 :
                    queue.append([cx+1, cy])
                if cy+1 < col_size and board[cx][cy+1] == 1 :
                    queue.append([cx, cy+1])
                if 0 <= cx-1 and board[cx-1][cy] == 1 :
                    queue.append([cx-1, cy])
                if 0 <= cy-1 and board[cx][cy-1] == 1 :
                    queue.append([cx, cy-1])
            count+=1
    print(count)




