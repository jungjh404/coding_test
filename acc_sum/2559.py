import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = dp[i-1] + lst[i-1]

max_val = None
for i in range(N-K+1):
    tmp = dp[i+K] - dp[i]

    if max_val is None:
        max_val = tmp
    else:
        max_val = max(max_val, tmp)

print(max_val)


