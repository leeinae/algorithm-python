def solution():
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(list(input().split()))

    arr.sort(key=lambda student: student[1])
    for i in range(n): print(arr[i][0], end=" ")


solution()
