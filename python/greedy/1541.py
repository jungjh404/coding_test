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

while '+' in lst:
    idx = lst.index('+')
    tmp = lst[idx-1] + lst[idx + 1]
    
    lst.insert(idx-1, tmp)
    
    lst.pop(idx+2)
    lst.pop(idx+1)
    lst.pop(idx)
    
while '-' in lst:
    idx = lst.index('-')
    tmp = lst[idx-1] - lst[idx + 1]
    lst.insert(idx-1, tmp)
    
    lst.pop(idx+2)
    lst.pop(idx+1)
    lst.pop(idx)

print(lst[0])