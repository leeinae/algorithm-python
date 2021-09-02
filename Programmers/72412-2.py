from itertools import combinations


def solution(info, query):
    result = []
    score_dict = dict()

    for i in info:
        i = i.split()
        condition = i[:-1]
        score = int(i[-1])

        for j in range(0, len(condition) + 1):
            for c in combinations(condition, j):
                new_condition = "|".join(c)
                if new_condition in score_dict:
                    score_dict[new_condition].append(score)
                else:
                    score_dict[new_condition] = [score]

    for i in score_dict.values():
        i.sort()
    for q in query:
        q = q.split()
        score = int(q[-1])
        condition = "|".join([i for i in q[:-1] if i not in ('and', '-')])

        if condition in score_dict:
            score_list = score_dict[condition]

            if len(score_list) < 0: continue
            left, right = 0, len(score_list)
            while left < right:
                mid = (left + right) // 2

                if score_list[mid] < score:
                    left = mid + 1
                else:
                    right = mid
            result.append(len(score_list) - left)
        else:
            result.append(0)

    return result


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])
