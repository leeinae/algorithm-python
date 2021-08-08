# 프로그래머스 방문길이, 소요시간 2시간 ... ㅠ

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def valid_position(x, y):
    return -5 <= x <= 5 and -5 <= y <= 5


def solution(dirs):
    answer = 0
    visited = set()
    dir_dict = {'U': 0, 'D': 1, 'R': 2, 'L': 3}

    position = (0, 0)  # 현재 좌표 / 5,5에서 시작
    for command in dirs:
        nd = dir_dict[command]  # 새로운 방향
        nx, ny = direction[nd][0] + position[0], direction[nd][1] + position[1]

        if valid_position(nx, ny):
            if (position[0], position[1], nx, ny) not in visited:
                visited.add((nx, ny, position[0], position[1]))
                visited.add((position[0], position[1], nx, ny))
                answer += 1
            position = (nx, ny)

    return answer


solution("ULURRDLLU")
solution("LULLLLLLU")
