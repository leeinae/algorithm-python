def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def solution(n, costs):
    answer = 0
    node = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2])

    for x, y, c in costs:
        x = find(node, x)
        y = find(node, y)

        if x != y:  # 사이클이 발생하지 않는 경우
            if x < y:
                node[y] = x
            else:
                node[x] = y
            answer += c
        if sum(node) == 0: break
    print(answer)
    return answer


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]])
solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]])
