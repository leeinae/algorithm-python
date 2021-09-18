import heapq
import sys

sys = sys.stdin.readline
n = int(sys())
m = int(sys())
costs = [int(1e9)] * (n + 1)
routes = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, sys().split())
    routes[x].append((y, z))  # 도착지, 비용
start, end = map(int, sys().split())
costs[start] = 0

q = [[costs[start], start]]
heapq.heapify(q)
while q:
    curr_cost, curr_dest = heapq.heappop(q)
    if costs[curr_dest] < curr_cost: continue  # 기존에 있는 거리보다 길다면 패스

    for d, c in routes[curr_dest]:
        cost = costs[curr_dest] + c
        if cost < costs[d]:
            costs[d] = cost
            heapq.heappush(q, [cost, d])

print(costs[end])
