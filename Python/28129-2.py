from itertools import combinations


def solution(needs, r):
    answer = 0

    for c in combinations(range(0, len(needs[0])), r):
        count = 0
        for need in needs:
            part = set([i for i, x in enumerate(need) if x == 1])
            if set(c).intersection(part) == part:
                count += 1
        answer = max(answer, count)
    print(answer)
    return answer


solution([[1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1]], 2)
