import sys
input = sys.stdin.readline
H,W = map(int, input().split())

map_dict = {}
for i in range(1,H+1):
    row = list(input().strip())
    for j in range(1, W+1):
        if row[j-1] == "#":
            map_dict[(i,j)] = True

start_lst = []
nears = [(-1,0), (0,1), (1,0), (0,-1)]

for key in map_dict.keys():
    cnt = 0
    for near in nears:
        if (key[0] + near[0], key[1] + near[1]) in map_dict:
            cnt += 1
    if cnt == 1:
        start_lst.append(key)

start_dir = None
if (start_lst[0][0] - 1, start_lst[0][1]) in map_dict:
    start_dir = 0
elif (start_lst[0][0] + 1, start_lst[0][1]) in map_dict:
    start_dir = 2
elif (start_lst[0][0], start_lst[0][1]+1) in map_dict:
    start_dir = 1
elif (start_lst[0][0], start_lst[0][1]-1) in map_dict:
    start_dir = 3

current_dir = start_dir
current_node = start_lst[0]

motion = []
while current_node != start_lst[1]:
    if (current_node[0] + nears[current_dir][0], current_node[1] + nears[current_dir][1]) in map_dict:
        motion.append('A')
        current_node = (current_node[0] + 2*nears[current_dir][0], current_node[1] + 2*nears[current_dir][1])
    elif (current_node[0] + nears[(current_dir-1)%4][0], current_node[1] + nears[(current_dir-1)%4][1]) in map_dict:
        motion.append('L')
        current_dir = (current_dir - 1)%4
    elif (current_node[0] + nears[(current_dir+1)%4][0], current_node[1] + nears[(current_dir+1)%4][1]) in map_dict:
        motion.append('R')
        current_dir = (current_dir + 1)%4
print(f'{start_lst[0][0]} {start_lst[0][1]}')
if start_dir==0:
    print('^')
if start_dir==2:
    print('v')
if start_dir==3:
    print('<')
if start_dir==1:
    print('>')
print(''.join(motion))
