'''result: 폰켓몬 종류의 최대 개수'''
from collections import Counter

def solution(nums):
    n = len(list(Counter(nums).keys()))
    
    if len(nums)/2 <= n:
        result = len(nums)/2
    else:
        result = n
    return result