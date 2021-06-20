def solution(S, C):
    answer = []
    employee = [s.split() for s in S.split(",")]
    email_dic = dict()

    C = C.lower()
    for e in employee:
        personal_email = (e[0] + "." + e[-1].replace("-", "")).lower()
        if personal_email in email_dic:
            email_dic[personal_email] += 1
            answer.append(f'{" ".join(e)} <{personal_email}{email_dic[personal_email]}@{C}.com>')
        else:
            email_dic[personal_email] = 1
            answer.append(f'{" ".join(e)} <{personal_email}@{C}.com>')

    print(", ".join(answer))
    return ", ".join(answer)


solution(
    "John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker",
    "Example")
