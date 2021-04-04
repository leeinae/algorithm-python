from itertools import combinations
import sys


def check(learn_word):
    count = 0
    for word in words:
        flag = True
        for w in word:
            if w not in learn_word:
                flag = False
                break

        if flag:
            count += 1

    return count


n, k = map(int, input().split())
words = []
word_set = {'a', 'n', 't', 'i', 'c'}
answer = 0

for i in range(n):
    temp_word = list(input()[4:-4])
    words.append(temp_word)
    word_set.update(temp_word)

if k < 5:
    print(0)
    sys.exit()
elif k == 26:
    print(n)
    sys.exit()

comb = combinations(word_set, k)
for i in comb:
    answer = max(check(i), answer)

print(answer)
