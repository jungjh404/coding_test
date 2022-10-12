import sys

input = sys.stdin.readline

N,M = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]

shapes = [
    [(0,0), (0,1), (0,2), (0,3)], 
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (1,0), (1,1)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (1,0), (0,1), (0,2)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,1), (1,1), (2,1), (2,0)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (1,1), (0,1), (0,2)],
    [(0,1), (1,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(0,0), (1,0), (1,1), (2,0)],
    [(0,1), (1,1), (1,0), (1,2)],
    [(0,1), (1,1), (1,0), (2,1)]
]

def check_in_world(map_points):
    global N, M
    x_max = 0
    y_max = 0

    for point in map_points:
        x_max = max(x_max, point[0])
        y_max = max(y_max, point[1])
    
    if x_max >= N or y_max >= M:
        return False
    
    return True


answer = 0

for shape in shapes:
    for i in range(N):
        for j in range(M):
            map_points = [
                (shape[0][0]+i, shape[0][1]+j),
                (shape[1][0]+i, shape[1][1]+j),
                (shape[2][0]+i, shape[2][1]+j),
                (shape[3][0]+i, shape[3][1]+j)
            ]

            if check_in_world(map_points):
                tmp = 0
                for point in map_points:
                    tmp += world[point[0]][point[1]]
                
                answer = max(answer, tmp)

print(answer)
