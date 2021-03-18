def cutting_dduck(arr, length):
    total = 0
    for i in arr:
        if i >= length:
            total += (i - length)
    return total


def binary_search(arr, target, start, end):
    mid = (start + end) // 2 # 설정한 높이
    temp = cutting_dduck(arr, mid) # 잘린 떡의 길이

    if temp == target:
        print(mid)
        return
    elif temp < target:
        binary_search(arr, target, start, mid - 1)
    else:
        binary_search(arr, target, mid + 1, end)


n, m = map(int, input().split())
dduck = list(map(int, input().split()))
binary_search(dduck, m, 0, max(dduck))
