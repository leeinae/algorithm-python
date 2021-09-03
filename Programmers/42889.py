def solution(N, stages):
    stage_dict = dict()

    total = len(stages)
    for n in range(1, N + 1):
        fail = stages.count(n)

        stage_dict[n] = fail / total if total != 0 else 0
        total -= fail

    return [i[0] for i in sorted(stage_dict.items(), key=lambda x: -x[1])]


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4, 4, 4, 4, 4])
