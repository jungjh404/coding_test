import sys

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
reserve = []
cnt = 0

lst.sort()

while N > 0:
    if cnt == 0:
        reserve.append(lst[0])
        cnt += 1
    
    else:
        if reserve[-1][1] <= lst[0][0]:
            reserve.append(lst[0])
            cnt += 1
        elif lst[0][1] < reserve[-1][1]:
            reserve[-1] = lst[0]
        
    lst.remove(lst[0])
    N -= 1
    
print(cnt)