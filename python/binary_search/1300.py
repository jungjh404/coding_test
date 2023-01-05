#https://st-lab.tistory.com/281
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

start = 1
end = N**2
res = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 0

    for i in range(1, N+1):
        if mid // i == 0:
            break
        
        cnt += min(mid // i, N)

    if cnt >= K:
        end = mid - 1
        
    elif cnt < K:
        start = mid + 1

    
print(start)
