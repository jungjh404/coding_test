import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

start = 1
end = max(trees)

res = 0

while start <= end:
    mid = (start + end) // 2
    tmp = 0

    for length in trees:
        if length > mid:
            tmp += length - mid
    
    if tmp >= M:
        start = mid + 1
        res = mid

    elif tmp < M:
        end = mid - 1

print(res)