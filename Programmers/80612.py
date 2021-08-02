# 더 맵게, 25분 소요

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        try:
            first, second = heapq.heappop(scoville), heapq.heappop(scoville)
            heapq.heappush(scoville, first + (second * 2))
            answer += 1
        except:
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 5], 5))
