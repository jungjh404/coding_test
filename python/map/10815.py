import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

num_dict = [False for _ in range(20000001)]

for num in nums:
    num_dict[num + 10000000] = True

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    print(int(num_dict[target+10000000]), end=' ')