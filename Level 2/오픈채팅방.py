def solution(record):
    answer = []
    li = []
    change = {}
    for i in record:
        a = list(i.split())
        if a[0] == "Enter":
            li.append(a[0:2])
            change[a[1]] = a[2]
        elif a[0] == "Leave":
            li.append(a[0:2])
        elif a[0] == "Change":
            change[a[1]] = a[2]
    for i in li:
        if i[0] == "Enter":
            answer.append(change[i[1]] + "님이 들어왔습니다.")
        else:
            answer.append(change[i[1]] + "님이 나갔습니다.")

    return answer