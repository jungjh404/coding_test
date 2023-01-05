'''
극이 다르면 반대방향 회전
같은 극이면 회전X
'''
import sys
from collections import deque

input = sys.stdin.readline
wheel_dict = {}

for i in range(1, 5):
    wheel_dict[i] = deque(list(input().rstrip()))

K = int(input())

for i in range(K):
    wheel_num, rot = map(int, input().split())

    rotate_dict = {wheel_num: rot}
    # 1 극 다른 거 확인

    # 오른쪽
    for j in range(wheel_num+1, 5):
        if wheel_dict[j-1][2] != wheel_dict[j][6]:
            rotate_dict[j] = -rotate_dict[j-1] 
        else:
            rotate_dict[j] = 0


    # 왼쪽
    for j in range(wheel_num-1, 0, -1):
        if wheel_dict[j][2] != wheel_dict[j+1][6]:
            rotate_dict[j] = -rotate_dict[j+1] 
        else:
            rotate_dict[j] = 0

    # 돌리기
    # print(rotate_dict)
    for key, value in rotate_dict.items():
        wheel_dict[key].rotate(value)
    # print(wheel_dict)



answer = 0

for i in range(1, 5):
    if wheel_dict[i][0] == '1':
        answer += 2 ** (i-1)

print(answer)