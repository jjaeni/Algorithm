# gpt ver.
from collections import defaultdict

def solution(genres, plays):
    genre_to_total = defaultdict(int)
    genre_to_songs = defaultdict(list)

    # 1. 정보 수집
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_to_total[genre] += play
        genre_to_songs[genre].append((play, i))  # (재생 수, 고유 번호)

    # 2. 장르 정렬 (총 재생 수 내림차순)
    sorted_genres = sorted(genre_to_total, key=genre_to_total.get, reverse=True)

    result = []

    for genre in sorted_genres:
        # 3. 장르 내 노래 정렬 (재생 수 내림차순, 고유번호 오름차순)
        songs = sorted(genre_to_songs[genre], key=lambda x: (-x[0], x[1]))
        # 4. 최대 2곡 선택
        result.extend([idx for _, idx in songs[:2]])

    return result
