from collections import deque
test = int(input())

for _ in range(test):
    count = 0
    popped = []
    popped_index = []
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    # print()
    index = [i for i in range(N)]
    queue = deque(priority)
    index_queue = deque(index)
    while queue:
        if queue[0] == max(queue):
            popped.append(queue.popleft())
            popped_index.append(index_queue.popleft())
            count += 1
        else:
            queue.rotate(-1)
            index_queue.rotate(-1)

    print(popped_index.index(M)+1)
