import re


def solution(new_id):
    answer = ''

    # 1 + 2
    answer = re.sub('[^a-z0-9\-\_\.]', '', new_id.lower())

    # 3
    answer = re.sub('\.\.+', '.', answer)

    # 4
    answer = re.sub('^\.|\.$', '', answer)

    # 5
    answer = 'a' if answer == '' else answer

    # 6
    answer = re.sub('\.$', '', answer[0:15])

    # 7
    while len(answer) < 3:
        answer += answer[-1:]

    return answer
