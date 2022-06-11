import sys

eq = sys.stdin.readline().strip()
lst = []

len_eq = len(eq)
prev_idx = 0
idx = 0
while idx < len_eq:
    if eq[idx] == '+' or eq[idx] == '-':
        lst.append(int(eq[prev_idx:idx]))
        lst.append(eq[idx])
        prev_idx = idx+1
    
    idx += 1
lst.append(int(eq[prev_idx:]))

res = None
minus_mode = False
mode = 0
tmp = 0
for i in range(len(lst)):
    if res is None:
        res = lst[i]
    
    elif lst[i] == '+':
        mode = 1
    
    elif lst[i] == '-':
        mode = -1
        minus_mode = True
    
    else:
        if mode == 0:
            tmp = lst[i]
        
        if mode == -1:
            tmp = tmp + mode*lst[i]
        