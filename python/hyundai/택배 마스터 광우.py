import sys
from itertools import permutations
input = sys.stdin.readline

N,M,K = map(int, input().split())
lane_lst = list(map(int, input().split()))

lane_combs = list(permutations(lane_lst, N))

answer = None
for lanes in lane_combs:
    tmp = 0
    idx = 0
    for _ in range(K):
        cart = 0
        while cart + lanes[idx] <= M:
            cart += lanes[idx]
            idx = (idx + 1) % N
            
        tmp += cart
        
    if answer is None:
        answer = tmp
    else:
        answer = min(answer, tmp)

print(answer)