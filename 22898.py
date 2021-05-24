import re


def solution(code, day, data):
    answer = []
    data_dic = dict()

    for d in data:
        d = re.split("=| ", d)

        price = int(d[1])
        code = int(d[3])
        date = d[5]
        if code in data_dic:
            data_dic[code].append((price, date))
        else:
            data_dic[code] = [(price, date)]

    data_dic[code].sort(key=lambda x: x[1])
    for d in data_dic[code]:
        if d[1][:-2] == day:
            answer.append(d[0])

    print(answer)
    return answer


solution("987654", "20190620", ["price=80 code=987654 time=2019062013",
                                "price=90 code=987654 time=2019062014",
                                "price=120 code=987654 time=2019062018",
                                "price=110 code=987654 time=2019062009",
                                "price=95 code=987654 time=2019062111"])
