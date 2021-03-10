def solution():
    n, m = map(int, input().split())

    answer = 0
    for i in range(n):
        min_num = min(list(map(int, input().split())))
        # answer = min_num if answer < min_num else answer
        answer = max(min_num, answer)
    print(answer)

solution()