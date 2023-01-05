import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    
    res = 1

    for i in range(M, M-N, -1):
        res *= i
    tmp = 1
    for i in range(N, 0, -1):
        tmp *= i
    print(res//tmp)
    # 그냥 쭉 나누면 안됨...