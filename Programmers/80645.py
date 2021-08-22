def solution(d, budget):
    answer = 0
    if sum(d) < budget: return len(d)
    d.sort()

    for cost in d:
        budget -= cost
        answer += 1
        if budget == 0:
            return answer
        elif budget < 0:
            return answer - 1


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
