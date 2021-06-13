def solution(n, arr1, arr2):
    result = [bin(arr1[i] | arr2[i]).replace("0b", "0" * n)[-n:] for i in range(len(arr1))]
    result = [num.replace('1', '#') for num in result]
    result = [num.replace('0', ' ') for num in result]
    return result


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
