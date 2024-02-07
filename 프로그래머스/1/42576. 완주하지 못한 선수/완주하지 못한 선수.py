from collections import Counter 

def solution(participant, completion):
    # 첫번째 풀이 -> 시간 초과
    # for c in completion:
    #     if c in participant:
    #         del participant[participant.index(c)]
    # return ''.join(participant)
    
    # 두번째 풀이
    part = Counter(participant)
    comp = Counter(completion)
    part.subtract(comp)

    return ''.join(list(part.elements())) 
    
