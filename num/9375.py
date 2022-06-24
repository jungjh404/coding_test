import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    clo_dict = {}
    for _ in range(N):
        cloth, kind = sys.stdin.readline().split()
        if kind in clo_dict:
            clo_dict[kind].append(cloth)
        
        else:
            clo_dict[kind] = [cloth]
    
    res = 1
    for items in list(clo_dict.values()):
        # print(items)
        res *= len(items) + 1
    
    print(res - 1)

