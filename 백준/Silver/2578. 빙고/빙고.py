def get_full_line_count():
    global board
    line = 0

    # 가로 열 full
    for row in board:
        if sum(row) == 0:
            line += 1

    # 세로 열 full
    for y in range(5):
        if sum(board[x][y] for x in range(5)) == 0:
            line += 1

    # 정대각선 full
    if sum([board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]]) == 0:
        line += 1

    # 반대각선 full
    if sum([board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]]) == 0:
        line += 1

    return line

# 2차원 배열인 board에서 특정 값의 2차원 인덱스 반환
def get_index_of(value):
    global board

    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == value:
                return x, y

board = [list(map(int, input().split())) for x in range(5)]
origin_list = [list(map(int, input().split())) for x in range(5)]

speak = [data for inner_list in origin_list for data in inner_list]
after = [[0 for _ in range(5)] for x in range(5)]


for idx, s in enumerate(speak):

    for x in range(5):
        for y in range(5):
            if board[x][y] == s:
                board[x][y] = 0

    if get_full_line_count() >= 3:
        print(idx+1)
        break


