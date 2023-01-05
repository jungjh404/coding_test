import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

if N == 0:
    print(lst[0]*lst[0])

else:
    lst.sort()
    print(lst[0]*lst[-1])