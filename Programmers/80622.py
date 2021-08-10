def check_lock(array):
    length = len(array) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            print(i, j)
            if array[i][j] != 1: return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] += lock[i][j]

    rotate_key = key
    for _ in range(4):
        rotate_key = list(zip(*rotate_key[::-1]))

        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += rotate_key[i][j]

                if check_lock(new_lock): return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= rotate_key[i][j]

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
