import heapq


def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    city = [[] for _ in range(N + 1)]
    time = [INF] * (N + 1)
    time[1] = 0
    q = []

    for a, b, c in road:
        city[a].append([b, c]) # 연결 도시, 시간
        city[b].append([a, c])

    heapq.heappush(q, (0, 1)) # 시간, 도시
    while q:
        dist, curr = heapq.heappop(q)

        if time[curr] < dist: continue
        for c in city[curr]:
            cost = time[curr] + c[1]
            if cost < time[c[0]]:
                time[c[0]] = cost
                heapq.heappush(q, (cost, c[0]))

    answer = list(filter(lambda x: x <= K, time))
    return len(answer)


solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4)
