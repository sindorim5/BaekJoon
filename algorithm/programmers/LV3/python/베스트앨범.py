from collections import defaultdict


def solution(genres, plays):
    answer = []

    genre_dict = defaultdict(int)
    index_dict = defaultdict(list)

    for i in range(len(genres)):
        genre_dict[genres[i]] += plays[i]
        index_dict[genres[i]].append((i, plays[i]))

    sorted_genre_dict = sorted(
        genre_dict.items(), key=lambda x: x[1], reverse=True)

    for key, value in sorted_genre_dict:
        sorted_index_dict = sorted(
            index_dict[key], key=lambda x: x[1], reverse=True)[:2]
        for index, play in sorted_index_dict:
            answer.append(index)

    return answer
