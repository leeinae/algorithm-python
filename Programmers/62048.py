'''
프로그래머스 멀쩡한 사각형

최대공약수 - 유클리드 호제법
두 수를 나눈 수와 나머지로 MOD 연산을 계속함 (나누는 수 가 0이 될 때까지)

LCM (least common multiple)도 최대공약수로 구할 수 있다
X = AB, Y = BC일 때 최대공약수는 B니까
최소공배수는 (X * Y) // gcd(X, Y) 라고 할 수 있지
'''


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def solution(w, h):
    g = gcd(w, h)
    return (w * h) - (w + h - g)


solution(8, 12)
