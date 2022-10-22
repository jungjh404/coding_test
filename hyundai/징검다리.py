import sys
input = sys.stdin.readline

N, K = map(int, input().split())
score = list(map(int, input().split()))
dp_score = [0]
for i in range(N):
    dp_score.append(dp_score[-1] + score[i])

for _ in range(K):
    a_i, b_i = map(int, input().split())
    num_people = b_i - a_i + 1
    answer = (dp_score[b_i] - dp_score[a_i-1]) / num_people
    print("{:.2f}".format(answer))