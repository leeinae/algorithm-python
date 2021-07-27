# 프로그래머스 후보키 (답안 참고)

from itertools import combinations


def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])

    candidate_case = []
    for i in range(1, col_len + 1):
        candidate_case.extend(combinations(range(col_len), i))

    case_set = []
    for case in candidate_case:
        temp = [tuple([item[c] for c in case]) for item in relation]

        if len(set(temp)) == row_len:
            case_set.append(case)

    answer = set(case_set.copy())
    for i in range(len(case_set)):
        for j in range(i+1, len(case_set)):
            if len(set(case_set[i]).intersection(set(case_set[j]))) == len(case_set[i]):
                answer.discard(case_set[j])
    return len(answer)


solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
          ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
