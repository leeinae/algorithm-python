def code_6002():
    print("Hello World")


def code_6003():
    print("Hello")
    print("World")


def code_6004():
    print("\'Hello\'")


def code_6006():
    print("\"!@#$%^&*()\'")


def code_6009():
    print(input())


def code_6013():
    a = input()
    b = input()
    print(b, a)


def code_6014():
    a = input()
    for i in range(3):
        print(a)


def code_6027():
    a = int(input())
    print('%X' % a)


# round: 반올림 함수. 두번째로 들어가는 인자까지의 자리수만큼 표현 가눙
def code_6045():
    n1, n2, n3 = map(int, input().split())

    total = n1 + n2 + n3
    avg = total / 3
    print(total, round(avg, 2))


def code_6046():
    n = int(input())

    print(n << 1)


def code_6047():
    a, b = map(int, input().split())
    # print(a * (2 ** b))
    print(a << b)


def code_6048():
    a, b = map(int, input().split())
    print(a < b)


def code_6049():
    a, b = map(int, input().split())
    print(a == b)


def code_6059():
    n = int(input())
    print(~ n)


def code_6060():
    a, b = map(int, input().split())
    print(a & b)


def code_6062():
    a, b = map(int, input().split())
    print(a ^ b)


def code_6063():
    a, b = map(int, input().split())
    print(max(a, b))


def code_6064():
    num = list(map(int, input().split()))
    print(min(num))


def code_6065():
    while True:
        n = int(input())
        if n == 0:
            break
        print(n)


def multi_table():
    for i in range(1, 10):
        print('======= ' + str(i) + '단 =========')
        for j in range(10):
            print('{0} * {1} = {2}'.format(i, j, i * j))


def code_6082():
    num = int(input())

    for i in range(1, num + 1):
        if i % 10 in [3, 6, 9]:
            print("X", end=" ")
            continue
        print(i, end=' ')


# from itertools import product
# def code_6083():
#     rgb = input().split()
#
#     colors = [[]]
#     for i in range(len(rgb)):
#         colors[i] = [j for j in range(rgb[i])]
#
#     print(colors)

def code_6086():
    n = int(input())

    total = 0
    idx = 1
    while total < n:
        total += idx
        idx += 1

    print(total)


def code_6087():
    n = int(input())

    count = 0
    while count < n:
        count += 1
        if count % 3 == 0:
            continue

        print(count, end=" ")


code_6087()
