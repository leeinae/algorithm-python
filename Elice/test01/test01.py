def calc_min_move_time(n, times):
    if n < 3:
        return times[n - 1]
    elif n == 3:
        return sum(times[:4])

    return calc_min_move_time(n - 2, times) + min(times[0] + (times[1] * 2) + times[n - 1],
                                                  (times[0] * 2) + times[n - 2] + times[n - 1])


def main():
    test_case = int(input())

    for case in range(test_case):
        n = int(input())
        times = list(map(int, input().split()))
        times.sort()

        time = calc_min_move_time(n, times)
        print(f'#{case + 1} {time}')


main()

'''
4
1
5
4
1 2 8 9
3
1 3 5
4
1 2 5 10
'''
