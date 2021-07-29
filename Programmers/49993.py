from collections import deque


# for - else: for 중간에 break에 걸리는 것 없이 수행되었을 때 else 실행

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_q = deque(skill)
        for s in skills:
            if s in skill_q and s != skill_q.popleft():
                break
        else:
            answer += 1

    return answer


solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
