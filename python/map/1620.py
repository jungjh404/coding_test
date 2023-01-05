import sys

N, M = map(int, sys.stdin.readline().split())

num_name = {}
name_num = {}
for i in range(1, N+1):
    name = input()
    num_name[i] = name
    name_num[name] = i

for _ in range(M):
    q = input()
    try:
        q = int(q)
        print(num_name[q])
    except ValueError:
        print(name_num[q])