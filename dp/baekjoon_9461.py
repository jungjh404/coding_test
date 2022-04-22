import sys

n = int(sys.stdin.readline())
p = [int(sys.stdin.readline().strip()) for _ in range(n)]

lst = [0]*100
lst[0] = 1
lst[1] = 1
lst[2] = 1

for i in range(3, 100):
    lst[i] = (lst[i-2] + lst[i-3])

for i in range(n):
    print(lst[p[i]-1])

