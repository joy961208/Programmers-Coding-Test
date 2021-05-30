import math
def ss(a):
    li = []
    b = a
    c = 2
    dic = {}
    
    for i in range(int(math.sqrt(b))+1):
        if a%c == 0:
            a = a//c
            li.append(c)
            c -= 1
        c += 1
    li.append(a)
    for i in li:
        dic[i] = li.count(i)
    return dic

def solution(arr):
    answer = 1
    dic ={}
    for i in arr:
        d = ss(i)
        for j in d:
            if j in dic and dic[j] <d[j]:
                dic[j] = d[j]
            elif j not in dic:
                dic[j] = d[j]
    for i in dic:
        answer *= i**dic[i]
    return answer
