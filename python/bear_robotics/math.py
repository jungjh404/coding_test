def MathChallenge(strParam):
  lst = strParam.split()
  stack = []
  ops = ['+', '-', '*', '/']

  for token in lst:
    if token in ops:
        b = stack.pop()
        a = stack.pop()

        if token == ops[0]:
            stack.append(a+b)
        
        elif token == ops[1]:
            stack.append(a-b)

        elif token == ops[2]:
            stack.append(a*b)

        elif token == ops[3]:
            stack.append(a/b)

    else:
        stack.append(int(token))
      
  # code goes here
  return stack[0]

# keep this function call here 
print(MathChallenge(input()))