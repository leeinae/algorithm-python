import heapq


def dijksta(graph, start):
    distances = [int(1e9)] * len(graph)
    distances[start] = 0
    q = [(0, start)]
    heapq.heapify(q)

    while q:
        dist, curr = heapq.heappop(q)

        if distances[curr] < dist:
            continue
        for i in graph[curr]:  # 다음, 비용
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distances


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for x, y, z in fares:
        graph[x].append((y, z))
        graph[y].append((x, z))

    x = dijksta(graph, s)
    min_cost = int(1e9)
    for node in range(len(x)):
        if x[node] != int(1e9):
            cost = dijksta(graph, node)  # idx부터 모든 경로까지의 비용
            a_cost = cost[a]
            b_cost = cost[b]
            min_cost = min(a_cost + b_cost + x[node], min_cost)
    return min(min_cost, x[a] + x[b])


solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]])
