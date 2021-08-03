from collections import deque


def solution(m, n, infests, vaccinateds):
    office = [[0] * (n + 1) for _ in range(m + 1)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x, y in infests:
        office[x][y] = 1

    for x, y in vaccinateds:
        office[x][y] = -1

    q = deque(infests)
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 1 <= nx <= m and 1 <= ny <= n and office[nx][ny] == 0:
                office[nx][ny] += office[cx][cy] + 1
                q.append([nx, ny])

    uninfected = sum(office, []).count(0) - (n + m + 1)
    return -1 if uninfected > 0 else max(max(office)) - 1


print(solution(2, 4, [[1, 4], [2, 2]], [[1, 2]]))
print(solution(2, 3, [[2, 2]], [[1, 2], [2, 1], [2, 3]]))
print(solution(2, 2, [[1, 1], [2, 2]], [[1, 2], [2, 1]]))
