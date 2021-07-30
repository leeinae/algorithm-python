from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    days = deque()

    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    print(days)
    days.append(101)

    prev = days.popleft()
    num = 1
    while days:
        curr = days.popleft()
        if prev >= curr:
            num += 1
        else:
            answer.append(num)
            num = 1
            prev = curr
    print(answer)
    return answer


solution([93, 30, 55], [1, 30, 5])
solution([0, 1, 20, 30, 40, 20], [20, 30, 1, 1, 1, 1])
