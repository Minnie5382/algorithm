import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
min_value = board[0][0]
max_value = board[0][0]

for b in board:
    if min_value > min(b):
        min_value = min(b)
    if max_value < max(b):
        max_value = max(b)

safe_area_num_list = []

for level in range(min_value-1, max_value+1): # min~max
    # level 보다 낮은 지역을 잠기게 함
    for line in board:
        for i in range(len(line)):
            if line[i] <= level:
                line[i] = 0

    # 완성된 지도를 보며 안전한 영역 개수를 구하기
    count = 0
    queue = []
    visited = [[0 for a in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if board[x][y] != 0 and visited[x][y] == 0:
                queue.append([x, y])
                visited[x][y] = 1

                while queue:
                    cx, cy = queue.pop()
                    visited[cx][cy] = 1
                    if cx + 1 < N:
                        if board[cx+1][cy] != 0 and visited[cx+1][cy] == 0:
                            queue.append([cx+1, cy])
                            visited[cx+1][cy] = 1
                    if 0 <= cx - 1:
                        if board[cx-1][cy] != 0 and visited[cx-1][cy] == 0:
                            queue.append([cx-1, cy])
                            visited[cx-1][cy] = 1
                    if cy + 1 < N:
                        if board[cx][cy+1] != 0 and visited[cx][cy+1] == 0:
                            queue.append([cx, cy+1])
                            visited[cx][cy+1] = 1
                    if 0 <= cy - 1:
                        if board[cx][cy-1] != 0 and visited[cx][cy-1] == 0:
                            queue.append([cx, cy-1])
                            visited[cx][cy-1] = 1
                count += 1

    safe_area_num_list.append(count)

print(max(safe_area_num_list))
