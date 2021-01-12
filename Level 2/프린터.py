def solution(priorities, location):
    answer = 0
    priorities[location] = priorities[location]/1
    t = 0
    while len(priorities) != 0 and t == 0:
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
