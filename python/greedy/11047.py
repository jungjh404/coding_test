import sys

N, K = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(N)]

coins.reverse()

cnt = 0
while K != 0:
    if coins[0] <= K:
        cnt += K // coins[0]
        K = K % coins[0]

    coins.remove(coins[0])

print(cnt)