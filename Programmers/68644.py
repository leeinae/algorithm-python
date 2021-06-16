# 프로그래머스 두 개 뽑아서 더하기 2: 40 시작
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer = list(set(answer))
    answer.sort()
    return answer


solution([2, 1, 3, 4, 1])
solution([0, 0, 2])
