car = int(input())  # 객차의 수
passenger = list(map(int, input().split()))
max_car = int(input())  # 객차가 끌 수 있는 최대 수

dp = [0] * car
dp[0] = passenger[0]
# dp[max_car - 1] = sum(passenger[:max_car - 1])
for i in range(max_car - 1, car):
    dp[i] = max(dp[i - 1] + passenger[i], dp[i - max_car] + sum(passenger[i - max_car:i]))

print(dp)


