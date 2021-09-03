def solution(genres, plays):
    answer = []
    top_genres = dict()
    music_dict = dict()

    for i in range(len(genres)):
        if genres[i] in music_dict:
            top_genres[genres[i]] += plays[i]
            music_dict[genres[i]].append((plays[i], i))
        else:
            top_genres[genres[i]] = plays[i]
            music_dict[genres[i]] = [(plays[i], i)]

    top_genres = sorted(top_genres.items(), key=lambda x: x[1])

    for i in music_dict.values():
        i.sort(key=lambda x: (x[0], -x[1]))
    print(music_dict, top_genres)

    while top_genres:
        genre, score = top_genres.pop()
        answer.extend([i[1] for i in music_dict[genre][:-3:-1]])

    return answer


solution(["classic", "pop", "classic", "classic", "pop", "classic"], [500, 600, 150, 800, 2500, 500])
