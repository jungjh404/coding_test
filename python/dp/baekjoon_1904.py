import sys

n = int(input())

lst = [0]*1000000
lst[0] = 1
lst[1] = 2

for i in range(2, n):
    lst[i] = (lst[i-1] + lst[i-2]) % 15746

print(lst[n-1])

