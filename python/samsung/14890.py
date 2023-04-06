import sys

input = sys.stdin.readline

N, L = map(int, input().split())

row_world = [list(map(int, input().split())) for _ in range(N)]
col_world = []

for i in range(N):
    col = []
    for j in range(N):
        col.append(row_world[j][i])
    col_world.append(col)

def check_slide(line: list, num: int, length: int):
    slide_state = [0 for _ in range(num)]
    prev_height = line[0]
    
    for i in range(num):
        if abs(prev_height - line[i]) > 1:
            return False
        
        elif prev_height > line[i]:
            for j in range(i,i+length):
                if j < 0 or j >= num:
                    return False
                slide_state[j] += 1
            

        elif prev_height < line[i]:
            for j in range(i-length,i):
                if j < 0 or j >= num:
                    return False
                slide_state[j] += 1

        # print(i, prev_height, slide_state)
        prev_height = line[i]
        
    
    for i in range(num):
        if slide_state[i] > 1:
            return False

    return True

res = 0

for i in range(N):
    # print(i, "ROW")
    if check_slide(row_world[i], N, L):
        res += 1
        # print("ROW", i)
    # print(i, "COL")
    if check_slide(col_world[i], N, L):
        res += 1
        # print("COL", i)
    

print(res)
