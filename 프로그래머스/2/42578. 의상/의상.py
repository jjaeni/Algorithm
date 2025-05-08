def solution(clothes):
    category_cnt = {}
    for name, category in clothes:
        category_cnt[category] = category_cnt.get(category, 0) + 1
    
    answer = 1
    for count in category_cnt.values():
        answer *= (count + 1)
    
    return answer-1