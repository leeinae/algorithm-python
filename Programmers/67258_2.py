def solution(gems):
    answer = []
    start, end = 0, 0
    gem_type = set(gems)
    gem_dict = {gems[0]: 1}

    while start < len(gems) and end < len(gems):
        if len(gem_dict) == len(gem_type):
            answer.append([start + 1, end + 1])

            if gem_dict[gems[start]] == 1:
                del gem_dict[gems[start]]
            else:
                gem_dict[gems[start]] -= 1

            start += 1
        else:
            end += 1
            if end == len(gems): break
            if gems[end] in gem_dict:
                gem_dict[gems[end]] += 1
            else:
                gem_dict[gems[end]] = 1

    answer.sort(key=lambda x: x[1] - x[0])
    return answer[0]


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
