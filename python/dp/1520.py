import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
map_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dp = [[0]*N for _ in range(M)]

que = deque([])
que.append([0, 0])
size = 1

near_ponint_lst = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while size > 0:
    cur_x, cur_y = que.pop()
    dp[cur_y][cur_x] += 1
    size -= 1

    for near_point in near_ponint_lst:
        new_x = cur_x + near_point[0]
        new_y = cur_y + near_point[1]

        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
            continue
            
        if map_lst[new_y][new_x] >= map_lst[cur_y][cur_x]:
            continue

        que.append([new_x, new_y])
        
        size += 1

print(dp[M-1][N-1])