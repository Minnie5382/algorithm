from collections import deque

test = int(input())
for _ in range(test):
    popped_index = []
    N, M = map(int, input().split())

    priority = list(map(int, input().split()))
    priority_queue = deque(priority)

    index_queue = deque([i for i in range(N)])

    while priority_queue:
        if priority_queue[0] == max(priority_queue):
            priority_queue.popleft()
            popped_index.append(index_queue.popleft())
        else:
            priority_queue.rotate(-1)
            index_queue.rotate(-1)

    print(popped_index.index(M)+1)