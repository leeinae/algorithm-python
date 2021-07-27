def solution(s):
    s = list(s)
    q = []

    for _ in s:
        if len(q) > 0 and _ == ')' and q[-1] == '(':
            q.pop()
        else:
            q.append(_)

    return len(q) == 0


solution("()()")
solution("(())()")
solution("((())")

solution("(())()")
solution(")()(")
