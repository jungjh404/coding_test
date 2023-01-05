import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice_num_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
dice_pos_dict = {'top': 1, 'bottom': 6, 'right': 3, 'left': 4, 'front': 5, 'back': 2}

'''
동:1
서:2
북:3
남:4

이동한 칸 == 0 => 주사위의 바닥 숫자 -> 칸 복사
이동한 칸 != 0 => 칸 숫자 -> 주사위 바닥 and 칸 숫자 = 0

출력: 주사위의 윗 면에 있는 수
========================================
구현할 함수
1. 넘어가는 지 판단
2. 주사위 회전 함수
3. 주사위와 판 적용
'''

def check_map_validity(x, y, command):
    global N, M
    command_map = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    new_x, new_y = (x + command_map[command-1][0], y + command_map[command-1][1])

    if new_x < 0 or new_x > N - 1 or new_y < 0 or new_y > M-1:
        return False
    
    else:
        return (new_x, new_y)
    

def rotate_dice(command):
    global dice_pos_dict
    if command == 3:
        # new_dice = (dice_pos_dict['back'], dice_pos_dict['top'], dice_pos_dict['front'], dice_pos_dict['bottom'])
        new_dice = (dice_pos_dict['top'], dice_pos_dict['front'], dice_pos_dict['bottom'], dice_pos_dict['back'])
        dice_pos_dict['back'] = new_dice[0]
        dice_pos_dict['top'] = new_dice[1]
        dice_pos_dict['front'] = new_dice[2]
        dice_pos_dict['bottom'] = new_dice[3]
    
    elif command == 4:
        new_dice = (dice_pos_dict['bottom'], dice_pos_dict['back'], dice_pos_dict['top'], dice_pos_dict['front'])
        dice_pos_dict['back'] = new_dice[0]
        dice_pos_dict['top'] = new_dice[1]
        dice_pos_dict['front'] = new_dice[2]
        dice_pos_dict['bottom'] = new_dice[3]

    elif command == 1:
        # new_dice = (dice_pos_dict['left'], dice_pos_dict['top'], dice_pos_dict['right'], dice_pos_dict['bottom'])
        new_dice = (dice_pos_dict['bottom'], dice_pos_dict['left'], dice_pos_dict['top'], dice_pos_dict['right'])
        dice_pos_dict['left'] = new_dice[0]
        dice_pos_dict['top'] = new_dice[1]
        dice_pos_dict['right'] = new_dice[2]
        dice_pos_dict['bottom'] = new_dice[3]
        pass

    elif command == 2:
        new_dice = (dice_pos_dict['top'], dice_pos_dict['right'], dice_pos_dict['bottom'], dice_pos_dict['left'])
        dice_pos_dict['left'] = new_dice[0]
        dice_pos_dict['top'] = new_dice[1]
        dice_pos_dict['right'] = new_dice[2]
        dice_pos_dict['bottom'] = new_dice[3]

def dice_and_world(x,y):
    global world, dice_pos_dict, dice_num_dict

    if world[x][y] == 0:
        world[x][y] = dice_num_dict[dice_pos_dict['bottom']]
    
    else:
        dice_num_dict[dice_pos_dict['bottom']] = world[x][y]
        world[x][y] = 0

for command in commands:
    next_step = check_map_validity(x,y,command)

    if not next_step:
        continue

    x, y = next_step

    rotate_dice(command)
    dice_and_world(x,y)
    print(dice_num_dict[dice_pos_dict['top']])