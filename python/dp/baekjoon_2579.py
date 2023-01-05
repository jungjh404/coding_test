import sys

n = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(n)]
# stair.reverse()

dp = [0 for _ in range(n)]

for i in range(n):
    if (i == 0):
        dp[i] = stair[i]
    
    elif (i == 1):
        dp[i] = dp[i-1] + stair[i]

    elif (i == 2):
        dp[i] = max(dp[i-2] + stair[i], stair[i-1] + stair[i])

    else:
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[-1])