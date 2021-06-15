def solution(gems):
    answer = []
    type_set = set(gems)

    left, right = 0, 0
    min_value = len(gems)
    while right < len(gems):
        temp = set([gems[g] for g in range(left, right + 1)])

        if len(temp) == len(type_set):
            if min_value >= right - left:
                answer.append([left + 1, right + 1])
                min_value = min(right - left, min_value)
            left += 1
        else:
            right += 1

    answer.sort(key=lambda x: x[1] - x[0])
    return answer[0]


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
