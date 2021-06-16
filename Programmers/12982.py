# 프로그래머스 예산

def solution(d, budget):
    d.sort()

    count, answer = 0, 0
    for i in range(len(d)):
        if count + d[i] > budget: break
        count += d[i]
        answer += 1
    return answer


solution([1, 2, 3, 4, 5], 9)
solution([2, 2, 3, 3], 10)
