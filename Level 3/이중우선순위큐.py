def solution(operations):
    answer = []
    for i in operations:
        if "I" in i:
            a = list(i.split(" "))
            answer.append(int(a[1]))
        elif answer != [] and "D 1" in i:
            answer.remove(max(answer))
        elif answer != [] and "D -1" in i:
            answer.remove(min(answer))
    if answer == []:
        return [0,0]
    else:
        answer = [max(answer),min(answer)]
    return answer

