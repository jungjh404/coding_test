import sys

input = sys.stdin.readline

N, M = map(int, input().split())
comb_lst = []

def distnace(home, chicken):
    return abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])

def combination(t, now, pos):
    global chick_num, M, comb_lst
    # print(t, now, pos)
    for i in range(now, chick_num+1):
        if pos == M:
            comb_lst.append(t)
            return        
        else:
            tmp = t + (i,)
            combination(tmp, i+1, pos+1)



home_lst = []
chicken_lst = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            home_lst.append((i+1, j+1))
        
        elif row[j] == 2:
            chicken_lst.append((i+1, j+1))

chick_num = len(chicken_lst)
home_num = len(home_lst)

answer = None

combination(tuple(), 0, 0)
print(comb_lst)
# print(comb_lst)
for comb in comb_lst:
    tmp = 0

    for home in home_lst:
        cur_min = None
        # print(home)
        for chick in comb:
            dist = distnace(home, chicken_lst[chick])
            # print(dist)
            if cur_min is None:
                cur_min = dist
            
            else:
                cur_min = min(cur_min, dist)
        
        tmp += cur_min
    # print(tmp)
    if answer is None:
        answer = tmp
    
    else:
        answer = min(answer, tmp)

print(answer)

