# 프로그래머스 괄호 변환 (2020 kakao)
def algorithm(w):
    result = ''
    if w == '': return result
    if check_correct(w): return w

    left, right, pointer = 0, 0, 0
    for i in range(len(w)):
        if w[i] == "(":
            left += 1
        elif w[i] == ")":
            right += 1
        if left == right:
            pointer = i
            break

    u = w[:pointer + 1]
    v = w[pointer + 1:]

    recursive_v = algorithm(v)
    if check_correct(u):
        return u + recursive_v
    else:
        return "(" + recursive_v + ")" + reverse_paren(u[1:-1])


def reverse_paren(u):
    u = list(u)
    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('
    return "".join(u)


def check_correct(w):
    q = [w[0]]
    for i in range(1, len(w)):
        if w[i] == '(':
            q.append(w[i])
        else:
            if q and q[-1] == '(':
                q.pop()
    if len(q) == 0: return True
    return False


def solution(p):
    answer = algorithm(p)

    return answer


solution("(()())()")
solution(")(")
solution("()))((()")
