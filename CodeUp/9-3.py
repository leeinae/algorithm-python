'''
플루이드 와샬 알고리즘
다익스트라 알고리즘이 한 노드에서의 최소 경로(비용)을 알아내는 알고리즘이라면
플루이드 와샬은 모든 노드에서 다른 모든 노드로의 최소 경로를 알아내는 알고리즘.
전반적인 흐름은 A,B 노드가 있으면 A-B로의 경로와 A-K-B 경로의 비용을 비교하여 갱신한다.
n개의 노드가 있다고 할 때, 모든 노드에 대해 O(n^2) 연산을 하기 때문에 총 시간 복잡도는 O(n^3)이라고 할 수 있음.
'''

INF = int(1e9)

n, m = map(int, input().split())  # 노드의 수, 간선의 수
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())  # a에서 b로 가는 비용 c
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INF", end="")
        else:
            print(graph[a][b], end=" ")
    print()

'''
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''