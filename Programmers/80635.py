from itertools import combinations


def solution(m, weights):
    answer = 0

    for num in range(1, len(weights)):
        for com in combinations(weights, num):
            if sum(com) == m:
                answer += 1

    return answer


solution(3000, [500, 1500, 2500, 1000, 2000])
