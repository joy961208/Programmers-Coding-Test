def solution(routes):
    answer = 1
    routes.sort()
    a = routes[0]

    for i in routes[1:]:

        if a[0] <= i[0]:
            a[0] = i[0]

        if a[1] >= i[1]:
            a[1] = i[1]

        if a[0] > a[1]:
            answer += 1
            a = i
    return answer
