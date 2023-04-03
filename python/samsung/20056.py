import sys
from collections import deque

input = sys.stdin.readline

class Ball:
    def __init__(self, r_i, c_i, m_i, s_i, d_i):
        self.r = r_i
        self.c = c_i
        self.m = m_i
        self.s = s_i
        self.d = d_i
    
    def move(self, N):
        if self.d == 0:
            self.r -= self.s
        
        if self.d == 1:
            self.r -= self.s
            self.c += self.s

        if self.d == 2:
            self.c += self.s
        
        if self.d == 3:
            self.r += self.s
            self.c += self.s
        
        if self.d == 4:
            self.r += self.s
        
        if self.d == 5:
            self.r += self.s
            self.c -= self.s
        
        if self.d == 6:
            self.c -= self.s
        
        if self.d == 7:
            self.r -= self.s
            self.c -= self.s
        
        self.r = ((self.r-1) % N) + 1
        self.c = ((self.c-1) % N) + 1
    
    def __repr__(self) -> str:
        return f"({self.r},{self.c},{self.m},{self.s},{self.d})"
    
N, M, K = map(int, input().split())

ball_lst = deque()

for _ in range(M):
    r_i, c_i, m_i, s_i, d_i = map(int, input().split())
    ball_lst.append(Ball(r_i, c_i, m_i, s_i, d_i))

cnt = 0

# 1000 * 50 * 50
while cnt < K:
    world = {}
    for i in range(1, N+1):
        for j in range(1, N+1):
            world[(i,j)] = []
    
    for _ in range(len(ball_lst)):
        ball = ball_lst.pop()
        ball.move(N)
        world[(ball.r, ball.c)].append(ball)
    
    for key, value in world.items():
        if len(value) == 1:
            ball_lst.append(value[0])

        elif len(value) > 1:
            m_sum = 0
            s_sum = 0
            d_cnt = 0

            for ball in value:
                m_sum += ball.m
                s_sum += ball.s

                if ball.d % 2 == 0:
                    d_cnt += 1
            
            new_m = m_sum // 5
            new_s = s_sum // len(value)

            if new_m != 0:
                if d_cnt == len(value) or d_cnt == 0:
                    ball_lst.append(Ball(key[0], key[1], new_m, new_s, 0))
                    ball_lst.append(Ball(key[0], key[1], new_m, new_s, 2))
                    ball_lst.append(Ball(key[0], key[1], new_m, new_s, 4))
                    ball_lst.append(Ball(key[0], key[1], new_m, new_s, 6))
                else:
                    ball_lst.append(Ball(key[0], key[1], new_m, new_s, 1))
                    ball_lst.append(Ball(key[0], key[1], new_m, new_s, 3))
                    ball_lst.append(Ball(key[0], key[1], new_m, new_s, 5))
                    ball_lst.append(Ball(key[0], key[1], new_m, new_s, 7))
            
    cnt+=1

res = 0

for ball in ball_lst:
    res += ball.m

print(res)
