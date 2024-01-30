def solution(N, stages):
    answer = []
    not_clear = [0 for _ in range(N+1)]
    reach = [0 for _ in range(N+1)]
    for stage in stages:
        not_clear[stage-1] += 1 # 현 스테이지 아직 못깸
        for j in range(stage): # 지금까지의 스테이지는 모두 도달함
            reach[j] += 1

    fail_rate = [not_clear[i] / reach[i] if reach[i] != 0 else 0 for i in range(N)]
    # 인덱스 정렬
    index = [i+1 for i in range(N)]
    sorted_index = sorted(index, key = lambda k: fail_rate[k-1], reverse = True)
            
    return sorted_index

