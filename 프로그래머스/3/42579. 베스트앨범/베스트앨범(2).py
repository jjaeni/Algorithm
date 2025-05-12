# code review
from collections import defaultdict

def solution(genres, plays):
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] += play
        genre_songs[genre].append([play, i])
    
    # 재생수 내림차순
    sorted_genres = sorted(genre_total, key=genre_total.get, reverse=True)
    
    # 베스트 앨범 구성
    result = []
    for genre in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        result.extend([i for _, i in sorted_songs[:2]])
        
    return result
