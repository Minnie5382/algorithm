import sys
from collections import deque
input = sys.stdin.readline

X, Y = map(int, input().split())
board = [list(map(int, input().split())) for x in range(X)]

visited = [[False for x in range(Y)] for y in range(X)]
queue = deque([])
area = 0

add_x = [-1, 1, 0, 0]
add_y = [0, 0, -1, 1]

area_list = []
for x in range(X):
    for y in range(Y):
        if board[x][y] != 1 or visited[x][y]: continue
        area = 0
        queue.append([x, y])
        visited[x][y] = True

        while queue:
            q = queue.pop()
            area += 1
            qx, qy = q[0], q[1]

            if board[qx][qy] == 1:
                for i in (0,1,2,3):
                    nx = qx + add_x[i]
                    ny = qy + add_y[i]
                    if nx < 0 or ny<0 or nx>=X or ny>=Y: continue
                    if board[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append([nx, ny])
                        visited[nx][ny] = True
        area_list.append(area)

print(len(area_list))
print(max(area_list) if len(area_list) != 0 else 0)