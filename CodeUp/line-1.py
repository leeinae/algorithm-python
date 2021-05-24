def solution(table, languages, preference):
    answer = ''

    score = []
    result = [0] * 5
    for i in range(5):
        score.append(list(map(str, table[i].split())))

    score.sort()
    for i in range(5):
        for j in range(len(languages)):
            if languages[j] not in score[i]: continue
            result[i] += (6 - score[i].index(languages[j])) * preference[j]

    print(score[result.index(max(result))][0])
    return answer


solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
          "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5])
solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
          "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5])
