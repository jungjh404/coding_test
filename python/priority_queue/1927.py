import sys
import heapq

N = int(sys.stdin.readline())
heap = []
size = 0

for _ in range(N):
    com = int(sys.stdin.readline())

    if com == 0 and size == 0:
        print(0)
    
    elif com == 0 and size != 0:
        print(heapq.heappop(heap))
        size -= 1
    
    else:
        heapq.heappush(heap, com)
        size += 1