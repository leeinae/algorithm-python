def hanoi(first, second, third, idx, answer):  # n -> m으로 이동
    if idx == 1:
        answer.append([first, third])
        return

    hanoi(first, third, second, idx - 1, answer)
    answer.append([first, third])
    hanoi(second, first, third, idx - 1, answer)


def solution(n):
    answer = []
    hanoi(1, 2, 3, n, answer)
    return answer


print(solution(2))
