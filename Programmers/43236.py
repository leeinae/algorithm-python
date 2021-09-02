def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()

    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2  # 거리 최솟값

        prev, count = 0, 0
        min_distance = distance
        for rock in rocks:
            d = rock - prev
            if d < mid:  # 삭제
                count += 1
            else:
                print(min_distance, d)
                min_distance = min(min_distance, d)
                prev = rock

        if count <= n:
            left = mid + 1
            answer = min_distance
        else:
            right = mid - 1

    return answer


solution(25, [2, 14, 11, 21, 17], 2)
solution(16, [4, 8, 11], 2)
