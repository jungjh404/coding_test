import sys
input = sys.stdin.readline

light_dict = {
    " ": [0, 0, 0, 0, 0, 0, 0],
    "0": [1, 1, 1, 0, 1, 1, 1],
    "1": [0, 0, 1, 0, 0, 1, 0],
    "2": [1, 0, 1, 1, 1, 0, 1],
    "3": [1, 0, 1, 1, 0, 1, 1],
    "4": [0, 1, 1, 1, 0, 1, 0],
    "5": [1, 1, 0, 1, 0, 1, 1],
    "6": [1, 1, 0, 1, 1, 1, 1],
    "7": [1, 1, 1, 0, 0, 1, 0],
    "8": [1, 1, 1, 1, 1, 1, 1],
    "9": [1, 1, 1, 1, 0, 1, 1]
}

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    

    lst_a = list(f'{A:5d}')
    lst_b = list(f'{B:5d}')

    answer = 0
    for i in range(5):
        a_num = light_dict[lst_a[i]]
        b_num = light_dict[lst_b[i]]

        for j in range(7):
            if a_num[j] != b_num[j]:
                answer += 1

    print(answer)