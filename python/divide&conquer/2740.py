import sys

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

M, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

res = [[0 for i in range(K)] for j in range(N)]

for i in range(N):
    for j in range(K):
        for x in range(M):
            res[i][j] += A[i][x] * B[x][j]
        print(res[i][j], end=" ")
    print()


