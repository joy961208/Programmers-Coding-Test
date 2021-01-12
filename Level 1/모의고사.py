def solution(answers):
    answer = [1,2,3]
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    b1 = 0
    b2 = 0
    b3 = 0
    for i in range(len(answers)): #답의 배열길이 만큼 나머지를 구해서
        if a1[i%5] == answers[i]: #두개의 답을 비교해본다
            b1 += 1
        if a2[i%8] == answers[i]:
            b2 += 1
        if a3[i%10] == answers[i]:
            b3 += 1
    if b1<b2 or b1<b3:
        answer.remove(1)
    if b2<b1 or b2<b3:
        answer.remove(2)
    if b3<b1 or b3<b2:
        answer.remove(3)
    return answer
