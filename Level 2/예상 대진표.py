def solution(n,a,b):
    answer = 1

    while True:
        if a%2 == 1 and a+1 == b :
            break
        elif b%2 == 1 and b+1 == a:
            break
        if a%2 == 1:
            a+=1
        if b%2 == 1:
            b+=1
        a = a//2
        b = b//2
        answer += 1
    return answer