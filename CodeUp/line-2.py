import re


def check_first(inp_str):
    if 8 <= len(inp_str) <= 15:
        return True
    else:
        return False


def check_second(inp_str):
    inp_str = re.sub("~!@#$%^&*", "", inp_str)
    if inp_str.isalnum():
        return True
    else:
        return False


def check_third(inp_str):
    count = 0
    if re.match('[a-z]+', inp_str):
        count += 1
    if re.match('[A-Z]+', inp_str):
        count += 1
    if re.match('[0-9]+', inp_str):
        count += 1
    if re.match('[~!@#$%^&*]+', inp_str):
        count += 1

    if count >= 3:
        return True
    else:
        return False

def check_fourth(inp_str):
    max


def solution(inp_str):
    answer = []

    if not check_first(inp_str):
        answer.append(1)

    if not check_second(inp_str):
        answer.append(2)

    if not check_third(inp_str):
        answer.append(3)

    print(answer)
    return answer

solution("aaaaZZZZ)")