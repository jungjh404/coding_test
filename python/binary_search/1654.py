import sys


K, N = map(int, sys.stdin.readline().split())
line = []
for _ in range(K):
    line.append(int(sys.stdin.readline()))
line.sort()

start = 1
end = line[-1]

res = 0

while start <= end:
    mid = (start + end) // 2
    tmp = 0

    for length in line:
        tmp += length // mid
    
    if tmp >= N:
        res = mid
        start = mid + 1

    elif tmp < N:
        end = mid - 1

print(res)
'''
https://claude-u.tistory.com/443 
res는 안되고 end는 되는 이유가 뭘까?

파악하지 못한 문제 조건
편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 
기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 
그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. 
N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.

'''

# print(end)