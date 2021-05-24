import heapq


def solution(t, r):
    answer = []
    client = []

    for c in range(len(t)):
        client.append([t[c], c])  # 시간, id
    client.sort()
    print(client)

    while True:
        temp = [client[0]]
        for i in range(1, len(client)):
            if client[i][0] == temp[0]:
                temp.append(client[i])
            else:
                break
        print(temp)


    print("a", answer)
    return answer


solution([0, 1, 3, 0], [0, 1, 2, 3])
# solution([7, 6, 8, 1], [0, 1, 2, 3])
