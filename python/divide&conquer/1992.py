import sys

N = int(sys.stdin.readline())

map_lst = []
for _ in range(N):
    map_lst.append(list(map(int, list(sys.stdin.readline().rstrip()))))

divider = 1
comb_map = []
while divider < N:
    # print(map_lst)
    end_cnt = 0
    comb_map = [[-1 for _ in range(N//(divider*2))] for j in range(N//(divider*2))]
    
    for i in range(N//(divider*2)):
        for j in range(N//(divider*2)):
            if type(map_lst[2*i][2*j]) == int and type(map_lst[2*i+1][2*j]) == int and type(map_lst[2*i][2*j+1]) == int and type(map_lst[2*i+1][2*j+1]) == int:
                if map_lst[2*i][2*j] == 1 and map_lst[2*i+1][2*j] == 1 and map_lst[2*i][2*j+1] == 1 and map_lst[2*i+1][2*j+1] == 1:
                    comb_map[i][j] = 1
                
                elif map_lst[2*i][2*j] == 0 and map_lst[2*i+1][2*j] == 0 and map_lst[2*i][2*j+1] == 0 and map_lst[2*i+1][2*j+1] == 0:
                    comb_map[i][j] = 0
                
                else:
                    comb_map[i][j] = [[map_lst[2*i][2*j], map_lst[2*i][2*j+1]], [map_lst[2*i+1][2*j], map_lst[2*i+1][2*j+1]]]
                    end_cnt += 1
            
            else:
                comb_map[i][j] = [[map_lst[2*i][2*j], map_lst[2*i][2*j+1]], [map_lst[2*i+1][2*j], map_lst[2*i+1][2*j+1]]]
                end_cnt += 1
    
    divider *= 2
    map_lst = comb_map[:]


def print_arrary(arr):
    if type(arr) == int:
        print(arr, end="")
    
    elif len(arr) == 1:
        print_arrary(arr[0])
    
    else:
        print('(', end="")
        print_arrary(arr[0][0])
        print_arrary(arr[0][1])
        print_arrary(arr[1][0])
        print_arrary(arr[1][1])
        print(')', end="")

print_arrary(map_lst)