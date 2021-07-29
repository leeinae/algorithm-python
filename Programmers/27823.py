from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)

    return list(answer.keys())[0]


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
