def solution(routes):
    answer = 1
    first = routes[0][0]
    second = routes[0][1]

    for i in routes[1:]:
        if first <=  i[0] and second >= i[1]:
            first,second = i[0] ,i[1]
        elif first <= i[0]:
            first = i[0]
        elif second >= i[1]:
            second = i[1]
        else :
            first = i[0]
            second = i[1]
            answer +=1
        if first > second:
            first = i[0]
            second = i[1]
            answer += 1
    return answer