import math
from itertools import permutations


def is_prime_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        per = permutations(numbers, i)
        for p in per:
            number = int("".join(p))
            if number == 0 or number == 1: continue
            if is_prime_number(number) and number not in answer:
                answer.append(number)
    return len(answer)


solution("17")
solution("011")
solution("0001231")
