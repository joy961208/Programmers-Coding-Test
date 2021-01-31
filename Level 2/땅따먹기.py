def solution(land):
    answer = 0
    li = land[0]
    for i in land[1:]:
        li2 = i
        for j in range(4):
            if j == 0:
                li2[j] += max(li[1:])
            elif j == 3:
                li2[j] += max(li[0:3])
            else:
                li2[j] += max(max(li[j + 1:4]), max(li[0:j]))
        li = li2
    answer = max(li)
    return answer