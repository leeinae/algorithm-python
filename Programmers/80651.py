def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False


def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i:j]):
                answer = max(answer, len(s[i:j]))

    return answer


solution("abcdcba")
solution("abacde")
solution("a")
