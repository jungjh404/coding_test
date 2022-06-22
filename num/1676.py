import sys

N = int(sys.stdin.readline())

cnt = 0

for i in range(1, N+1):
    tmp = i
    while tmp % 5 == 0:
        cnt += 1
        tmp = tmp // 5

print(cnt)
