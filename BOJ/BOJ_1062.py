from itertools import combinations


def check(learn):
    count = 0
    for word in words:
        flag = True
        read_word = 0
        for w in word:
            read_word |= 1 << (ord(w) - 97)
            if (read_word & learn) != read_word:
                flag = False
                break
        if flag:
            count += 1

    return count


n, k = map(int, input().split())
words = []  # 전체 단어
word_mask = 0  # 비트 마스킹
word_set = {'a', 'n', 't', 'i', 'c'}
answer = 0

for i in range(n):
    temp_word = list(input())
    words.append(temp_word)
    word_set.update(temp_word)
    for j in temp_word:
        word_mask |= 1 << (ord(j) - 97)

word_mask |= 1 << (ord('a') - 97)
word_mask |= 1 << (ord('n') - 97)
word_mask |= 1 << (ord('t') - 97)
word_mask |= 1 << (ord('i') - 97)
word_mask |= 1 << (ord('c') - 97)

if k < 5 or k == 26:
    print(0 if k < 5 else n)
    exit(0)

comb = combinations(word_set, k)
for i in comb:
    learn_word = 0
    for j in i:
        learn_word |= 1 << (ord(j) - 97)
        answer = max(check(learn_word), answer)

print(answer)
