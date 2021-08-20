def check_lamps(dist, l, v):
    if (0 < v[0] - dist) or (v[-1] + dist < l):
        return False
    for i in range(1, len(v)):
        if v[i - 1] + dist < v[i] - dist: return False
    return True


def solution(l, v):
    answer = int(1e9)
    v.sort()

    left, right = 0, l
    while left <= right:
        mid = (left + right) // 2

        if check_lamps(mid, l, v):
            answer = min(answer, mid)

            right = mid - 1
        else:
            left = mid + 1

    return answer


solution(15, [15, 5, 3, 7, 9, 14, 0])
solution(5, [2, 5])
