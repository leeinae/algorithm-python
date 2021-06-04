# 2019 kakao 오픈채팅방

def solution(record):
    answer = []
    user_dic = dict()
    printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}

    for r in record:
        args = r.split()
        command, user_id = args[0], args[1]
        if command == "Enter" or command == "Change":
            user_dic[user_id] = args[2]

    for r in record:
        args = r.split()
        command, user_id = args[0], args[1]
        if command == "Enter" or command == "Leave":
            answer.append(user_dic[user_id] + printer[command])

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
