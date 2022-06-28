#fibonacci 행렬: https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95
import sys

N = int(sys.stdin.readline())

dp = []

bin_N = bin(N)[2:][::-1]
len_bin_N = len(bin_N)

for i in range(len_bin_N):
    if i == 0:
        dp.append([[1, 1], [1, 0]])

    else:
        tmp = [[0, 0], [0, 0]]
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    tmp[j][k] += dp[-1][j][l] * dp[-1][l][k]
                tmp[j][k] = tmp[j][k] % 1000000007
        dp.append(tmp)

res = [[1, 0], [0, 1]]
for i in range(len_bin_N):
    if bin_N[i] == '1':
        tmp = [[0, 0], [0, 0]]
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    tmp[j][k] += res[j][l] * dp[i][l][k]
                tmp[j][k] = tmp[j][k] % 1000000007
        res = tmp

print(res[0][1])