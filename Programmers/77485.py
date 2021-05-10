def solution(rows, columns, queries):
    answer = []
    arr = [[(columns * r) + c for c in range(1, columns + 1)] for r in range(rows)]

    for query in queries:
        q = []

        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        for i in range(y1, y2 + 1): q.append(arr[x1][i])
        for i in range(x1 + 1, x2 + 1): q.append(arr[i][y2])
        for i in range(y2 - 1, y1, -1): q.append(arr[x2][i])
        for i in range(x2, x1, -1): q.append(arr[i][y1])

        answer.append(min(q))

        for i in range(y1 + 1, y2 + 1): arr[x1][i] = q.pop(0)
        for i in range(x1 + 1, x2 + 1): arr[i][y2] = q.pop(0)
        for i in range(y2 - 1, y1, -1): arr[x2][i] = q.pop(0)
        for i in range(x2, x1 - 1, -1): arr[i][y1] = q.pop(0)

    print(answer)
    return answer


solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])
# solution()
