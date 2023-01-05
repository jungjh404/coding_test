def StringChallenge(strParam):
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    ops_dict = {'plus': '+', 'minus': '-'}

    nums = list(num_dict.keys())
    ops = list(ops_dict.keys())

    for num in nums:
        strParam = strParam.replace(num, num_dict[num])
    
    for op in ops:
        strParam = strParam.replace(op, ops_dict[op])
    
    lst = []
    cnt = 0
    idx = 0
    for i in range(len(strParam)):
        if strParam[i] == '+' or strParam[i] == '-':
            lst.append(int(strParam[idx:i]))
            lst.append(strParam[i])
            idx = i + 1
            cnt += 2
    lst.append(int(strParam[idx:]))
    cnt += 1

    stack = []
    top = 0
    while cnt > 0:
        item = lst.pop(0)
        cnt -= 1

        if item == '+' or item == '-':
            stack.append(item)
            top += 1
        
        else:
            if top == 0:
                stack.append(item)
                top += 1
            
            else:
                op = stack.pop()
                a = stack.pop()
                
                if op == '+':
                    stack.append(a + item)
                elif op == '-':
                    stack.append(a - item)
                
                top -= 1
        
    res = ""
    print(stack)
    for char in str(stack[0]):
        if char == '-':
            res = res + "negative"
        else:
            res = res + nums[int(char)]

    return res

# keep this function call here 
print(StringChallenge(input()))