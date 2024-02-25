import sys
input = sys.stdin.readline
vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    flag = True
    pw = input().rstrip()
    if pw == 'end': break

    # 1. 모음 하나를 포함하지 않으면 not
    for p in pw:
        if p in vowels: # 모음이 있으면
            break
    else: # break로 나오지 않았다는건 모음이 하나도 없다는 것 -> not
        flag = False

    # 2. 같은 글자가 연속 두번 오면 not (ee, oo만 허용)
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1] and pw[i] != 'e' and pw[i] != 'o': # 연속 두번 왔는데 ee, oo가 아니면
            flag = False
            break

    # 3. 모음 3개, 자음 3개가 연속으로 오면 not
    for i in range(len(pw) - 2):
        if (pw[i] in vowels) and (pw[i+1] in vowels) and (pw[i+2] in vowels): # 모음 3개 연속이면
            flag = False
            break
        elif (pw[i] not in vowels) and (pw[i+1] not in vowels) and (pw[i+2] not in vowels): # 자음 3개 연속이면
            flag = False
            break

    # 출력
    if flag:
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')

