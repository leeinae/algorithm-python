# 카카오 블라인드 2018 뉴스 클러스터링

CONSTANT = 65536


def solution(str1, str2):
    str1_dic = dict()
    str2_dic = dict()

    if str1.upper() == str2.upper():
        return CONSTANT

    for i in range(len(str1) - 1):
        str = str1[i:i + 2].upper()

        if not str.isalpha(): continue
        if str in str1_dic:
            str1_dic[str] += 1
        else:
            str1_dic[str] = 1

    for i in range(len(str2) - 1):
        str = str2[i:i + 2].upper()

        if not str.isalpha(): continue
        if str in str2_dic:
            str2_dic[str] += 1
        else:
            str2_dic[str] = 1

    if len(str1_dic) == 0 or len(str2_dic) == 0: return 0

    inter_count = 0
    union_count = 0
    for i in str1_dic:
        for j in str2_dic:
            if i == j:
                inter_count += min(str1_dic[i], str2_dic[j])
                union_count += max(str1_dic[i], str2_dic[j])

    union_count = sum(str1_dic.values()) + sum(str2_dic.values()) - inter_count
    return int((inter_count / union_count) * CONSTANT)


solution("FRANCE", "french")
solution("handshake", "shake hands")
solution("aa1+aa2", "AAAA12")
solution("E=M*C^2", "e=m*c^2")
