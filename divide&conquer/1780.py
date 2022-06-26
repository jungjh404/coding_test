import sys

N = int(sys.stdin.readline())

map_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

minus_1 = 0
zero = 0
plus_1 = 0

divider = 1
while divider <= N:
    # print(map_lst)
    for i in range(N//divider):
        for j in range(N//divider):
            if map_lst[i][j] == 0:
                zero += 1
            elif map_lst[i][j] == -1:
                minus_1 += 1
            
            elif map_lst[i][j] == 1:
                plus_1 += 1
    
    temp_map = [[2 for _ in range(N//(divider*3))] for k in range(N//(divider*3))]
    # print(temp_map)
    for i in range(N//(divider*3)):
        for j in range(N//(divider*3)):
            area = [map_lst[3*i][3*j], map_lst[3*i][3*j+1], map_lst[3*i][3*j+2], map_lst[3*i+1][3*j], map_lst[3*i+1][3*j+1], map_lst[3*i+1][3*j+2], map_lst[3*i+2][3*j], map_lst[3*i+2][3*j+1], map_lst[3*i+2][3*j+2]]
            # print(area)
            if area.count(-1) == 9:
                # print(i, j)
                temp_map[i][j] = -1
                minus_1 -= 9
            
            elif area.count(0) == 9:
                # print(i, j)
                temp_map[i][j] = 0
                zero -= 9
            
            elif area.count(1) == 9:
                # print(i, j)
                temp_map[i][j] = 1
                plus_1 -= 9
    divider *= 3
    map_lst = temp_map[:]

print(minus_1, zero, plus_1, sep="\n")