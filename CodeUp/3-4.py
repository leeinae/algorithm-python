'''
그리디 - 1이 될 때까지
입력으로 주어진 n, k가 있을 때
1. n이 k로 나눠떨어지면 n을 k로 나눔
2. n에서 1을 뺌
이 두 가지 연산 중 한 가지만 선택해서 수행할 때 최소 수행 횟수를 출력
'''

def solution():
    n, k = map(int, input().split())

    count = 0
    while n != 1:
        n //= k if n % k == 0 else n - 1
        count += 1

    print(count)

solution()