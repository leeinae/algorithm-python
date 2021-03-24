string = input()

count_0 = 0  # 0으로 만드는 방법 카운트
count_1 = 0

before = int(string[0])
if before == 1:
    count_0 += 1
else:
    count_1 += 1

for i in string[1:]:
    if int(i) == before:
        continue

    if int(i) == 1:
        count_0 += 1
    else:
        count_1 += 1

    before = int(i)

print(min(count_1, count_0))
