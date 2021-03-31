def possible(answer):
    for x, y, build in answer:
        if build == 0:  # 기둥
            if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif build == 1:  # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x + 1, y, 1] in answer and [x - 1, y,
                                                                                                       1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if b == 0:  # 삭제
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        elif b == 1:  # 설치
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])

    # 그냥 sorted해도 되더군
    # return sorted(answer, key=lambda pos: (pos[0], pos[1], pos[2]))
    return sorted(answer)


# result = solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
#                       [3, 2, 1, 1]])
result = solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                      [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
print(result)
