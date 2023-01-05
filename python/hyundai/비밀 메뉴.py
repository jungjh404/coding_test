import sys

input = sys.stdin.readline

M,N,K =  map(int, input().split())
key = ''.join(list(input().split()))
numbers = ''.join(list(input().split()))

if key in numbers:
    print("secret")
else:
    print("normal")