def solution(seat):
    return len(set(map(lambda x: (x[0], x[1]), seat)))


solution([[1, 1], [2, 1], [1, 2], [3, 4], [2, 1], [2, 1]])
