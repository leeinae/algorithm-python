import sys

sys = sys.stdin.readline

n, k = map(int, sys().split())
seq = list(map(int, sys().split()))
multitap = []
answer = 0

for i in range(k):
    if seq[i] in multitap:
        continue

    if len(multitap) < n:
        multitap.append(seq[i])
        continue
    else:
        idxs = []
        flag = True
        for m in multitap:
            if m in seq[i:]:
                multitap_idx = seq[i:].index(m)
            else: # 안 쓰일 코드
                multitap_idx = 101
                flag = False
            idxs.append(multitap_idx)

            if not flag:
                break
        remove_idx = idxs.index(max(idxs))
        del multitap[remove_idx]
        multitap.append(seq[i])
        answer += 1

print(answer)
