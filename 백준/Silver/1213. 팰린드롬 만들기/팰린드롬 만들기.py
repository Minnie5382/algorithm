from collections import Counter

name = input()
sorted_name = ''.join(sorted(list(name)))
counter = Counter(sorted_name)


answer = ""
center_char = ""

odd_count = 0
for char in counter.keys():
    if counter.get(char)%2 == 0:
        answer += char*(counter.get(char)//2)
    else :
        odd_count += 1
        if odd_count >= 2:
            print("I'm Sorry Hansoo")
            break
        answer += char*((counter.get(char)-1)//2)
        center_char = char # 홀수일 경우 그 홀수가 중앙값이 돼야함 -> center에 넣어줌
else: # break로 빠져나온 경우가 아니라면, for 문을 다 돌고 실행됨
    answer += center_char
    if odd_count >0: # 홀수가 있다면
        for i in range(len(answer)-2, -1, -1) :
            answer += list(answer)[i]
    else: # 전부 짝수라면
        for i in range(len(answer)-1, -1, -1) :
            answer += list(answer)[i]
    print(answer)