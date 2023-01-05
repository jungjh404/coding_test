import sys

def get_near(r,c,d):
    #Front Right Back Left
    if d == 0:
        return (r-1, c), (r, c+1), (r+1, c), (r, c-1)
    elif d == 1:
        return (r, c+1), (r+1, c), (r, c-1), (r-1, c)
    elif d == 2:
        return (r+1, c), (r, c-1), (r-1, c), (r, c+1)
    elif d == 3:
        return (r, c-1), (r-1, c), (r, c+1), (r+1, c)

def print_map(map_dict, n, m):
    for i in range(n):
        for j in range(m):
            print(map_dict[(i,j)], end=' ')
        print()

input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
# 북:0, 동:1, 남:2, 서: 3

global_dict = {}

for i in range(N):
    row = list(map(int, input().split()))
    
    for j in range(M):
        global_dict[(i,j)] = row[j]

answer = 0


# 닦으면2, 벽은 1, 빈공간 0
while 1:
    if global_dict[(r,c)] == 0:
        global_dict[(r,c)] = 2
        answer += 1
    
    # print(r,c,d)
    # print_map(global_dict, N, M)
    # input()

    front, right, back, left = get_near(r, c, d)
    
    if global_dict[left] == 0:
        d = (d - 1) % 4
        r, c = left
    
    elif global_dict[left] != 0 and global_dict[front] != 0 and global_dict[right] != 0 and global_dict[back] == 1:
        break

    elif global_dict[left] != 0 and global_dict[front] != 0 and global_dict[right] != 0 and global_dict[back] != 0:
        r,c = back
    
    else:
        d = (d - 1) % 4


print(answer)