# 프로그래머스 가장 큰 수........ 풀이 참고함
def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x * 4, reverse=True)
    return str(int("".join(numbers)))


print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2, 20]))
print(solution([0, 0, 0, 0]))
print(solution([1, 10, 20]))
print(solution([2, 20, 22]))
