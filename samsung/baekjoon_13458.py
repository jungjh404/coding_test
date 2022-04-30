import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = list(map(int, sys.stdin.readline().split()))

res = 0

for ai in a:
    rest = ai - b
    res += 1
    
    if rest <= 0:
        continue

    else:
        if (rest % c == 0):
            res = res + int(rest / c)
        else:
            res = res + int(rest / c) + 1


print(res)
