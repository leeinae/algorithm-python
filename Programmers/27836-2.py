def valid_parentheses(prev, next):
    return (prev == "(" and next == ")") or (prev == "[" and next == "]") or (prev == "{" and next == "}")


def solution(s):
    stack = []
    for p in s:
        if stack and valid_parentheses(stack[-1], p):
            stack.pop()
        else:
            stack.append(p)

    return len(stack) == 0


solution("({})[]")
