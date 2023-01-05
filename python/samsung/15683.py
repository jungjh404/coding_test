import sys
from pprint import pprint

input = sys.stdin.readline

N,M = map(int, input().split())
world = {}
wall_cnt = 0
wall_set = set()
cctv_dict = {
                1: [],
                2: [],
                3: [],
                4: [],
                5: []
}

for i in range(N):
    row = list(map(int, input().split()))
    
    for j in range(M):
        world[(i,j)] = row[j]

        if row[j] >= 1 and row[j] <= 5:
            cctv_dict[row[j]].append((i,j))
        
        elif row[j] == 6:
            wall_cnt += 1
            wall_set.add((i,j,))
# print('wall', wall_set)

def check_coverage(type, pos):
    global world
    
    tmp = []
    
    
    nears = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    for near in nears:
        tmp_pos = [pos[0], pos[1]]
        tmp_set = set()
        tmp_set.add(tuple([pos[0], pos[1]]))
        # print(pos, tmp_set)
        while 1:
            tmp_pos[0] += near[0]
            tmp_pos[1] += near[1]

            tmp_pos_tuple = tuple(tmp_pos)

            if tmp_pos_tuple not in world or world[tmp_pos_tuple] == 6:
                break

            tmp_set.add(tuple(tmp_pos))
        
        tmp.append(tmp_set)

    return tmp


cctv_cov_dict = {}
for type, cctv_lst in cctv_dict.items():
    # print(type, cctv_lst)
    for cctv in cctv_lst:
        cctv_cov_dict[cctv] = check_coverage(type, cctv)
num_cctv = len(cctv_cov_dict)

cctv_lst = list(cctv_cov_dict)
# pprint(cctv_cov_dict)
'''
진행상황: 각 방향 일직선에 대한 값만 추출
permutation으로 set extend하기
'''

comb_dict = {
    1: [[0],[1],[2],[3]],
    2: [[0,2],[1,3]],
    3: [[0,1], [1,2], [2,3], [3,0]],
    4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5: [[0,1,2,3]]
}

comb_lst = []

def get_comb(comb, cctv_idx):
    global comb_lst, num_cctv, cctv_lst
    
    if cctv_idx == num_cctv:
        comb_lst.append(comb)

    else:
        for dir in comb_dict[world[cctv_lst[cctv_idx]]]:
            if comb is None:
                tmp = tuple(dir)
            else:
                tmp = comb + tuple(dir)
            get_comb(tmp, cctv_idx+1)
            
get_comb(None, 0)
# pprint(comb_lst)

blocked_num = 0

for combs in comb_lst:
    idx = 0
    current_set = set()
    for cctv in cctv_lst:
        dirs = None

        if world[cctv] == 1:
            dirs = combs[idx:idx+1]
            idx += 1
        elif world[cctv] == 4:
            dirs = combs[idx:idx+3]
            idx += 3
        elif world[cctv] == 5:
            dirs = combs[idx:idx+4]
            idx += 4
        else:
            dirs = combs[idx:idx+2]
            idx += 2

        for dir in dirs:
            current_set = current_set | cctv_cov_dict[cctv][dir]
    
    current_set = current_set | wall_set
    blocked_num = max(blocked_num, len(current_set))

print(N*M - blocked_num)
