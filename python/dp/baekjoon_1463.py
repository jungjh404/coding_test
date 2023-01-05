import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    if (i == 2):
        dp[2] = 1

    elif (i == 3):
        dp[3] = 1

    else:
        a = None
        b = None
        c = None
        if (i % 3 == 0):
            a = dp[int(i/3)] + 1
        
        if (i % 2 == 0):
            b = dp[int(i/2)] + 1
        
        c = dp[i-1] + 1

        if a is None and b is None:
            dp[i] = c
        
        elif a is None:
            dp[i] = min(b,c)

        elif b is None:
            dp[i] = min(a,c)
        
        else:
            dp[i] = min(a,b,c)

print(dp[n])
