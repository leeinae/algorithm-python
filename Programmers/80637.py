def solution(brown, red):
    answer = []
    total = brown + red
    # 세로
    for col in range(3, total // 2):
        row = total // col
        if row < col: break
        if total % col == 0 and (row - 2) * (col - 2) == red:
            answer.extend([row, col])

    return answer


solution(10, 2)
solution(8, 1)
solution(24, 24)
