import sys

n, m = list(map(int, sys.stdin.readline().split(" ")))

ball_map = []

red_idx = None
blue_idx = None
goal_idx = None

for y in range(m):
    row = list(sys.stdin.readline().strip())

    if ('0' in row):
        goal_idx = [row.index('0'), y]

    if ('R' in row):
        red_idx = [row.index('0'), y]

    if ('B' in row):
        blue_idx = [row.index('0'), y]

cnt = 0




