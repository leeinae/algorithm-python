def calc_score(s, sentence):
    return sentence.count(s)


def solution(scores):
    answer = 0

    for score in scores:
        a_count = calc_score("A", score)
        f_count = calc_score("F", score)
        if f_count >= 2:
            continue
        elif a_count >= 2:
            answer += 1
            continue

        sentence = sorted(score)[1:-1]
        avg = sum(map(lambda x: 70 - ord(x), sentence)) / len(sentence)

        if avg >= 3:
            answer += 1
    return answer


solution(["AAFAFA", "FEECAA", "FABBCB", "CBEDEE", "CCCCCC"])
solution(["BCD", "ABB", "FEE"])
