import sys
from collections import deque

input = sys.stdin.readline

N,K = map(int, input().split())
components = list(input().strip())

queue = deque([])
size = 0
answer = 0

for i in range(N):
    # print(queue, size)
    if size == 0:
        queue.append((components[i], i))
        size += 1
        continue
    
    idx = size
    for j in range(size-1, -1, -1):
        # 뒤 쪽만 보게 수정
        if i - queue[j][1] > K:
            break
        if queue[j][0] != components[i] and i - queue[j][1] <= K:
            idx = min(idx, j)
    
    if idx != size:
        del queue[idx]
        size -= 1
        answer += 1

    else:
        queue.append((components[i], i))
        size += 1

print(answer)