from collections import deque
import copy

direction = [[-1, 1, 0, 0], [0, 0, -1, 1]]


def bfs(x, y, place):
    q = deque([[x, y]])
    visited = [[False] * 5 for _ in range(5)]

    place[x][y] = 0
    while q:
        cx, cy = q.popleft()
        visited[cx][cy] = True

        for _ in range(4):
            nx = cx + direction[0][_]
            ny = cy + direction[1][_]

            if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] != 'X' and not visited[nx][ny]:
                distance = place[cx][cy] + 1

                if place[nx][ny] == 'P' and distance <= 2: return 1
                place[nx][ny] = distance
                visited[nx][ny] = True
                q.append([nx, ny])
    return 0


def solution(places):
    answer = []

    for place in places:
        place = [list(p) for p in place]

        loopBreak = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if bfs(i, j, copy.deepcopy(place)) == 1:
                        answer.append(0)
                        loopBreak = True
                        break
            if loopBreak: break
        else:
            answer.append(1)

    print(answer)
    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])

solution([["PXOOO", "OOOOO", "PXOOO", "OOOOO", "OOOPO"]])
