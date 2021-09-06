from itertools import combinations


def solution(orders, course):
    answer = []
    orders = [list(i) for i in orders]

    for i in course:
        menu_dict = dict()
        for order in orders:
            for c in combinations(order, i):
                c = sorted(c)
                menu = "".join(c)
                if menu in menu_dict:
                    menu_dict[menu] += 1
                else:
                    menu_dict[menu] = 1

        for key, val in menu_dict.items():
            max_count = max(menu_dict.values())
            if 2 <= max_count == val:
                answer.append(key)

    answer.sort()
    return answer


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
