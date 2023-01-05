import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    child = lst[0]
    parent = lst[i]

    min_num = min(child, parent)
    com_num = 1
    for num in range(2, min_num+1):
        if child % num == 0 and parent % num == 0:
            com_num = max(com_num, num)
    
    print(f'{child//com_num}/{parent//com_num}')