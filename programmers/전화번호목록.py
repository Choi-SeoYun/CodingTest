def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    
    for i, j in zip(phone_book[:-1], phone_book[1:]):
        if j.startswith(i):
            return False

    return answer