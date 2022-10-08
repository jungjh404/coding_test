import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

link_dict = {}

for i in range(1, N+1):
    link_dict[i] = [0, []]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    
    link_dict[u][1].append(v)
    link_dict[v][1].append(u)

for i in range(1, N+1):
    link_dict[i][1].sort()

visited = [0 for _ in range(N)]

cnt = 1

while 1:
    visited[R-1] = cnt

    try:
        next = link_dict[R][1][link_dict[R][0]]
        link_dict[R][0] += 1
    except:
        break

    if visited[next-1] != 0:
        continue

    else:
        R = next
        cnt += 1

for i in range(N):
    print(visited[i])

