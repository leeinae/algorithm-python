def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


n = int(input())
component = list(map(int, input().split()))

m = int(input())
check_list = list(map(int, input().split()))

component.sort()
for _ in range(m):
    result = binary_search(component, check_list[_])

    if result is False:
        print("no", end=" ")
    else:
        print("yes", end=" ")
