
def solution(priorities, location):
    answer = 0
    #목표의 타입을 int 에서 float로 변경
    priorities[location] = priorities[location]/1

    while len(priorities) != 0 :
        a = 0
        b = priorities[0]

        for i in priorities:
            if i> b:
                priorities.remove(b)
                priorities.append(b)
                a = 1
                break

        if a == 0:
            answer += 1
            priorities.remove(b)
            if type(b) == type(1.0):
                return answer

    return answer


def solution(priorities, location):
    answer = 0
    #목표의 타입을 int 에서 float로 변경
    priorities[location] = priorities[location]/1

    while priorities:
        b =  priorities.pop(0)

        if len(priorities) != 0 and b < max(priorities):
            priorities.append(b)
        else :
            answer += 1
            if type(b) == type(1.0):
                return answer

    return answer
