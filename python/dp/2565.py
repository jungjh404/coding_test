import sys

N = int(sys.stdin.readline())
A = []

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    A.append(line)
A.sort()

dp1 = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i][1] > A[j][1]:
            dp1[i] = max(dp1[i], dp1[j] + 1)


print(N - max(dp1))