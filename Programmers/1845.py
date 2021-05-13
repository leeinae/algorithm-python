def solution(nums):
    return len(nums) // 2 if len(set(nums)) >= len(nums) // 2 else len(set(nums))

solution([3, 1, 2, 3])
solution([3, 3, 3, 2, 2, 2])
solution([3, 3, 3, 3])
