def solution(phone_book):
    phone_book.sort() # 사전순 정렬
    
    for i in range(len(phone_book)-1):
        # 현재 번호가 다음 번호의 접두사인지 확인
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True