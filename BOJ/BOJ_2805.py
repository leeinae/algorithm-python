n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)


def cut_tree(h):
    result = 0
    for tree in trees:
        if tree > h:
            result += (tree - h)
    return result


answer = 0
while start <= end:
    middle = (start + end) // 2  # 높이
    result = cut_tree(middle)

    if result >= m:
        start = middle + 1
        answer = middle
    else:
        end = middle - 1

print(answer)
