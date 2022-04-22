import sys

n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0,0,0] for _ in range(n)]

for i in range(n):
    for j in range(3):
        if (j == 0):
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + lst[i][j]

        elif (j == 1):
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + lst[i][j]

        elif (j == 2):
            dp[i][j] = min(dp[i-1][1], dp[i-1][0]) + lst[i][j]

print(min(dp[-1]))
