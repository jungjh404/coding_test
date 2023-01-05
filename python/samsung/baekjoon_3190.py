import sys

n = int(sys.stdin.readline())
leng = 1
body = [[1, 1]]


k = int(sys.stdin.readline())
apple_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

l = int(sys.stdin.readline())
move = [sys.stdin.readline().split() for _ in range(l)]

# map_lst = [[0 for _ in range(n+2)] for _ in range(n+2)]

# for i in range(n+2):
#     map_lst[0][i] = 'x'
#     map_lst[-1][i] = 'x'
#     map_lst[i][0] = 'x'
#     map_lst[i][-1] = 'x'

# for apple in apple_lst:
#     map_lst[apple[0]][apple[1]] = 1

# map_lst[1][1] = -1
# print(map_lst)

cnt = 0
direction = [4,8,6,2]
direction_idx = 2

next_move = move.pop(0)

while 1:
    if next_move is not None:
        if int(next_move[0]) == cnt:
            if next_move[1] == 'L':
                direction_idx = (direction_idx - 1) % 4
            else:
                direction_idx = (direction_idx + 1) % 4

            # change to l
            if len(move) != 0:
                next_move = move.pop(0)
            else:
                next_move = None
    

    next_head = body[0][:]
    if direction[direction_idx] == 8:
        next_head[0] -= 1
    
    elif direction[direction_idx] == 4:
        next_head[1] -= 1
    
    elif direction[direction_idx] == 2:
        next_head[0] += 1

    elif direction[direction_idx] == 6:
        next_head[1] += 1
    
    cnt += 1
    
    if 0 in next_head or n+1 in next_head or next_head in body:
        break

    if not next_head in apple_lst:
        body.pop()
    else:
        apple_lst.remove(next_head)

    
    
    body.insert(0, next_head) 
    print(cnt, direction[direction_idx], body)


print(cnt)
