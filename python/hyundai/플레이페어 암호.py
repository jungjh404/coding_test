from collections import deque

alphabets = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")

message = deque(list(input()))
size = len(message)

keys = list(input())


table = {} #alphabet: (i,j)
reverse = {} #(i,j): alphabet

i = 0
for key in keys:
    if key in table:
        continue

    table[key] = (i//5, i%5)
    reverse[(i//5, i%5)] = key
    i+=1

for alphabet in alphabets:
    if alphabet in table:
        continue

    table[alphabet] = (i//5, i%5)
    reverse[(i//5, i%5)] = alphabet
    i+=1

two_lst = []

while size > 0:
    if size == 1:
        a = message.popleft()
        two_lst.append(a+"X")
        size -= 1

    else:
        a = message.popleft()
        b = message.popleft()
        size -= 2

        if a != b:
            two_lst.append(a+b)
        
        else:
            message.appendleft(b)
            size += 1

            if a != "X":
                two_lst.append(a+"X")
            else:
                two_lst.append(a+"Q")

answer = []

for pair in two_lst:
    a_x, a_y = table[pair[0]]
    b_x, b_y = table[pair[1]]

    if a_x == b_x:
        next_a = reverse[(a_x, (a_y+1)%5)]
        next_b = reverse[(b_x, (b_y+1)%5)]
    
    elif a_y == b_y:
        next_a = reverse[((a_x+1)%5, a_y)]
        next_b = reverse[((b_x+1)%5, b_y)]

    else:
        next_a = reverse[(a_x, b_y)]
        next_b = reverse[(b_x, a_y)]
    
    answer.append(next_a+next_b)

print(''.join(answer))