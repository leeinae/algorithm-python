def inquiry_rank(count):
    return 6 if 7 - count >= 6 else 7 - count


def solution(lottos, win_nums):
    answer = []

    zero_count = 0  # 0의 개수
    curr_count = 0  # 현재 일치하는 수의 개수
    for lotto in lottos:
        if lotto == 0: zero_count += 1
        if lotto in win_nums: curr_count += 1

    answer.append(inquiry_rank(zero_count + curr_count))
    answer.append(inquiry_rank(curr_count))

    print(answer)
    return answer


solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
