'''
백준 1793_타일링
* 기존과 똑같은 문제였으나 테스트 케이스 입력의 수가 정해지지 않음 -> try catch로 런타임 에러 감지
* n = 0일때도 고려했어야 함
'''

dp = [0] * 251
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, 251):
    dp[i] = dp[i - 1] + (2 * dp[i - 2])

while True:
    try:
        n = int(input())
        print(dp[n])
    except:
        break
