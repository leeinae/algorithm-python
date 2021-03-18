x = int(input())

dp = [0] * (x + 1)

for i in range(2, x + 1):
    result = dp[i - 1] + 1

    if i % 2 == 0:
        result = min(result, dp[i // 2] + 1)
    if i % 3 == 0:
        result = min(result, dp[i // 3] + 1)
    dp[i] = result

print(dp[x])
