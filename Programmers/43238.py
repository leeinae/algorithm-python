# 프로그래머스 입국심사

def solution(n, times):
    answer = 0
    left, right = 0, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        count = sum([mid // time for time in times])

        if count >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


solution(6, [7, 10])
solution(10, [3, 8, 3, 6, 9, 2, 4])
