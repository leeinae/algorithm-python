# import itertools
# from collections import Counter

# 문자열 정렬
# 문자열 s, 자연수 n
# def solution():
#     n, s = input().strip().split('')
#
#     print(s.rjust(n))
#     print(s.ljust(n))
#     print(s.center(n))

# 배열 뒤집기
# def solution(mylist):
#     answer = [[], [], []]
#     print(answer)
#     for i in range(len(mylist)):
#         for j in range(len(mylist[i])):
#             answer[i].append(mylist[j][i])
#     return answer
#
# print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 배열 i, i-1 접근
# zip(): 서로 다른 길이의 list가 인자로 들어올 경우는 길이가 짧은 list까지만 이터레이션
# def solution(mylist):
#     answer = []
#     for num1, num2 in zip(mylist, mylist[1:]):
#         answer.append(abs(num1 - num2))
#     print(answer)
#
# solution([83, 48, 13, 4, 71, 11])

# 문자열 리스트 -> 정수형 리스트 반환
# map(func,elem): 리스트의 요소를 지정된 함수로 처리
# def solution(mylist):
#     answer = list(map(int, mylist))
#     return answer
#
# solution(['1', '100', '33'])

# 리스트 요소 갯수 리턴
# def solution(mylist):
#     answer = list(map(len, mylist))
#     print(answer)
#
# solution([[1, 2], [3, 4], [5]])

# 문자열 리스트 -> 문자열 리턴
# def solution(mylist):
#     answer = ''.join(mylist)
#     return answer

# product 함수
# 데카르트 곱, 두 개 이상의 리스트의 모든 조합을 구함
# def solution():
#     list1 = 'abcd'
#     list2 = '1234'
#
#     print(list(itertools.product(list1, list2)))

# collections 모듈
# def solution():
#     portfolio = [
#         ('GOOG', 100, 490.1),
#         ('IBM', 50, 91.1),
#         ('CAT', 150, 83.44),
#         ('IBM', 100, 45.23),
#         ('GOOG', 75, 572.45),
#         ('AA', 50, 23.15)
#     ]
#
#     total_shares = Counter()
#
#     for name, share, price in portfolio:
#         total_shares[name] += share
#     print(total_shares)
#
# solution()

# 자연수 5개의 곱이 제곱수일때 - found, 아닐 때 - not found
# for-else: for문이 break 등으로 끊기지 않고 끝까지 수행되었을 때 수행. (flag가 필요없음)

# import math
#
# numbers = [int(input()) for i in range(5)]
#
# total = 1
# for i in numbers:
#     total *= i
#     if (math.sqrt(total) == int(math.sqrt(total))):
#         print("found")
#         break;
# else:
#     print("not found")
