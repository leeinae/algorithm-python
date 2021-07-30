def dfs(x, y, image):
    stack = [(x, y)]
    color = image[x][y]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while stack:
        curr = stack.pop()

        for i in range(4):
            nx = curr[0] + dx[i]
            ny = curr[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= len(image) or ny >= len(image[0]): continue
            if image[nx][ny] == -1 or color != image[nx][ny]: continue

            image[nx][ny] = -1
            stack.append((nx, ny))


def solution(n, m, image):
    answer = 0

    for i in range(n):
        for j in range(m):
            if image[i][j] != -1:
                dfs(i, j, image)
                answer += 1

    return answer


solution(2, 3, [[1, 2, 3], [3, 2, 1]])
solution(3, 2, [[1, 2], [1, 2], [4, 5]])
