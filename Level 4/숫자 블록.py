import math

def prime(a):
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i == 0:
            if a//i > 10000000:
                continue
            else:
                return a//i
    return 1

def solution(begin, end):
    answer = []

    for i in range(begin,end+1):
        if i == 1:
            answer.append(0)
        a = prime(i)
        answer.append(a)
    return answer
