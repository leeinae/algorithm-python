from collections import deque


def is_equals(origin, inp_str):
    return origin == inp_str


def is_valid_command(origin_type, input_type):
    if origin_type == "NUMBER":
        return input_type.isdigit()
    elif origin_type == "STRING":
        return input_type.isalpha()


def solution(program, flag_rules, commands):
    answer = []
    rules_dict = dict(tuple(i.split(" ") for i in flag_rules))

    for command in commands:
        comm = deque(command.split(" "))

        # program
        if not is_equals(program, comm.popleft()):
            answer.append(False)
            continue

        while comm:
            result = True
            flag = comm.popleft()

            if flag in rules_dict:
                if rules_dict[flag] == "NULL":
                    continue

                if not is_valid_command(rules_dict[flag], comm.popleft()):
                    result = False
                    break
            else:
                result = False
        answer.append(result)

    return answer


solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"])
solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"])