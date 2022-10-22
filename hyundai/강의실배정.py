import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    s_i, f_i = map(int, input().split())
    heapq.heappush(heap, (f_i, s_i))

answer = 1
prev_end_time, _ = heapq.heappop(heap)

for _ in range(N-1):
    f_i, s_i = heapq.heappop(heap)
    if s_i >= prev_end_time:
        answer += 1
        prev_end_time = f_i
print(answer)