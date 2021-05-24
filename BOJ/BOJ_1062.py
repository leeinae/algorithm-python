from itertools import combinations


def get_bitmask(word):
    temp = 0
    for w in word:
        temp |= 1 << (ord(w) - 97)
    return temp


def check(learn):
    count = 0
    for word in words:
        if (word & learn) != word:
            continue
        count += 1

    return count


n, k = map(int, input().split())
words = []  # 전체 단어
word_set = {'a', 'n', 't', 'i', 'c'}  # 전체 필요한 단어 set
answer = 0

for i in range(n):
    temp_word = list(input()[4:-4])
    word_set.update(temp_word)
    words.append(get_bitmask(temp_word))

if k < 5 or k == 26:
    print(0 if k < 5 else n)
    exit(0)

for i in combinations(word_set, k):
    if 'a' in i and 'n' in i and 't' in i and 'i' in i and 'c' in i:
        learn_word = get_bitmask(i)
        answer = max(check(learn_word), answer)

print(answer)
