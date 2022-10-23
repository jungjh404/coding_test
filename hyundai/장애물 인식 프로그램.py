from collections import deque

obstacle_set = set()
size = 0

N = int(input())

for i in range(N):
    row = list(input())
    for j in range(N):
        if row[j] == '1':
            obstacle_set.add((i,j,))
            size += 1

queue = deque([obstacle_set.pop()])
size -= 1
queue_size = 1
cur_size = 1

nears = [(-1,0),(1,0),(0,1),(0,-1)]

# bfs
answer = []

while size > 0:
    if queue_size == 0:
        answer.append(cur_size)
        
        queue.append(obstacle_set.pop())
        size -= 1
        queue_size += 1
        cur_size = 1
        continue

    current_node = queue.popleft()
    queue_size -= 1

    for near in nears:
        near_node = (current_node[0] + near[0], current_node[1] + near[1])
        if near_node in obstacle_set:
            queue.append(near_node)
            queue_size += 1
            cur_size += 1
            obstacle_set.remove(near_node)
            size -= 1
answer.append(cur_size)
answer.sort()

print(len(answer))
for num in answer:
    print(num)