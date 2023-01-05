import sys
input = sys.stdin.readline

N = int(input())
rocks = list(map(int, input().split()))
dp = [0]*N
dp[0] = 1

for i in range(1, N):
    max_rocks = 0
    for j in range(i):
        if rocks[i] > rocks[j]:
            max_rocks = max(max_rocks, dp[j])
    dp[i] = max_rocks + 1

print(max(dp))