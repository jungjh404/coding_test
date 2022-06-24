import sys

N = int(sys.stdin.readline())

map_lst = []
for _ in range(N):
    map_lst.append(list(map(int, sys.stdin.readline().split())))

cnt_1 = 0
cnt_0 = 0

divider = 1
while divider <= N:
    for i in range(N//divider):
        for j in range(N//divider):
            if map_lst[i][j] == 1:
                cnt_1 += 1
            if map_lst[i][j] == 0:
                cnt_0 += 1
    
    comb_map = [[-1 for _ in range(N//(divider*2))] for j in range(N//(divider*2))]

    for i in range(N//(divider*2)):
        for j in range(N//(divider*2)):
            if map_lst[2*i][2*j] == 1 and map_lst[2*i+1][2*j] == 1 and map_lst[2*i][2*j+1] == 1 and map_lst[2*i+1][2*j+1] == 1:
                comb_map[i][j] = 1
                cnt_1 -= 4
            
            elif map_lst[2*i][2*j] == 0 and map_lst[2*i+1][2*j] == 0 and map_lst[2*i][2*j+1] == 0 and map_lst[2*i+1][2*j+1] == 0:
                comb_map[i][j] = 0
                cnt_0 -= 4
    
    divider *= 2
    map_lst = comb_map[:]

print(cnt_0)
print(cnt_1)
