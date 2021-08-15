def solution(monster, S1, S2, S3):
    answer, total = 0, 0
    s1 = [_ for _ in range(1, S1 + 1)]
    s2 = [_ for _ in range(1, S2 + 1)]
    s3 = [_ for _ in range(1, S3 + 1)]

    for i in s1:
        for j in s2:
            for z in s3:
                total += 1
                if i + j + z + 1 not in monster:
                    answer += 1
    return int((answer / total) * 1000)


solution([4, 9, 5, 8], 2, 3, 4)
solution([4, 9, 5, 8], 2, 3, 3)
