def solution(S):
    a_count = S.count('a')

    if a_count == 0:
        return (len(S) - 2) * (len(S) - 1) // 2
    if a_count % 3 != 0:
        return 0

    print("나머지", S, a_count)


solution("babaa")
solution("bbbbbb")
solution("aba")
solution("ababa")
