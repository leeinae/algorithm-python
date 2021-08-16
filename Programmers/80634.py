import math
from itertools import combinations


def solution(n):
    array = [True for _ in range(n)]

    for i in range(2, int(math.sqrt(n) + 1)):
        if not array[i]: continue
        for j in range(i + i, n, i):
            array[j] = False

    prime_number = [num for num in range(2, n) if array[num]]
    return len([c for c in combinations(prime_number, 3) if sum(c) == n])


solution(33)
solution(9)
