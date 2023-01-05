import sys
from collections import deque

def binary_search(lst, target, N):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return 1
        
        elif lst[mid] < target:
            start = mid + 1
        
        else:
            end = mid - 1
    return 0

N = int(sys.stdin.readline())
#파이썬은 tim sort가 좋아서 정렬은 그냥 쓰자!
A = sorted(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
B = deque(list(map(int, sys.stdin.readline().split())))



for i in range(M):
    target = B.popleft()
    print(binary_search(A, target, N))

