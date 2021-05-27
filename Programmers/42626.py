import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    if max(scoville) == 0: return -1

    while scoville[0] < K:
        first_low, second_low = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, first_low + (second_low * 2))
        answer += 1

        if scoville[0] < K and len(scoville) == 1: return -1

    return answer


solution([1, 2, 3, 9, 10, 12], 7)
solution([8, 10, 11], 7)
solution([1, 2, 3], 11)
