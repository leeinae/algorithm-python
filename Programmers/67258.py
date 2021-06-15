def solution(gems):
    answer = []
    type_set = set(gems)
    type_dict = {gems[0]: 1}

    left, right = 0, 0
    while left < len(gems) and right < len(gems):
        if len(type_dict) == len(type_set):
            answer.append([left + 1, right + 1])

            if type_dict[gems[left]] == 1:
                del type_dict[gems[left]]
            else:
                type_dict[gems[left]] -= 1

            left += 1
        else:
            right += 1
            if right == len(gems): break

            if gems[right] in type_dict.keys():
                type_dict[gems[right]] += 1
            else:
                type_dict[gems[right]] = 1

    answer.sort(key=lambda x: x[1] - x[0])
    return answer[0]


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
