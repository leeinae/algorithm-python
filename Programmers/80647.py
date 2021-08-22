def solution(numbers):
    numbers = list(map(lambda x: str(x), numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(list(map(lambda x: str(int(x)), numbers)))))


print(solution([2, 20]))
print(solution([3, 30, 34, 5, 9]))
print(solution([1, 10, 20, 2]))
print(solution([0, 0, 0, 0]))
print(solution([21, 212]))
print(solution([12, 121]))
