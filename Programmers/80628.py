from collections import deque


def solution(s):
    answer = []
    s = deque(s[s.index(max(s)):])

    for c in s:
        while answer and answer[-1] < c:
            answer.pop()
        answer.append(c)

    return "".join(answer)


solution("xyb")
solution("yxyc")
solution("abcd")
solution("aaddc")
