def solution(n):
    num = ['1', '2', '4']
    answer = ''

    while n > 0:
        remainder = n % 3 if n % 3 != 0 else 3
        answer = num[remainder - 1] + answer

        n = (n - 1) // 3

    return answer


solution(3)
solution(18)
solution(16)
solution(8)
solution(10)
solution(500000000)
