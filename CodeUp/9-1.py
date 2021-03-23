'''
다익스트라 알고리즘 구현
시작 노드가 주어졌을 때 그 노드로부터 최소 비용을 차지하는 노드를 찾아서 탐색하는 알고리즘.
1. 리스트로 최소 거리를 저장하고 관리한다.
2. 우선순위 큐로 최소 비용이 소요되는 노드를 관리한다. O(nlogn)의 복잡도를 가짐
파이썬의 우선순위 큐는 최소 힙으로 구현되어 있음
'''


INF = int(1e9)

n, m = map(int, input().split())  # 노드 수, 간선 수
start = int(input())  # 시작 노드 번호
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)  # 최단 거리 테이블을 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())  # a -> b로 가는 비용 c
    graph[a].append((b, c))


# 방문하지 않는 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if not visited[i] and min_value > distance[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    # start에서 연결된 간선에 대해 비용을 넣어줌
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()

        for j in graph[now]:
            cost = distance[now] + j[1]
            distance[j[0]] = cost if cost < distance[j[0]] else distance[[j][0]]


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


