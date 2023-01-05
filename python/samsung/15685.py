import sys

input = sys.stdin.readline

N = int(input())

curve_lst = [list(map(int, input().split())) for _ in range(N)]
# x y d g

curve_dict = {
    (0, 0): [(0,0), (0,1)],
    (0, 1): [(0,0), (-1,0)],
    (0, 2): [(0,0), (0,-1)],
    (0, 3): [(0,0), (1,0)]
}
# gen, dir

for gen in range(1, 11):
    for dir in range(4):
        prev_gen = (gen-1, dir)
        current_gen = []

        for point in curve_dict[prev_gen]:
            current_gen.append(point)
        # print(gen,dir)
        for i in range(len(curve_dict[prev_gen])-1, 0, -1):
            diff = (curve_dict[prev_gen][i-1][0] - curve_dict[prev_gen][i][0], curve_dict[prev_gen][i-1][1] - curve_dict[prev_gen][i][1])
            # print("diff",diff)
            if diff == (0, 1):
                current_gen.append((current_gen[-1][0]+1, current_gen[-1][1]))
            elif diff == (1, 0):
                current_gen.append((current_gen[-1][0], current_gen[-1][1]-1))
            elif diff == (0, -1):
                current_gen.append((current_gen[-1][0]-1, current_gen[-1][1]))
            elif diff == (-1, 0):
                current_gen.append((current_gen[-1][0], current_gen[-1][1]+1))
        
        curve_dict[(gen,dir)] = current_gen

# for i in range(0, 4):
#     for j in range(4):
#         print(f'{i},{j}: {curve_dict[(i,j)]}')
point_dict = {}

'''
k세대 커브는 K-1세대의 끝 점에 k-1세대를 90도 시계방향 시킴
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
     → x축
y축 ↓
'''

min_x = 100
min_y = 100
max_x = 0
max_y = 0

for curve in curve_lst:
    shape = curve_dict[(curve[3], curve[2])]
    # print(shape)
    for curve_point in shape:
        point = (curve[1] + curve_point[0], curve[0] + curve_point[1]) #y, x
        # print(point)
        if point not in point_dict:
            point_dict[point] = True
        
        min_y = min(min_y, point[0])
        max_y = max(max_y, point[0])

        min_x = min(min_x, point[1])
        max_x = max(max_x, point[1])

answer = 0

# print(point_dict)
# print(min_x, max_x)
# print(min_y, max_y)

for i in range(min_x, max_x):
    for j in range(min_y, max_y):
        square = [(j,i), (j,i+1), (j+1, i), (j+1, i+1)]
        cnt = 0
        for point in square:
            if point in point_dict:
                cnt += 1
        
        # print(square, cnt)
        if cnt == 4:
            answer += 1
            

print(answer)



