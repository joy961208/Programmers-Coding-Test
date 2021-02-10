def solution(tickets):
    answer = []
    dic = {}

    for i in tickets:
        if i[0] in dic:
            dic[i[0]].append(i[1])
            dic[i[0]] = sorted(dic[i[0]],reverse=True)
        else:
            dic[i[0]] = [i[1]]

    li1 = ["ICN"]
    li2 = []

    while li1:
        a = li1[-1]
        
        if a in dic :
            li1.append(dic[a].pop())
        else:
            li2.append(a)
            li1.pop()
        if a in dic and dic[a] == []:
            del(dic[a])

    li2.reverse()
    return li2