s = list(map(int, list(input())))
answer = 0

for i in range(len(s)):
    for j in range(i + 1, len(s), 2):
        sub = s[i:j + 1]
        mid = (j + 1 - i) // 2
        if sum(sub[:mid]) == sum(sub[mid:]):
            answer = max(answer, mid * 2)
print(answer)