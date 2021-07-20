def solution(people, limit):
    answer = len(people)
    people.sort()

    left, right = 0, len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            answer -= 1
            left += 1
        right -= 1

    return answer
