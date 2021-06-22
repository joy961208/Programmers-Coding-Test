def solution(begin, target, words):
    answer = 0
    words.append(begin)

    if target not in words:
        return 0
    dic = {}
    
    for i in words:
        sub_li = []
        for j in words:
            c = 0
            for v,t in enumerate(j):
                if t == i[v]:
                    c+=1
            if c == len(i)-1:
                sub_li.append(j)
        dic[i] = sub_li

    li1 = [begin] #총경로
    li2 = [begin]

    while True:
        for i in dic:
            if i in li1:
                li2.extend(dic[i])
        answer += 1

        li1 = li2.copy()
        if target in li1:
            break

    return answer
