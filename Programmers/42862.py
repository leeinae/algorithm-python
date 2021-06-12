def solution(n, _lost, _reserve):
    reserve = [r for r in _reserve if r not in _lost]
    lost = [l for l in _lost if l not in _reserve]

    for r in range(len(reserve)):
        value = 1
        for i in range(2):
            num = reserve[r] - value
            value *= -1

            if num in lost:
                reserve[r] = -1
                lost.remove(num)

    count = 0
    for i in lost:
        if i > 0:
            count += 1

    return n - count


solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])
solution(5, [1, 3, 5], [2, 3, 4])
solution(5, [5, 4, 3, 2, 1], [3, 1, 2, 5, 4])
