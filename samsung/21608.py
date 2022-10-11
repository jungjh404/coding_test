import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def satisfy(love_dict, position_dict, i, j):
    cnt = 0

    nears = [(i-1, j), (i+1, j), (i,j-1), (i, j+1)]
    for near in nears:
        if near in position_dict:
            if position_dict[near] in love_dict[position_dict[(i,j)]]:
                cnt += 1
    
    if cnt == 0:
        return 0
    else:
        return 10 ** (cnt - 1)

def position(love_dict, pos_dict, num, N):
    heap = []
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if pos_dict[(i,j)] is not None:
                heappush(heap, (1, 1) + (i, j))
                continue
            
            
            empty_val = 0
            max_val = 0
            nears = [(i-1, j), (i+1, j), (i,j-1), (i, j+1)]

            for near in nears:
                if near not in pos_dict:
                    continue
                
                if pos_dict[near] is None:
                    empty_val += 1
                
                elif pos_dict[near] in love_dict[num]:
                    max_val += 1
            heappush(heap, (-max_val, -empty_val) + (i, j))
    
    # print(heap)
    a = heappop(heap)[2:]
    pos_dict[a] = num
    # print(num, a)


answer = 0

N = int(input())

love_dict = {}
order = []
for _ in range(N**2):
    a, b1, b2, b3, b4 = map(int, input().split())
    love_dict[a] = [b1,b2,b3,b4]
    order.append(a)

position_dict = {}


for i in range(1, N+1):
    for j in range(1, N+1):
        position_dict[(i,j)] = None
        
        
for num in order:
    position(love_dict, position_dict, num, N)
    # print(position_dict)

for i in range(1, N+1):
    for j in range(1, N+1):
        answer += satisfy(love_dict, position_dict, i, j)
        # print(i, j, answer)

print(answer)