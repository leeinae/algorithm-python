def solution(clothes):
    answer = 1
    clothes_dict = dict()
    for name, type in clothes:
        if type in clothes_dict:
            clothes_dict[type].append(name)
        else:
            clothes_dict[type] = [name]

    for i in clothes_dict.values():
        answer *= len(i) + 1
    return answer - 1


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
