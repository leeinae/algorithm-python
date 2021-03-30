from collections import deque

'''
빈 칸 0
사과 1
머리 2
꼬리 -2
방향 0: 북, 1: 서, 2: 남, 3: 동
'''

n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
k = int(input())

snake_dir = 1
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1
l = int(input())
q = deque()
for _ in range(l):
    time, dir = input().split()
    q.append((int(time), dir))

time_counter = 0
dir_change_counter = q[0][0]
snake = deque([(1, 1)])
while True:
    time_counter += 1

    sx, sy = snake[0]
    if snake_dir == 0:
        sx -= 1
    elif snake_dir == 1:
        sy += 1
    elif snake_dir == 2:
        sx += 1
    else:
        sy -= 1

    # 종료 조건
    if sx <= 0 or sx > n or sy <= 0 or sy > n:
        break
    if (sx, sy) in snake:
        break

    snake.appendleft((sx, sy))
    # 다음 칸이 사과가 아닌 경우
    if board[sx][sy] == 0:
        snake.pop()
    board[sx][sy] = 0

    # 방향 변경
    if time_counter == dir_change_counter:
        dir = q.popleft()[1]
        if dir == 'L':
            snake_dir = (snake_dir - 1 + 4) % 4
        else:
            snake_dir = (snake_dir + 1) % 4
        dir_change_counter = q[0][0] if q else -1

print(time_counter)
