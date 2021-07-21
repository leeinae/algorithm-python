from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cities = deque(list(map(lambda x: x.lower(), cities)))
    cache = deque()

    if cacheSize == 0: return len(cities) * 5

    while cities:
        curr_city = cities.popleft()

        if curr_city in cache:
            cache.remove(curr_city)
            cache.append(curr_city)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(curr_city)
            answer += 5

    return answer


solution(2,
         ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
          "Rome"])
solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(5, ["Jeju", "Pangyo", "NewYork", "newyor"])
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
solution(5, ["SEOUL", "SEOUL", "SEOUL"])
