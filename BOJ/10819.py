def search(selected, visited):
    global answer, n, nums
    if len(selected) == n:
        total = 0
        for i in range(1, len(selected)):
            total += abs(selected[i] - selected[i - 1])
        answer = max(answer, total)
        return

    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            selected.append(nums[i])
            search(selected, visited)
            visited[i] = False
            selected.pop()


n = int(input())
nums = list(map(int, input().split()))
visited = [False] * len(nums)
answer = 0
search([], visited)

print(answer)
