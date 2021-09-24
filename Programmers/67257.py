import re
from itertools import permutations
from collections import deque


def calc(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '*':
        return n1 * n2
    elif op == '-':
        return n1 - n2


def solution(expression):
    answer = 0
    operation = re.findall(r'\*|-|\+', expression)
    expression = list(map(int, re.split(r"\D", expression)))

    for p in permutations(('+', '-', '*'), 3):
        _expression = expression
        _operation = operation
        for prior in p:
            num_q = deque([_expression[0]])
            oper_q = deque()

            for i in range(len(_operation)):
                num_q.append(_expression[i + 1])
                oper_q.append(_operation[i])

                if _operation[i] == prior:  # 계산해야하는 경우
                    num1 = num_q.pop()
                    num2 = num_q.pop()
                    op = oper_q.pop()

                    num_q.append(calc(num2, num1, op))
            _expression = num_q
            _operation = oper_q

            answer = max(answer, abs(num_q[0])) if len(num_q) == 1 else answer
    return answer


solution("50*6-3*2")
solution("100-200*300-500+20")
solution("2*2*2*2*2-2*2*2")
solution("200-300-500-600*40+500+500")
solution("2-990-5+2")
