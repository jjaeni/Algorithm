'''completion 길이가 participant 길이보다 1이 작음으로써 완주하지 못한 선수가 없는 경우는 X'''
from collections import Counter

def solution(participant, completion):
    return list((Counter(participant)-Counter(completion)).keys())[0]