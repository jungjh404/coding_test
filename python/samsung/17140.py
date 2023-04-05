import sys
import heapq

input = sys.stdin.readline

r,c,k = map(int, input().split())

world = []
for _ in range(3):
    tmp = list(map(int, input().split()))
    world.append(tmp)

t = 0
res = -1

max_r = 3
max_c = 3

while t <= 100:
    # print(world, world[r-1][c-1], k, t)
    if r <= max_r and c <= max_c:
        if world[r-1][c-1] == k:
            res = t
            break
    
    if max_r >= max_c:
        # r 연산
        tmp_max_c = 0

        tmp_world = []

        for i in range(max_r):
            tmp_dict = {}
            for j in range(max_c):
                if world[i][j] == 0:
                    continue
                elif world[i][j] in tmp_dict:
                    tmp_dict[world[i][j]] += 1
                else:
                    tmp_dict[world[i][j]] = 1
            
            heap = []

            for key, value in tmp_dict.items():
                heap.append((value,key))

            heapq.heapify(heap)

            tmp_max_c = max(tmp_max_c, len(heap*2))
            
            tmp_row = []

            for _ in range(len(heap)):
                item = heapq.heappop(heap)
                tmp_row.append(item[1])
                tmp_row.append(item[0])
                
            tmp_world.append(tmp_row)
        
        max_c = min(tmp_max_c, 100)
        
        for i in range(max_r):
            while len(tmp_world[i]) < max_c:
                tmp_world[i].append(0)
            while len(tmp_world[i]) > 100:
                tmp_world[i].pop()
        
        world = tmp_world

    else:
        tmp_max_r = 0

        tmp_world = []

        for j in range(max_c):
            tmp_dict = {}
            for i in range(max_r):
                if world[i][j] == 0:
                    continue
                elif world[i][j] in tmp_dict:
                    tmp_dict[world[i][j]] += 1
                else:
                    tmp_dict[world[i][j]] = 1
            heap = []

            for key, value in tmp_dict.items():
                heap.append((value,key))

            heapq.heapify(heap)

            tmp_max_r = max(tmp_max_r, len(heap*2))
            
            tmp_row = []

            for _ in range(len(heap)):
                item = heapq.heappop(heap)
                tmp_row.append(item[1])
                tmp_row.append(item[0])
                
            tmp_world.append(tmp_row)
        
        max_r = min(tmp_max_r, 100)

        for i in range(max_c):
            while len(tmp_world[i]) < max_r:
                tmp_world[i].append(0)
            
            while len(tmp_world[i]) > 100:
                tmp_world[i].pop()
        
        world.clear()
        
        for i in range(max_r):
            tmp_row = []
            for j in range(max_c):
                tmp_row.append(tmp_world[j][i])
            
            world.append(tmp_row)

    t += 1

print(res)

