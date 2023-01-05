from audioop import reverse
import queue
import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    queue = deque(eval(sys.stdin.readline()))
    
    reverse_mode = False

    for fun in p:
        if fun == 'R':
            reverse_mode = not reverse_mode
        
        elif fun == 'D' and not reverse_mode:
            if n > 0:
                queue.popleft()
                n -= 1
            else:
                n -= 1
                break

        elif fun == 'D' and reverse_mode:
            if n > 0:
                queue.pop()
                n -= 1
            else:
                n -= 1
                break
    
    if n == -1:
        print("error")
    
    else:
        print("[", end="")
        while n > 0:
            if reverse_mode:
                if n == 1:
                    print(queue.pop(), end="")
                else:
                    print(queue.pop(), end=",")
            else:
                if n == 1:
                    print(queue.popleft(), end="")
                else:
                    print(queue.popleft(), end=",")
            n -= 1
        print("]")

