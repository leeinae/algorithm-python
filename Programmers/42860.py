def solution(name):
    answer = 0
    # 상하 탐색
    change = [min(ord(c) - ord('A'), ord('Z') + 1 - ord(c)) for c in name]

    # 좌우 탐색
    idx = 0
    while True:
        answer += change[idx]
        change[idx] = 0

        if sum(change) == 0:
            break

        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1

        idx += -left if left < right else right
        answer += left if left < right else right
    return answer


solution('JAZ')
solution('ACCCCA')
solution('CCCCV')
solution('JEROEN')
solution('JAN')
