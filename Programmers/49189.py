# 프로그래머스 가장 먼 노드
from collections import deque


def solution(n, edge):
    adj = [[] for _ in range(n)]
    visited = [False] * n
    distance = [-1] * n

    for a, b in edge:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    distance[0] = 0

    q = deque([0])
    while q:
        temp = q.popleft()

        for node in adj[temp]:
            if not visited[node] and distance[node] == -1:
                q.append(node)
                visited[temp] = True
                distance[node] = distance[temp] + 1

    return distance.count(max(distance))


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
solution(4, [[1, 2], [2, 4], [2, 3]])
solution(4, [[1, 2], [1, 3], [2, 3], [2, 4]])
solution(4, [[1, 2], [2, 4]])
solution(4, [])
solution(4, [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]])
solution(4, [[1, 2], [2, 3], [3, 4]])
solution(7, [[1, 2], [1, 6], [1, 5], [3, 4], [4, 5], [4, 7]])
solution(6, [[1, 2], [2, 4], [3, 4], [3, 5], [5, 6]])
