import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

res = 0

for i in range(N):
    if dp1[i] + dp2[i] > res:
        res = dp1[i] + dp2[i]

print(res-1)