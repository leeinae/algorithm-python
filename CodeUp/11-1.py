n = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0
idx = len(arr) - 1
while True:
    if idx < 0:
        break

    count += 1
    idx -= arr[idx]

print(count)
