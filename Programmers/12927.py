# 프로그래머스 야근 지수
import heapq


def solution(n, works):
    answer = 0
    works = [w * (-1) for w in works]
    heapq.heapify(works)

    while n != 0:
        temp = heapq.heappop(works)

        if temp == 0: break
        heapq.heappush(works, temp + 1)
        n -= 1

    for w in works:
        answer += abs(w) ** 2
    print(answer)
    return answer


solution(4, [4, 3, 3])
solution(1, [2, 2, 1])
solution(3, [1, 1])
