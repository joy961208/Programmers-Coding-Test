def solution(s):
    answer = ''
    a = list(s)
    c = 0
    for i in a:
        if i==' ':
            answer += i
            c = 0
        else :
            if c%2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            c+=1

    return answer