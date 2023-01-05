import sys
from collections import deque

def combinations(acc_tuple, start, pos):
    global empty_cnt, comb_set

    for i in range(start, empty_cnt+1):
        if pos >= 3:
            comb_set.add(acc_tuple)
        
        else:
            tmp = acc_tuple + (i,)
            combinations(tmp, i+1, pos+1)

def virus_dfs(virus_lst, wall_set, virus_cnt):
    global world, empty_lst
    cnt = 0
    visited = set()

    for new_wall in wall_set:
        visited.add(empty_lst[new_wall])
    
    queue = deque(virus_lst)
    size = virus_cnt
    
    nears = [[-1,0], [1,0], [0, -1], [0, 1]]
    
    while size > 0:
        target = queue.popleft()
        size -= 1

        if target not in visited:
            visited.add(target)
            cnt += 1

        
        for near in nears:
            next_target = (target[0] + near[0], target[1] + near[1])
            
            if next_target[0] >= 0 and next_target[0] < N and next_target[1] >= 0 and next_target[1] < M:
                if world[next_target[0]][next_target[1]] == 0 and next_target not in visited:
                    queue.append(next_target)
                    size += 1
    
    return cnt


input = sys.stdin.readline
N, M = map(int, input().split())

'''
1. 나올 수 있는 벽 조합 수 = 64 * 64 * 64 => 64C3 차이가 꽤남. 얘는 1번만 구하면 됨!
2. bfs: 4 * 64
3. 넓이 구하기 64
'''

total_size = N * M

empty_lst = []
empty_cnt = 0

wall_lst = []
wall_cnt = 0

virus_lst = []
virus_cnt = 0


comb_set = set()

world = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if world[i][j] == 0:
            empty_lst.append((i,j))
            empty_cnt += 1
        
        elif world[i][j] == 1:
            wall_cnt += 1
        
        elif world[i][j] == 2:
            virus_lst.append((i,j))
            virus_cnt += 1

combinations(tuple(), 0, 0)


answer = total_size
for wall_set in comb_set:
    answer = min(answer, virus_dfs(virus_lst, wall_set, virus_cnt))


print(total_size - answer - wall_cnt - 3) 