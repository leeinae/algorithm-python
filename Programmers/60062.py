from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    weak_length = len(weak)
    weak.extend(list(map(lambda x: x + n, weak)))

    for i in range(weak_length):
        point = [weak[_] for _ in range(i, i + weak_length)]
        for p in permutations(dist, len(dist)):
            friend_idx, friend_count = 0, 1  # 친구 인덱스, 사용 친구 횟수
            possible_dist = point[0] + p[0]  # 첫 번쨰 결점에서 출발해서 가능한 길이

            for idx in range(weak_length):
                if possible_dist < point[idx]:
                    friend_count += 1

                    if friend_count > len(dist): break
                    friend_idx += 1
                    possible_dist = point[idx] + p[friend_idx]
            answer = min(answer, friend_count)

    if answer == len(dist) + 1: return -1
    return answer


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
solution(12, [1, 3, 4, 9, 10], [3, 5, 7])
