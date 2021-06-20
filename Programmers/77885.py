# 프로그래머스 2개 이하로 다른 비트
def solution(numbers):
    answer = []
    for number in numbers:
        num = list('0' + bin(number)[2:])
        idx = int("".join(num).rfind('0'))
        num[idx] = '1'

        if number % 2 != 0:  # 짝수
            num[idx + 1] = '0'
        answer.append(int("0b" + "".join(num), 2))
    return answer


solution([2, 7, 10, 9, 5, 1, 30, 31, 32, 20, 0])
