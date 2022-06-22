import sys

N = int(sys.stdin.readline())

for i in range(N):
    N, M = map(int, sys.stdin.readline().split())

    min_num = min(N,M)
    
    com_num = 1
    for i in range(2, min_num + 1):
        if N % i == 0 and M % i == 0:
            com_num = i
    
    print(int(N / com_num * M / com_num * com_num))