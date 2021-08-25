def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    return sum(map(lambda x: x[0] * x[1], list(zip(A, B))))


solution([1, 2], [3, 4])
solution([1, 4, 2], [5, 4, 4])
solution([0, 5, 7], [0, 1, 5])
