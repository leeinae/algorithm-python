# 프로그래머스 프린터
from collections import deque


def solution(priorities, location):
    count = 0
    printer = deque((p, priorities[p]) for p in range(len(priorities)))

    while printer:
        idx, priority = printer.popleft()

        max_value = max(printer, key=lambda x: x[1]) if len(printer) != 0 else (0, -1)
        if priority < max_value[1]:
            printer.append((idx, priority))
        else:
            count += 1
            if idx == location: break

    return count


solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 1)
solution([1], 0)
