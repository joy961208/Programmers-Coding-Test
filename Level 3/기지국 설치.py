def solution(n, stations, w):
    answer = 0
    b = []
    a = 1

    for i in stations:
        if i - w > 1:
            b.append((i-w) - a)
        a = i+w
    if a != n:
        b.append(n-a)
        
    print(b)
    for i in b:
        answer += int(i/(w*2 + 1) )
        prin

    return answer
