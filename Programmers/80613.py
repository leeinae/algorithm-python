# 프로그래머스 배상비용 최소화 사본, 15분 소요
import heapq


def solution(no, works):
    works = list(map(lambda x: -x, works))
    heapq.heapify(works)

    while no > 0:
        work = heapq.heappop(works)
        if work == 0: break

        heapq.heappush(works, work + 1)
        no -= 1

    return sum(map(lambda x: x ** 2, works))


print(solution(8, [2, 2, 2]))
print(solution(2, [3, 3, 3]))
print(solution(4, [4, 3, 3]))
