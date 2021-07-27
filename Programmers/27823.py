def solution(participant, completion):
    for c in completion:
        if c in participant:
            participant.remove(c)

    print(participant[0])
    return participant[0]


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
