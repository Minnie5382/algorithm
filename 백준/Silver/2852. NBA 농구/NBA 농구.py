import sys
input = sys.stdin.readline

shoot_num = int(input())
score_1 = 0
score_2 = 0
team_1_win_time = 0
team_2_win_time = 0

second_list = []
win_team = []
for _ in range(shoot_num):
    team_num, time = input().split()

    # 분:초 -> 초로 변환
    mm, ss = map(int, time.split(":"))
    seconds = mm*60 + ss

    second_list.append(seconds)
    win_team.append(team_num)

second_list.append(60*48) # 경기 종료 시간을 추가

for i in range(shoot_num):
    interval = second_list[i+1] - second_list[i]

    if win_team[i] == '1':
        score_1 += 1
    elif win_team[i] == '2':
        score_2 += 1

    if score_1 > score_2:
        team_1_win_time += interval
    if score_1 < score_2:
        team_2_win_time += interval

print('%02d:%02d' % (team_1_win_time//60, team_1_win_time%60))
print('%02d:%02d' % (team_2_win_time//60, team_2_win_time%60))