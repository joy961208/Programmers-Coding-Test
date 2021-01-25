def solution(n, m):
    answer = []
    a = 1
    for i in range(1,min(n,m)+1):
        if m%i == 0 and n%i == 0:
            a = i
    answer.append(a)
    a = min(n,m)
    while True:
        if a%n == 0 and a%m == 0:
            answer.append(a)
            break
        a+=1
    return answer