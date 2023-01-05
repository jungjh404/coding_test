# 나중에 다시 풀기
import sys

N, C = map(int, sys.stdin.readline().split())
ap = sorted([int(sys.stdin.readline()) for _ in range(N)])

for i in range(N-1):
