from collections import deque


def printLock(lock):
    for i in range(len(lock)):
        print(lock[i])


# def bfs(row, col):
#     q = deque([row])
#     click = [0 for _ in range(k)]
#
#     while q:
#         t_row = q.popleft()
#         visited[t_row][col] = True
#
#         for i in range(2):
#             n_row = t_row + direction[i]
#             if n_row == k:
#                 n_row = 0
#             elif n_row < 0:
#                 n_row = k - 1
#
#             if visited[n_row][col]: continue
#
#             q.append(n_row)
#             visited[n_row][col] = True
#             click[n_row] = click[t_row] + 1
#             if lock[n_row][col] == 1: return click[n_row]


# def main():
#     test_case = int(input())
#
#     for case in range(test_case):
#         global lock, visited, direction, n, k
#
#         n, k = map(int, input().split())  # n개의 링, k개의 칸
#         lock = [list(map(int, input())) for _ in range(k)]
#         direction = [-1, 1]
#         answer = int(1e9)
#
#         for row in range(k):
#             total = 0
#             for col in range(n):
#                 visited = [[False] * n for _ in range(k)]
#                 if lock[row][col] == 1 or visited[row][col]: continue
#
#                 result = bfs(row, col)
#                 total += result
#             answer = min(total, answer)
#
#         print(f'#{case + 1} {answer}')

def main():
    test_case = int(input())

    for case in range(test_case):
        n, k = map(int, input().split())  # n개의 링, k개의 칸
        lock = [list(map(int, input())) for _ in range(k)]
        key_count = [sum(l) for l in lock]

        for col in range(n):
            for row in range(k):
                prev_idx = row - 1 if row - 1 >= 0 else k - 1
                next_idx = row + 1 if row + 1 != k else 0

                lock[prev_idx][col] = lock[row][col] + 1 if lock[prev_idx][col] == 0 else min(lock[row][col] + 1,
                                                                                              lock[prev_idx][col])
                lock[next_idx][col] = lock[row][col] + 1 if lock[next_idx][col] == 0 else min(lock[row][col] + 1,
                                                                                              lock[next_idx][col])

        print(lock)


main()

'''
3
5 4
01000
00110
10001
11111
5 4
01000
00110
10001
01001
5 4
01000
00110
10001
01111
'''
