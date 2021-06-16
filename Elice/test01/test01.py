def calc_min_move_time(n, times):
    if n <= 2:
        return times[n - 1]
    elif n == 3:
        return sum(times[:4])

    return calc_min_move_time(n - 2, times) + min(times[0] + (times[1] * 2) + times[n - 1],
                                                  (times[0] * 2) + times[n - 2] + times[n - 1])


def main():
    f = open('sample_input.txt', 'r')
    test_case = int(f.readline())
    input_lines = f.readlines()

    case_num = 1
    while case_num <= test_case:
        args = 2 * (case_num - 1)
        n = int(input_lines[args])
        times = list(map(int, input_lines[args + 1].split()))
        times.sort()

        time = calc_min_move_time(n, times)
        print(f'#{case_num} {time}')

        case_num += 1

    f.close()


main()
