'''
효율적인 화폐 구성
n가지 종류의 화폐로 m원을 만들기 위한 최소한의 화폐 개수를 출력
'''

n, m = map(int, input().split())
arr = [int(input()) for i in range(n)]
dp = [10001] * 101

for i in arr:
    dp[i] = 1

for i in range(1, m + 1):
    for j in arr:
        if i - j >= 1 and dp[i - j] != 0:
            dp[i] = min(dp[i], dp[i - j] + 1)

dp[m] = 10001 if dp[m] == 0 else dp[m]
print(dp[m])
