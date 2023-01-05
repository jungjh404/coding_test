import sys

N = int(sys.stdin.readline())

series = [int(sys.stdin.readline()) for _ in range(N)]
stack = []
cnt = 0
res = []
flag = True

idx = 1
while N > 0:

    if cnt == 0:
        stack.append(idx)
        res.append('+')
        cnt += 1
        idx += 1
        continue

    if stack[-1] == series[0]:
        series.pop(0)
        stack.pop()
        N -= 1
        cnt -= 1
        res.append('-')
    
    elif stack[-1] < series[0] and idx <= series[0]:
        stack.append(idx)
        cnt += 1
        idx += 1
        res.append('+')
    
    else:
        print("NO")
        flag = False
        break

if flag:
    for a in res:
        print(a)