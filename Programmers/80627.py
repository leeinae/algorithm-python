def solution(s):
    q = []
    for c in s:
        try:
            if q[-1] == c:
                q.pop()
            else:
                q.append(c)
        except:
            q.append(c)

    return 0 if len(q) > 0 else 1
