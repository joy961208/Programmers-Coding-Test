def solution(genres, plays): # 각각의 장르에대한 고유번호와 점수를 사전을 통해 분류하여 계산
    answer = []
    a = {}
    
    for i in range(len(plays)):
        if genres[i] in a:
            a[genres[i]].append([plays[i], i])
            a[genres[i]][0] += plays[i]
        else:
            a[genres[i]] = [plays[i],[plays[i], i]]
    b = list(a.values())
    b.sort()
    b.reverse()
    
    for i in b:
        t = i[1:]
        t.sort()
        t.reverse()
        if len(t) == 1:
            answer.append(t[0][1])
        elif t[0][0] == t[1][0]:
            answer.append(t[1][1])
            answer.append(t[0][1])
        else :
            answer.append(t[0][1])
            answer.append(t[1][1])
    return answer
