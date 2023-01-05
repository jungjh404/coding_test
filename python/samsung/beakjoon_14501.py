import sys

n = int(sys.stdin.readline())
schedule_lst = []
dp = [0] * (n + 1)

for _ in range(n):
    schedule_lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(n+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[j])

        if schedule_lst[j][0] + j <= i:
            dp[i] = max(dp[i], dp[j]+schedule_lst[j][1])

            
print(dp[-1])
