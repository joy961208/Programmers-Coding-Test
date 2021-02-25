def solution(s):
    li = []

    for i in s:
        if li == []:
            li.append(i)
        elif li[-1] == i:
            li.pop()
        else:
            li.append(i)

    if li == []:
        return 1
    else:
        return 0