import sys

S = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

s_len = len(S)
dp = [[0]*(s_len + 1) for _ in range(26)]

for i in range(26):
    for j in range(1, s_len+1):
        dp[i][j] = dp[i][j - 1] + (S[j - 1] == chr(97+i))

for i in  range(q):
    tmp = sys.stdin.readline().split()
    print(dp[ord(tmp[0]) -97][int(tmp[2]) + 1] - dp[ord(tmp[0]) - 97][int(tmp[1])])