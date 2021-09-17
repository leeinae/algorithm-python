from itertools import permutations


def search(total, curr, prev, count, visited):
    global answer, n, nums
    total = total + abs(curr - prev) if count != 1 else 0
    if count == n:
        answer = max(answer, total)
        return

    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            search(total, nums[i], curr, count + 1, visited)
            visited[i] = False


n = int(input())
nums = list(map(int, input().split()))
# visited = [False] * len(nums)
answer = 0
# search(0, 0, 0, 0, visited)

for p in permutations(nums, n):
    total = 0
    for i in range(1, len(p)):
        total += abs(p[i] - p[i - 1])
    answer = max(answer, total)
print(answer)
