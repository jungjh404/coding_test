import queue
import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())

queue = deque([i for i in range(1, N+1)])
size = N
idx = 0


print("<", end="")
while size > 0:
    for i in range(K):
        if i != K - 1:
            queue.append(queue.popleft())

        else:
            if size != 1:
                print(queue.popleft(), end=", ")
            else:
                print(queue.popleft(), end="")
            size -= 1
print(">", end="")