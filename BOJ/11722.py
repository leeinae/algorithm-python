def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            right = mid
        else:
            left = mid + 1
    return right


n = int(input())
nums = list(map(int, input().split()))

s = [1001]
for i in range(n):
    if nums[i] < s[-1]:
        s.append(nums[i])
    else:
        idx = lower_bound(s, nums[i])
        s[idx] = nums[i]

print(len(s) - 1)
