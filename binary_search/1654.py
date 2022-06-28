import sys


N, K = map(int, sys.stdin.readline().split())
line = []
for _ in range(N):
    line.append(int(sys.stdin.readline()))
line.sort()

start = 1
end = line[-1]

res = 0
while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for length in line:
        tmp += length // mid
    print(start, mid, end, "개수", tmp)
    if tmp == K:
        res = mid
        start += 1

    elif tmp < K:
        end = mid - 1
    
    elif tmp > K:
        start = mid + 1
print(res)
