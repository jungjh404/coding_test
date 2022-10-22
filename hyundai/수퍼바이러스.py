import sys
input = sys.stdin.readline

K,P,N = map(int, input().split())

steps = int(N / 0.1)
lst = [] 
lst.append(P)
lst.append(P**2)

binary_stps = list(reversed(bin(steps)[2:]))

for i in range(len(binary_stps)):
    lst.append((lst[-1]**2 % 1000000007))


answer = 1

for i in range(len(binary_stps)):
    if binary_stps[i] == '1':
        answer = (answer * lst[i]) % 1000000007

answer = (answer * K) % 1000000007
print(answer)