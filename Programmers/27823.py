from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)

    p_dict, c_dict = dict(), dict()
    for p in participant:
        if p in p_dict:
            p_dict[p] += 1
        else:
            p_dict[p] = 1

    for c in completion:
        if c in c_dict:
            c_dict[c] += 1
        else:
            c_dict[c] = 1

    return list(answer.keys())[0]


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
