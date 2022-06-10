import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    