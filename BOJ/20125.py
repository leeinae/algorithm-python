import sys

sys = sys.stdin.readline

n = int(sys())
cookies = [sys().strip() for _ in range(n)]

answer = []
heart_idx = (-1, -1)

# 머리 -> 심장 좌표
for i in range(len(cookies)):
    if '*' in cookies[i]:
        heart_idx = (i + 1, cookies[i].index('*') + 1)
        answer.append([heart_idx[0] + 1, heart_idx[1]])  # 심장 위치
        break

# 팔 길이
left_arm_len = (heart_idx[1] - 1) - cookies[heart_idx[0]].find('*')
right_arm_len = cookies[heart_idx[0]].rfind('*') - (heart_idx[1] - 1)
answer.append([left_arm_len, right_arm_len])

# 허리 길이
waist_len = 0
leg_idx = -1
for i in range(heart_idx[0] + 1, len(cookies)):
    if cookies[i].count('*') == 1:
        waist_len += 1
        leg_idx = i + 1
    else:
        break
answer[1].extend([waist_len])

# 다리 길이
left_leg_idx = cookies[leg_idx].find('*')
left_leg_len, right_leg_len = 0, 0
for i in range(leg_idx, len(cookies)):
    cookie_count = cookies[i].count('*')
    if cookie_count > 0:
        if cookie_count == 2:
            left_leg_len += 1
            right_leg_len += 1
        elif cookie_count == 1:
            left_leg_len += 1 if left_leg_idx == cookies[i].find('*') else 0
            right_leg_len += 1 if left_leg_idx + 2 == cookies[i].find('*') else 0
    else:
        break
answer[1].extend([left_leg_len, right_leg_len])

print(*answer[0])
print(*answer[1])
