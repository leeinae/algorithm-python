from collections import deque


def solution(enter, leave):
    answer = [0] * len(enter)

    stack = []
    leave_queue = deque(leave)
    print(leave_queue)
    cusor = 0
    while cusor < len(enter):
        print(enter[cusor])
        stack.append(enter[cusor])

        while leave_queue[0] in stack:
            temp = len(stack) - 1
            for i in stack:
                answer[i - 1] += temp
            print(answer)
            stack.pop()
            leave_queue.popleft()
        cusor += 1

    return answer


result = solution([1, 4, 2, 3], [2, 1, 3, 4])
print(result)
