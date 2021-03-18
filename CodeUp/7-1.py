def binary_search(target, arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


result = binary_search(39, [1, 2, 3, 4, 5, 7, 9, 10, 11, 17, 31, 39])
if result is None:
    print("no result")
else:
    print(result)

# 많은 양의 입출력 받기
import sys
data = sys.stdin.readline().rstrip()
