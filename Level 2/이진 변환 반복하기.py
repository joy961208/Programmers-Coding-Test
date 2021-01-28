def change2(a):
    answer = []
    if a == 1:
        return [1]
    while a!=0:
        answer.append(a%2)
        a = a//2
    answer.reverse()
    return answer

def del_zero(li):
    c = li.count(0)
    return [i for i in li if i!=0], c

def solution(s):
    answer = []
    s = list(map(int,list(s)))
    count_zero = 0
    count_try = 0
    while len(s) != 1:
        s,c = del_zero(s)
        s =change2(len(s))
        count_zero += c
        count_try += 1
    return [count_try,count_zero]