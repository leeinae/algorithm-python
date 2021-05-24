# 카카오 블라인드 2018 뉴스 클러스터링

CONSTANTS = 65536


def solution(str1, str2):
    if str1.upper() == str2.upper():
        return CONSTANTS

    str1 = [str1[i:i + 2].upper() for i in range(0, len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2 = [str2[i:i + 2].upper() for i in range(0, len(str2) - 1) if str2[i:i + 2].isalpha()]

    inter = set(str1) & set(str2)
    union = set(str1) | set(str2)

    inter_count = sum([min(str1.count(i), str2.count(i)) for i in inter])
    union_count = sum([max(str1.count(i), str2.count(i)) for i in union])

    return int((inter_count / union_count) * CONSTANTS)


solution("FRANCE", "french")
solution("handshake", "shake hands")
solution("aa1+aa2", "AAAA12")
solution("E=M*C^2", "e=m*c^2")
