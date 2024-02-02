def solution(myString):
    answer = []
    for m in myString:
        if m < 'l':
            answer.append('l')
        else:
            answer.append(m)
    return "".join(answer)