def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    result = a[n - k + 1:] + b[0:k]
    print(sum(result))


solution()
