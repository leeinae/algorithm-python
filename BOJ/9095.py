def add_num(total, num):
    global answer, n
    total += num
    if total > n:
        return
    elif total == n:
        answer += 1

    add_num(total, 1)
    add_num(total, 2)
    add_num(total, 3)


test_case = int(input())

for t in range(test_case):
    n = int(input())
    answer = 0

    dp = [0] * 11
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])
