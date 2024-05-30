height, width = map(int, input().split())
board = [list(map(int, input().split(" "))) for i in range(height)]

def bfs():
    queue = [[0, 0]]
    melt = []

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        [x, y] = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 0: # 공기면
                    queue.append((nx, ny)) # 계속 탐색을 위해 큐에 넣기
                elif board[nx][ny] == 1: # 치즈면
                    melt.append((nx, ny))
    for x, y in melt:
        board[x][y] = 0

    return len(melt)

# 전체 치즈 갯수 구하기
cheese_count = 0
for b in board:
    cheese_count += sum(b)

time = 1
while True:
    visited = [[0] * width for _ in range(height)]
    melted_count = bfs()
    cheese_count -= melted_count
    if cheese_count == 0:  # 치즈를 다 녹였으면
        print(time, melted_count, sep='\n')  # 시간과 직전에 녹인 치즈 갯수를 출력
        break
    time += 1