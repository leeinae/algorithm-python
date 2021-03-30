def rotate_array(array):
    new_array = [[0] * len(array) for _ in range(len(array[0]))]

    for i in range(len(array)):
        for j in range(len(array[0])):
            new_array[j][len(array) - 1 - i] = array[i][j]

    return new_array


def check_array(new_lock):
    len_lock = len(new_lock) // 3

    for i in range(len_lock, len_lock * 2):
        for j in range(len_lock, len_lock * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotate in range(4):
        key = rotate_array(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check_array(new_lock):
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
print(result)

# rotate_array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
