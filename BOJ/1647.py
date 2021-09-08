import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


input = sys.stdin.readline
n, m = map(int, input().split())
road = [] * m
node = [i for i in range(n + 1)]
answer = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    road.append((a, b, c))

road.sort(key=lambda x: x[2])
last_cost = 0

for a, b, cost in road:
    a = find(node, a)
    b = find(node, b)

    if a != b:
        if a < b:
            node[b] = a
        else:
            node[a] = b
        answer += cost
        last_cost = cost
print(answer - last_cost)
