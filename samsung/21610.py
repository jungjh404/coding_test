from re import S
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
map_dict = {}
command = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        map_dict[(i+1, j+1)] = line[j]


'''
전체 탐색 경우의 수: 2500 * 100 * 4 = 백만
        j→
i↓   맵
'''
def calc_pos(i, j, d_i, s_i):
    global N
    new_i = None
    new_j = None
    if d_i == 1:
        new_i = i
        new_j = (j - 1 * s_i) % N
    
    elif d_i == 2:
        new_i = (i - 1 * s_i) % N
        new_j = (j - 1 * s_i) % N
    
    elif d_i == 3:
        new_i = (i - 1 * s_i) % N
        new_j = j
    
    elif d_i == 4:
        new_i = (i - 1 * s_i) % N
        new_j = (j + 1 * s_i) % N
    
    elif d_i == 5:
        new_i = i
        new_j = (j + 1 * s_i) % N
    
    elif d_i == 6:
        new_i = (i + 1 * s_i) % N
        new_j = (j + 1 * s_i) % N

    elif d_i == 7:
        new_i = (i + 1 * s_i) % N
        new_j = j

    elif d_i == 8:
        new_i = (i + 1 * s_i) % N
        new_j = (j - 1 * s_i) % N

    if new_i == 0:
        new_i = N
    
    if new_j == 0:
        new_j = N
    
    # print((i, j), "->", (new_i, new_j))
    return (new_i, new_j)


def calc_diagonal(i,j):
    return [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]


def move_cloud(cloud_set: set, d_i, s_i):
    new_cloud_set = set()

    for cloud in cloud_set:
        i,j = cloud
        new_i, new_j = calc_pos(i, j, d_i, s_i)
        new_cloud_set.add((new_i, new_j))

    return new_cloud_set

def rain(map_dict, next_poses):
    for pose in next_poses:
        map_dict[pose] += 1

def copy_water(map_dict, next_poses):
    for pose in next_poses:
        diagonals = calc_diagonal(pose[0], pose[1])

        cnt = 0
        for diagonal in diagonals:
            if diagonal in map_dict:
                if map_dict[diagonal] > 0:
                    cnt += 1
        
        map_dict[pose] += cnt


def reamke_rain(map_dict, prev_cloud, i):
    global N

    if i == 0:
        return set([(N, 1), (N, 2), (N-1, 1), (N-1, 2)])
    
    else:
        cloud_set = set()
        for i in range(N):
            for j in range(N):
                if map_dict[(i+1, j+1)] >= 2:
                    # print(i+1, j+1, ':', map_dict[(i+1, j+1)])
                    cloud_set.add((i+1, j+1))

        target_cloud = cloud_set - prev_cloud
        for cloud in target_cloud:
            map_dict[cloud] -= 2
        return target_cloud

def print_map(map_dict):
    global N 

    for i in range(1, N+1):
        for j in range(1, N+1):
            print(map_dict[i,j], end=" ")
        print()

prev_cloud = set()
# i = 0
for i in range(M):
    d_i, s_i = map(int, input().split())
    cloud_set = reamke_rain(map_dict, prev_cloud, i)
    # print(prev_cloud)
    # print_map(map_dict)
    # print(cloud_set)
    next_cloud_pos = move_cloud(cloud_set, d_i, s_i)
    rain(map_dict, next_cloud_pos)
    copy_water(map_dict, next_cloud_pos)

    # print("step", i)
    # print("cloud_set", cloud_set)
    # print("next_cloud", next_cloud_pos)
    # print_map(map_dict)
    # print("===========================")
    
    prev_cloud = next_cloud_pos

reamke_rain(map_dict, prev_cloud, M)
answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        answer += map_dict[(i,j)]
    
print(answer)


'''
1,5 -> 2,5
2,1 -> 
2,2
2,3
3,1
3,2
3,3
3,4
5,1
5,2
'''