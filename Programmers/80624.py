from collections import deque


def solution(max_weight, specs, names):
    answer = 1

    names = deque(names)
    spec_dict = {key: int(value) for key, value in specs}

    total = 0
    while names:
        curr = names.popleft()

        total += spec_dict[curr]
        if total > max_weight:
            total = spec_dict[curr]
            answer += 1

    return answer


solution(300, [["toy", "70"], ["snack", "200"]], ["toy", "snack", "snack"])
solution(200, [["toy", "70"], ["snack", "200"]], ["toy", "snack", "toy"])
