from collections import deque


def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        # i개 만큼 자르기
        q = deque()
        for j in range(0, len(s), i):
            q.append(s[j:j + i])

        q.append("-")
        prev = q.popleft()
        final = ''
        num = 1
        while q:
            word = q.popleft()
            if prev == word:
                num += 1
            else:
                final += ('' if num == 1 else str(num)) + prev
                num = 1
            prev = word

        answer = min(answer, len(final))
    return answer


solution("aabbaccc")
solution("abcabcabcabcdededededede")
solution("a")
