import sys
import heapq

N = int(sys.stdin.readline())
heap = []
size = 0

for i in range(N):
    command = int(sys.stdin.readline())
    
    if command == 0:
        if size == 0:
            print(0)

        else:
            print(heapq.heappop(heap)[1])
            size -= 1
    else:
        heapq.heappush(heap, (-command, command))
        size += 1
    