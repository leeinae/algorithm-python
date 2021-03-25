from collections import deque
import heapq


# # 정확성 통과, 효율성 실패
# def solution(food_times, k):
#     answer = -1
#     total_count = 0
#
#     q = deque()
#     for i in range(len(food_times)):
#         if food_times[i] == 0: continue
#         q.append((food_times[i], i + 1))  # (food 값, idx 번호)
#
#     while q:
#         food, idx = q.popleft()
#         if total_count == k:
#             answer = idx
#             break
#
#         total_count += 1
#         if food - 1 == 0:
#             continue
#         else:
#             q.append((food - 1, idx))
#
#     return answer


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        if food_times[i] == 0: continue
        heapq.heappush(q, (food_times[i], i + 1))  # (food 값, idx 번호)

    food_length = len(food_times)
    prev = 0
    sum_times = 0
    while sum_times + (food_length * (q[0][0] - prev)) <= k:
        food = heapq.heappop(q)[0]

        sum_times += (food - prev) * food_length
        food_length -= 1
        prev = food

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_times) % food_length][1]


# answer = solution([3, 1, 2], 2)
# answer = solution([3, 1, 2], 5)
# answer = solution([5, 1, 1], 1)
# answer = solution([4, 2, 3, 6, 7, 1, 5, 8], 27)
# answer = solution([4, 2, 3, 6, 7, 1, 5, 8], 16)
answer = solution([0, 0, 0, 0, 0, 0, 0], 16)
print(answer)
