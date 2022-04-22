import sys
n = int(sys.stdin.readline())
tri = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dp = [[0]* n for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if (j == 0):
            dp[i][j] = dp[i-1][j] + tri[i][j]
        
        elif (j == i):
            dp[i][j] = dp[i-1][j-1] + tri[i][j]

        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

# print(max(dp[n-1]))
print(dp)