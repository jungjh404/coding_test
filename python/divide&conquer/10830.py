import sys

N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

## init값에도 % 연산 적용하기!
for i in range(N):
    for j in range(N):
        A[i][j] = A[i][j] % 1000
dp = []
bin_B = bin(B)[2:]
bin_B = bin_B[::-1]
len_dp = len(bin_B)

for i in range(len_dp):
    if i == 0:
        dp.append(A)
    
    else:
        tmp = [[0 for j in range(N)] for k in range(N)]
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    tmp[j][k] += dp[-1][j][l] * dp[-1][l][k]
                tmp[j][k] = tmp[j][k] % 1000
        dp.append(tmp)

res = None

for i in range(len_dp):
    if bin_B[i] == '1':
        if res is None:
            res = dp[i]

        else:
            tmp = [[0 for j in range(N)] for k in range(N)]
            for j in range(N):
                for k in range(N):
                    for l in range(N):
                        tmp[j][k] += (res[j][l] * dp[i][l][k])
                    tmp[j][k] = tmp[j][k] % 1000
            res = tmp

for i in range(N):
    for j in range(N):
        if j != N-1:
            print(res[i][j], end=" ")
        else:
            print(res[i][j])
        