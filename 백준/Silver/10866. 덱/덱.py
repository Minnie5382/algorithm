from collections import deque
import sys
queue = deque()
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    statement = input()
    if "push_front" in statement:
        s, n = statement.split()
        n = int(n)
        queue.appendleft(n)
    elif "push_back" in statement:
        s, n = statement.split()
        n = int(n)
        queue.append(n)
    elif "pop_front" in statement:
        print(queue.popleft() if queue else -1)
    elif "pop_back" in statement:
        print(queue.pop() if queue else -1)
    elif "size" in statement:
        print(len(queue))
    elif "empty" in statement:
        print(0 if queue else 1)
    elif "front" in statement:
        print(queue[0] if queue else -1)
    elif "back" in statement:
        print(queue[-1] if queue else -1)