# 더 맵게, 25분 소요

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        first = heapq.heappop(scoville)
        if first >= K: break

        if len(scoville) > 0:
            answer += 1
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + (second * 2))
    else:
        return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 5], 5))
