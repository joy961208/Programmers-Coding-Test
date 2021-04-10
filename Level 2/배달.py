from math import inf
def solution(N, road, K):
    answer = 0
    dic1 = {}
    dic2 = {}
    
    for i in range(1,N+1):
        a = {}
        dic2[i] = inf
        for j in road:
            if j[0] == i:
                a[j[1]] = j[2]
            elif j[1] == i:
                a[j[0]] = j[2]
        dic1[i] = a

    return answer
