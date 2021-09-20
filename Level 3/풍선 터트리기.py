def solution(a):
    answer = 2
    if len(a) <= 2:
        return len(a)
    c = len(a)
    num0 = a[0]
    ind0 = 0
    num1 = a[-1]
    ind1 = len(a) -1
    
    for i in range(c-2):
        if num0 <num1:
            if a[ind1 - 1] < num1:
                num1 = a[ind1 - 1]
                answer += 1
            ind1 -= 1
        else:
            if a[ind0 + 1] < num0:
                num0 = a[ind0 + 1]
                answer += 1
            ind0 += 1
    return answer

