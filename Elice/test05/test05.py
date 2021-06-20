from itertools import combinations


def main():
    test_case = int(input())

    for case in range(1, test_case + 1):
        answer = int(1e9)

        n, k = map(int, input().split())
        positions = []

        for _ in range(n):
            positions.append(list(map(int, input().split())))

        comb = combinations(positions, k)
        for c in comb:
            if len(set([stone[2] for stone in c])) != k: continue

            max_x, max_y, min_x, min_y = 0, 0, int(1e9), int(1e9)
            for x, y, type in c:
                max_x = max(x, max_x)
                min_x = min(x, min_x)
                max_y = max(y, max_y)
                min_y = min(y, min_y)

            answer = min((max_x - min_x) * (max_y - min_y), answer)
        print(f'#{case} {answer}')


main()
