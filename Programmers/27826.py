from itertools import combinations


def solution(nums):
    answer = 0
    numbers = [True] * 3000

    for i in range(2, 3000):
        for j in range(i + i, len(numbers), i):
            if numbers[j] // i == 0:
                numbers[j] = False

    prime_numbers = [n for n in range(2, len(numbers)) if numbers[n]]

    for c in combinations(nums, 3):
        if sum(c) in prime_numbers: answer += 1

    return answer


solution([1, 2, 3, 4])
solution([1, 2, 7, 6, 4, ])
