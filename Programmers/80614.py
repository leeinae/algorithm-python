# 게임 아이템, 소요시간 2시간 이상 ;;

import heapq
from collections import deque


def solution(healths, items):
    answer = []

    item_dict = dict()  # 공격력
    for i in range(len(items)):
        item_dict[items[i][0]] = i + 1

    items.sort(key=lambda x: x[1])  # 공격력, 체력
    items = deque(items)
    healths.sort()

    result = []
    for health in healths:
        while items and health - items[0][1] >= 100:
            item = items.popleft()
            heapq.heappush(result, (-item[0], item_dict[item[0]]))  # 공격력, 아이템
        if result:
            answer.append(heapq.heappop(result)[1])

    answer.sort()
    return answer


solution([200, 120, 150], [[30, 100], [500, 30], [100, 400]])
solution([300, 200, 500], [[1000, 600], [400, 500], [300, 100]])
solution([500], [[30, 100], [500, 30], [100, 400]])  # 공격력, 체력
solution([500, 120, 100], [[300, 0], [1, 0], [2, 0], [3, 0]])  # 공격력, 체력
