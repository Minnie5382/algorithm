height, width, figure_num = map(int, input().split())
board = [[1 for _ in range(width)] for a in range(height)]
visited = [[0 for _ in range(width)] for a in range(height)]

for _ in range(figure_num):
    start_x, start_y, end_x, end_y = map(int, input().split())
    for x in range(start_y, end_y):
        for y in range(start_x, end_x):
            board[x][y] = 0

queue = []
areas = []
for y in range(height):
    for x in range(width):
        if board[y][x] == 1 and visited[y][x] == 0:
            area = 0
            queue.append([y, x])
            visited[y][x] = 1

            while queue:
                cy, cx = queue.pop()
                visited[cy][cx] = 1
                area += 1
                if cx+1 < width:
                    if board[cy][cx+1] == 1 and visited[cy][cx+1] == 0:
                        queue.append([cy, cx+1])
                        visited[cy][cx+1] = 1
                if 0 <= cx-1:
                    if board[cy][cx-1] == 1 and visited[cy][cx-1] == 0:
                        queue.append([cy, cx-1])
                        visited[cy][cx-1] = 1
                if cy+1 < height:
                    if board[cy+1][cx] == 1 and visited[cy+1][cx] == 0:
                        queue.append([cy+1, cx])
                        visited[cy+1][cx] = 1
                if 0 <= cy-1:
                    if board[cy-1][cx] == 1 and visited[cy-1][cx] == 0:
                        queue.append([cy-1, cx])
                        visited[cy-1][cx] = 1
            areas.append(area)
print(len(areas))
for area in sorted(areas):
    print(area, end=" ")