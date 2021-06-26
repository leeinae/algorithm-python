# 프로그래머스 이중우선순위큐
import heapq


def solution(operations):
    q = []

    for operation in operations:
        operation = operation.split()

        command, number = operation[0], int(operation[1])
        if command == 'I':
            heapq.heappush(q, number)
        else:
            if len(q) == 0: continue
            if number > 0:
                max_value = max(q)
                q.remove(max_value)
            else:
                heapq.heappop(q)

    if len(q) == 0:
        return [0, 0]
    else:
        return [max(q), q[0]]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I 2", "I 4", "D -1", "I 1", "D 1"]))
