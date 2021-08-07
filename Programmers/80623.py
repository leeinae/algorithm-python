from collections import Counter


def solution(v):
    answer = []

    x_dict = Counter(map(lambda x: x[0], v))
    y_dict = Counter(map(lambda x: x[1], v))

    for x in x_dict.keys():
        if x_dict[x] == 1:
            answer.append(x)

    for y in y_dict.keys():
        if y_dict[y] == 1:
            answer.append(y)

    return answer


solution([[1, 4], [3, 4], [3, 10]])
