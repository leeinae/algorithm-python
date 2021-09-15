def add_num(total, num):
    global answer, n
    total += num
    if total > n:
        return
    elif total == n:
        answer += 1

    add_num(total, 1)
    add_num(total, 2)
    add_num(total, 3)


test_case = int(input())

for t in range(test_case):
    n = int(input())
    answer = 0
    add_num(0, 0)
    print(answer)
