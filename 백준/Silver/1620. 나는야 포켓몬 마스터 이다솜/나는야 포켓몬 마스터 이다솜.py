import sys
input = sys.stdin.readline
N, M = map(int, input().split())

mons = [input().replace("\n", "") for _ in range(N)]
quizzes = [input().replace("\n", "") for _ in range(M)]
index_name = dict(zip(range(1, len(mons)+1), mons))
name_index = dict(zip(mons, range(1, len(mons)+1)))

for quiz in quizzes:
    if quiz.isalpha(): # 이름이면
        print(name_index[quiz])
    else: # 번호면
        print(index_name[int(quiz)])