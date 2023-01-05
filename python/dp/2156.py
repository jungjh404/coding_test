import sys

N = int(sys.stdin.readline())
wine = [0]
for _ in range(N):
    wine.append(int(sys.stdin.readline()))

dp = [[0, 0] for _ in range(N+1)]

dp[1] = [wine[1], 1]

if N >= 2:
    dp[2] = [dp[1][0] + wine[2], 2]

for i in range(3, N+1):
    if dp[i-1][1] == 2:
        a = dp[i-3][0] + wine[i] + wine[i-1]
        b = dp[i-2][0] + wine[i]
        c = dp[i-1][0]

        if a >= b and a >= c:
            dp[i] = [a, 2]
        
        elif b > a and b > c:
            dp[i] = [b, 1]

        else:
            dp[i] = [c, 0]  

    else:
        dp[i] = [dp[i-1][0] + wine[i], dp[i-1][1]+1]

print(dp[N][0])