from audioop import reverse
import sys
from collections import deque

input = sys.stdin.readline

N,M,R = map(int, input().split())
map_dict = {}
visited = {}
answer_dict = {}


for i in range(M):
    u, v = map(int, input().split())
    
    if u in map_dict:
        map_dict[u].append(v)
    
    else:
        map_dict[u] = [v]

    if v in map_dict:
        map_dict[v].append(u)
    
    else:
        map_dict[v] = [u]

for key in map_dict.keys():
    map_dict[key].sort(reverse=True)

queue = deque()
queue.append(R)
size = 1
cnt = 1

while size > 0:
    target = queue.popleft()
    size -= 1


    if target in visited:
        continue

    else:
        visited[target] = True
        answer_dict[target] = cnt
        cnt += 1

        if target in map_dict:
            for num in map_dict[target]:
                queue.append(num)
                size += 1


for i in range(1, N+1):
    if i in answer_dict:
        print(answer_dict[i])
    else:
        print(0)