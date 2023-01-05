import sys

input = sys.stdin.readline

gears = list(map(int, input().split()))

if gears[0] == 1 and gears[1] == 2 and gears[2] == 3 and gears[3] == 4 and gears[4] == 5 and gears[5] == 6 and gears[6] == 7 and gears[7] == 8:
    print("ascending")

elif gears[0] == 8 and gears[1] == 7 and gears[2] == 6 and gears[3] == 5 and gears[4] == 4 and gears[5] == 3 and gears[6] == 2 and gears[7] == 1:
    print("descending")

else:
    print("mixed")
