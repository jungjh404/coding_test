import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(N+1):
    for j in range(i+1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007

print(dp[N][K])