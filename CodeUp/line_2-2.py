from collections import deque


def is_equals(origin, inp_str):
    return origin == inp_str


def is_valid_command(origin_type, input_type):
    if origin_type == "NUMBER" or origin_type == "NUMBERS":
        return input_type.isdigit()
    elif origin_type == "STRING" or origin_type == "STRINGS":
        return input_type.isalpha()


def solution(program, flag_rules, commands):
    answer = []
    rules_dict = dict(tuple(i.split(" ") for i in flag_rules))
    print(rules_dict)

    for command in commands:
        command = command.split(" -")

        # program
        if not is_equals(program, command[0]):
            answer.append(False)
            continue

        # flag
        for i in range(1, len(command)):
            result = True
            comm = deque(command[i].split(" "))

            flag = '-' + comm[0]
            print(flag)

            if flag in rules_dict:
                for j in range(1, len(comm)):
                    print(comm[j])
                    if rules_dict[flag] == "NULL":
                        continue

                    if not is_valid_command(rules_dict[flag], comm[j]):
                        result = False
                        break
            else:
                result = False
        answer.append(result)

    print(answer)
    return answer


# solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"])
# solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"])

solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"])
