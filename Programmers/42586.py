def solution(progresses, speeds):
    answer = []
    q = []

    for i in range(len(progresses)):
        remain_progress = 100 - progresses[i]
        r = 0 if remain_progress % speeds[i] == 0 else 1
        q.append((remain_progress // speeds[i]) + r)

    deploy = q[0]
    count = 0
    while q:
        if deploy >= q[0]:
            count += 1
            q.pop(0)

            if len(q) == 0:
                answer.append(count)
        else:
            answer.append(count)
            count = 0
            deploy = q[0]

    return answer


solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
