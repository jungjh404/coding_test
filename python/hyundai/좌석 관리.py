import sys

input = sys.stdin.readline

N,M,Q = map(int, input().split())

seat_dict = {}

for i in range(1, N+1):
    for j in range(1, M+1):
        seat_dict[(i, j)] = None

eat = set()

for _ in range(Q):
    state, id = input().split()
    id = int(id)

    if state == "In":
        pass

    else:
        pass

def safety():
    min_seat = (1,1)
    max_safety = (N**2 + M**2) ** 0.5

    for i in range(1, N+1):
        for j in range(1, M+1):
            pass
