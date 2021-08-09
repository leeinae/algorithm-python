from collections import defaultdict


def solution(board, nums):
    answer = 0
    num_dict = defaultdict(int)

    for num in nums:
        num_dict[num] += 1

    for i in range(len(board)):
        for j in range(len(board)):
            if num_dict[board[i][j]] == 1:
                board[i][j] = 0

    # 대각선 체크
    answer += int(sum(board[i][i] for i in range(len(board))) == 0)
    answer += int(sum(board[i][len(board) - 1 - i] for i in range(len(board))) == 0)

    # 가로 체크
    # answer += [sum(board[i]) for i in range(len(board))].count(0)
    answer += len([i for i in board if sum(i) == 0])

    # 세로 체크
    # answer += [sum(list(zip(*board[::-1]))[i]) for i in range(len(board))].count(0)
    answer += len([i for i in zip(*board) if sum(i) == 0])


    print(answer)
    return answer


solution([[11, 13, 15, 16], [12, 1, 4, 3], [10, 2, 7, 8], [5, 14, 6, 9]], [14, 3, 2, 4, 13, 1, 16, 11, 5, 15])
solution([[6, 15, 17, 14, 23], [5, 12, 16, 13, 25], [21, 4, 2, 1, 22], [10, 20, 3, 18, 8], [11, 9, 19, 24, 7]],
         [15, 7, 2, 25, 9, 16, 12, 18, 5, 4, 10, 13, 20])
