from glob import glob
import heapq
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
tmp = list(map(int, input().split()))
belt = deque([[tmp[i], False, i]for i in range(2*N)])
broken = {}

answer = 1
cnt = 0

def check_broken(i):
    global broken, cnt

    if i not in broken:
        cnt += 1
        broken[i] = True

while 1:
    

    # 1
    belt.rotate(1)
    if belt[N-1][1]:
        belt[N-1][1] = False
    
    # 2
    for i in range(N-2, -1, -1):
        if belt[i][1] and not belt[i+1][1] and belt[i+1][0] > 0:
            belt[i+1][0] -= 1
            belt[i+1][1] = True
            belt[i][1] = False

            if belt[i+1][0] == 0:
                check_broken(belt[i+1][2])

            if i+1 == N-1 and belt[i+1][1]:
                belt[i+1][1] = False

    # 3
    if belt[0][0] > 0:
        belt[0][1] = True
        belt[0][0] -= 1

        if belt[0][0] == 0:
                check_broken(belt[0][2])

    # print(answer, cnt)
    # print(belt)
    # print('=====================')

    # 4
    if cnt >= K:
        break

    answer += 1

print(answer)

