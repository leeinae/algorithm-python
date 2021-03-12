def solution():
    n = int(input().strip())

    weight = [int(input().strip()) for i in range(n)]
    weight.sort(reverse=True)

    value = []
    for i in range(n):
        value.append(weight[i] * (i + 1))

    print(max(value))


solution()
