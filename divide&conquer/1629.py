import sys

A, B, C = map(int, sys.stdin.readline().split())

dp = [0 for _ in range(32)]
dp[0] = A % C

for i in range(1, 32):
    dp[i] = dp[i-1]**2 % C

bin_num = bin(B)
res = 1
for i in range(len(bin_num)-2):
    if int(bin_num[len(bin_num)-1-i]) == 1:
        res *= dp[i]
print(res % C)