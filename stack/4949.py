import sys

braket = ['[', ']', '(', ')']
stack = []
top = 0
flag = False

while not flag:
    string = sys.stdin.readline()
    if string[0] == '.':
        flag = True
        break

    idx = 0 
    while string[idx-1] != '.':
        idx += 1
        if string[idx-1] in braket:
            stack.append(string[idx-1])
            top += 1
            
            
            if top < 2:
                continue
            if ((stack[-1] ==  ')' and stack[-2] == '(') or (stack[-1] ==  ']' and stack[-2] == '[')):
                top -= 2
                stack.pop()
                stack.pop()
        
    
    if top == 0:
        print('yes')
    else:
        print('no')
    
    stack.clear()
    top = 0