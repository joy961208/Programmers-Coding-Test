def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in phone_book:
        for j in phone_book:
            if i == j:
                continue
            if i == j[0:len(i)]:
                return False

    return answer
