import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N+1)]
for i in range(1,N+1):
    dp[i] = dp[i-1] + lst[i-1]

for i in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j]- dp[i-1])