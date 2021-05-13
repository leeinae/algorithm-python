def solution(nums):
    answer = 0
    num_count = len(set(nums))

    if num_count >= len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = num_count

    print(answer)
    return answer


solution([3, 1, 2, 3])
solution([3, 3, 3, 2, 2, 2])
solution([3, 3, 3, 3])
