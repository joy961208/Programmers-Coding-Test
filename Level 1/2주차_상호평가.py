def solution(scores):
    answer = ""
    scores = list(map(list,zip(*scores)))
    for i, v in enumerate(scores):
        score = 0
        if max(v) == v[i] and v.count(v[i]) == 1:
            v.remove(v[i])
        elif min(v) == v[i] and v.count(v[i]) == 1:
            v.remove(v[i])
        scroe = sum(v)/ len(v)
        if -1 in v:
            v.remove(-1)
        score = sum(v)/ len(v)
        if score >= 90:
            answer += "A"
        elif score >=80:
            answer += "B"
        elif score >= 70:
            answer += "C"
        elif score >= 50:
            answer += "D"
        else:
            answer += "F"
    return answer
