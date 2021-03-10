'''
그리디 - 거스름돈
거슬러줘야할 돈이 n일때, 거슬러 줘야 할 동전의 최소 개수 구하기
'''

def solution():
    n = int(input())
    money = (500, 100, 50, 10)
    count = 0

    for _ in money:
        count += n // _
        n %= _

    print(count)


solution()
