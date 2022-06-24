import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([i for i in range(1, N+1)])
size = N

while size > 1:
    queue.popleft()
    size -= 1
    queue.append(queue.popleft())

print(queue[0])
