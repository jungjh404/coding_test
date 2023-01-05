import sys

N, K = map(int, sys.stdin.readline().split())

res = 1

for i in range(N, N-K, -1):
    res *= i
for i in range(K, 0, -1):
    res /= i
print(int(res))