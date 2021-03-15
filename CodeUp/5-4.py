from collections import deque


def bfs(x, y):
    global answer
    q = deque([(x, y)])
    values[x][y] = 1

    while q:
        temp = q.popleft()

        x, y = temp[0], temp[1]
        if x == n - 1 and y == m - 1:
            print(answer)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if maze[nx][ny] == 0 or values[nx][ny] > 0: continue

            q.append((nx, ny))
            values[nx][ny] = values[x][y] + 1
            answer = max(answer, values[nx][ny])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
maze = []
values = []

for _ in range(n):
    maze.append(list(map(int, input())))
    values.append([0] * m)

answer = 0
bfs(0, 0)
