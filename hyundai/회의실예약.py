import sys

input = sys.stdin.readline

N,M = map(int, input().split())
room_dict = {}
room_lst = []

for _ in range(N):
    room = input().strip()
    room_dict[room] = [False] * 9
    room_lst.append(room)

room_lst.sort()

for _ in range(M):
    room, s, t = input().split()
    for i in range(int(s)-9, int(t)-9):
        room_dict[room][i] = True

for i in range(N):
    print(f'Room {room_lst[i]}:')

    empty_lst = []
    start = -1
    end = -1
    for j in range(9):
        if room_dict[room_lst[i]][j] == False and start == -1:
            start = j+9
        if room_dict[room_lst[i]][j] == True and start != -1:
            end = j+9
            empty_lst.append((start, end))
            start = -1
            end = -1
    if start != -1:
        end = 18
        empty_lst.append((start, end))
    
    size = len(empty_lst)
    if size == 0:
        print("Not available")
    
    else:
        print(f"{size} available:")
        for time in empty_lst:
            print(f'{time[0]:02d}-{time[1]}')

    if i < N-1:
        print("-----")
