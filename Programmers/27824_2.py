import heapq


def solution(n, works):
    if sum(works) <= n: return 0
    works = list(map(lambda x: -x, works))
    heapq.heapify(works)

    while n > 0:
        heapq.heappush(works, heapq.heappop(works) + 1)
        n -= 1

    print(sum(map(lambda x: x ** 2, works)))
    return sum(map(lambda x: x ** 2, works))


solution(4, [4, 3, 3])
solution(1, [2, 1, 2])
solution(3, [1, 1])
