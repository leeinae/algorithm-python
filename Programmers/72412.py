from itertools import combinations


def solution(info, query):
    answer = []
    applicant = dict()

    for i in info:
        i = i.split()
        conditions = i[:-1]
        score = int(i[-1])

        for n in range(5):
            comb = list(combinations(range(4), n))
            for c in comb:
                t_c = conditions.copy()
                for v in c:
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in applicant:
                    applicant[changed_t_c].append(score)
                else:
                    applicant[changed_t_c] = [score]

    for i in applicant.values():
        i.sort()

    for q in query:
        q = [i for i in q.split() if i != 'and']
        query_condition = '/'.join(q[:-1])
        query_score = int(q[-1])

        if query_condition in applicant:
            data = applicant[query_condition]

            if len(data) > 0:
                start = 0
                end = len(data)
                while start < end:
                    mid = (start + end) // 2

                    if data[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(data) - start)
        else:
            answer.append(0)
    print(answer)
    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 150", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 140",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 150",
          "- and - and - and - 150"])
