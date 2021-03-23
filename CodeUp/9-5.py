import heapq

INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, idx = heapq.heappop(q)

        if dist > distance[idx]: continue

        for i in graph[idx]:  # i: (인덱스, 걸리는 시간)
            if i[1] + dist < distance[i[0]]:
                distance[i[0]] = i[1] + dist
                heapq.heappush(q, (distance[i[0]], i[0]))


dijkstra(c)

count = 0
time = 0
for i in distance:
    if i >= INF: continue

    count += 1
    time = max(time, i)

print(count - 1, time)
