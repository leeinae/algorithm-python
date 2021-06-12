def solution(brown, yellow):
    total_num = brown + yellow

    for i in range(total_num // 2, 1, -1):
        if total_num % i == 0:
            width = i
            height = total_num // i

            if (width - 2) * (height - 2) == yellow:
                return [width, height]


solution(10, 2)
