import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

queue = []

x, y = 0, 0
queue.append((x, y))
visited[x][y] = 1

while queue:
    x, y = queue.pop(0)

    # 4방향
    for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and visited[nx][ny] == 0:
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    # # 구구절절 코드
    # if board[x][y] == 1 and visited[x][y] == 0:
    #     if 0 <= x-1:
    #         queue.append((x-1, y))
    #         visited[x-1][y] = visited[x][y] + 1
    #     if x+1 < N:
    #         queue.append((x+1, y))
    #         visited[x+1][y] = visited[x][y] + 1
    #     if 0 <= y-1:
    #         queue.append((x, y-1))
    #         visited[x][y-1] = visited[x][y] + 1
    #     if y+1 < M:
    #         queue.append((x, y+1))
    #         visited[x][y+1] = visited[x][y] + 1
print(visited[N-1][M-1])
