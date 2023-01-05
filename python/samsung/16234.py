import sys
from collections import deque

input = sys.stdin.readline
N,L,R = map(int, input().split())

world_dict = {}
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        world_dict[(i,j)] = row[j]

day = 0

def bfs(key):
    global visited, exchange_dict, union_grpah
    queue = deque()
    queue.append(key)
    size = 1
    root_node = key

    while size > 0:
        target = queue.popleft()
        size -= 1

        if target not in visited:
            visited[target] = True

            if target != root_node:
                exchange_dict[root_node].append(target)


            for node in union_grpah[target]:
                if node not in visited:
                    queue.append(node)
                    size += 1

while 1:
    # print(day)
    union_grpah = {}

    for i in range(N):
        for j in range(N):
            current = (i,j)
            nears = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

            for near in nears:
                if near in world_dict:
                    diff = abs(world_dict[current] - world_dict[near])
                    if diff >= L and diff <= R:
                        if (i,j) in union_grpah:
                            union_grpah[current].add(near)
                            pass
                        else:
                            union_grpah[current] = set([near])
                        
                        if near in union_grpah:
                            union_grpah[near].add(current)
                            pass
                        
                        else:
                            union_grpah[near] = set([current])
    # print(union_grpah)

    if not union_grpah:
        break
        
    visited = {}
    exchange_dict = {}

    for key in union_grpah.keys():
        if key not in visited:
            exchange_dict[key] = [key]
            bfs(key)

    # print(visited)
    # print(exchange_dict)

    for group in exchange_dict.values():
        tmp = 0
        num = 0
        for nation in group:
            tmp += world_dict[nation]
            num += 1
        
        divided = tmp // num
        for nation in group:
            world_dict[nation] = divided
        
    day += 1
    # print(world_dict)
    
print(day)