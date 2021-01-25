def solution(num):
    answer = 0
    n = num
    while n != 1:
        if n%2 == 0:
            n = n//2
            answer += 1
        else:
            n = (n*3)+1
            answer += 1
        if answer == 500:
            return -1
    return answer