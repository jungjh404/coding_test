import sys
from itertools import combinations
n = int(sys.stdin.readline())

lst = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

res = -1

possible_team = []

for team in list(combinations([i for i in range(n)],n//2)):
    possible_team.append(team)

for i in range(len(possible_team)//2):
    team_start = 0
    team_link = 0

    for x in possible_team[i]:
        for y in possible_team[i]:
            team_start += lst[x][y]

    for x in possible_team[len(possible_team) -1 -i]:
        for y in possible_team[len(possible_team) -1 -i]:
            team_link += lst[x][y]

    if res == -1:
        res = abs(team_link - team_start)

    else:
        res = min(res, abs(team_link - team_start))

print(res)