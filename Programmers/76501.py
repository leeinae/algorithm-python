# 프로그래머스 음양 더하기

def solution(absolutes, signs):
    signs = list(map(lambda x: x if int(x) > 0 else -1, signs))
    return sum([signs[i] * absolutes[i] for i in range(len(signs))])


r = solution([4, 7, 12], [True, False, True])
print(r)
