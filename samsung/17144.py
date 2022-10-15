import sys
import time

input = sys.stdin.readline

R,C,T = map(int, input().split())

world = {}

for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        world[(i,j)] = row[j]

cleaners = []

for i in range(R):
    if world[(i,0)] == -1:
        cleaners.append((i,0))

cleaner_dict = {
    "before_up": [],
    "before_down": []
}

for i in range(2):
    if i == 0:
        start = cleaners[i]
        for j in range(1, C):
            cleaner_dict["before_up"].append((start[0], j))
        for _ in range(start[0]):
            prev = cleaner_dict["before_up"][-1]
            cleaner_dict["before_up"].append((prev[0]-1,prev[1]))
        for _ in range(C-1):
            prev = cleaner_dict["before_up"][-1]
            cleaner_dict["before_up"].append((prev[0],prev[1]-1))
        for _ in range(start[0]-1):
            prev = cleaner_dict["before_up"][-1]
            cleaner_dict["before_up"].append((prev[0]+1,prev[1]))
        
    elif i == 1:
        start = cleaners[i]
        for j in range(1, C):
            cleaner_dict["before_down"].append((start[0], j))
        for _ in range(R-start[0]-1):
            prev = cleaner_dict["before_down"][-1]
            cleaner_dict["before_down"].append((prev[0]+1,prev[1]))
        for _ in range(C-1):
            prev = cleaner_dict["before_down"][-1]
            cleaner_dict["before_down"].append((prev[0],prev[1]-1))
        for _ in range(R-start[0]-2):
            prev = cleaner_dict["before_down"][-1]
            cleaner_dict["before_down"].append((prev[0]-1,prev[1]))

'''
1. 기존 값은 유지된 상태에서 분산될 값을 계산해야 하므로, 
기존 값을 유지하고 흩어질 양을 찾아야하고
나중에 한번에 world에서 찾아줘아함.

2. 공기청정기로 보내줘야하므로, 
list 두개로 이전값을 이후 값에 붙여 넣으면 좋을듯
'''

def distribution():
    global world, cleaner
    dis_dict = {}
    for i in range(R):
        for j in range(C):
            if world[(i,j)] == -1 or world[(i,j)] == 0:
                continue

            pos = (i,j)
            nears = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
            cnt = 0
            amount = world[pos] // 5
            for near in nears:
                if near in world and world[near] != -1:
                    cnt += 1

                    if near in dis_dict:
                        dis_dict[near] += amount
                        
                    else:
                        dis_dict[near] = amount
            
            if pos in dis_dict:
                dis_dict[pos] -= amount * cnt
            else:
                dis_dict[pos] = -amount * cnt

    for key, value in dis_dict.items():
        world[key] += value


def circulation():
    global world, cleaner_dict
    for values in cleaner_dict.values():
        dust = [world[pos] for pos in values]
        for i in range(len(dust)-1):
            world[values[i+1]] = dust[i]
        world[values[0]] = 0   

for _ in range(T):
    distribution()
    circulation()

answer = 0

for i in range(R):
    for j in range(C):
        if world[(i,j)] != -1:
            answer += world[(i,j)]
    
print(answer)
