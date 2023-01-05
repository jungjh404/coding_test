import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])
size = 0

for _ in range(N):
    com = sys.stdin.readline().split()

    if com[0] == "push":
        queue.append(int(com[1]))
        size += 1
    
    elif com[0] == "pop":
        if size == 0:
            print(-1)

        else:
            print(queue.popleft())
            size -= 1

    elif com[0] == "front":
        if size == 0:
            print(-1)
        
        else:
            print(queue[0])
    
    elif com[0] == "back":
        if size == 0:
            print(-1)
        
        else:
            print(queue[size-1])
    
    elif com[0] == "empty":
        if size == 0:
            print(1)

        else:
            print(0)
    
    elif com[0] == "size":
        print(size)
