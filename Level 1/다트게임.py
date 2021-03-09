def solution(dartResult):
    answer = 0
    num = [str(i) for i in range(0,11)]
    a = list(dartResult)
    li = []
    d = 0
    for i,j in enumerate(a[:-1]):
        if d == 1:
            d = 0
            continue
        if j + a[i+1] == '10':
           li.append(10)
           d = 1
        elif j in num:
            li.append(int(j))
        else:
            li.append(j)
    li.append(a[-1])
    ans = []
    for i in li:
        if type(i)== int:
            a = i
        elif i == "S":
            ans.append(a)
        elif i == "D":
            ans.append(a**2)
        elif i == "T":
            ans.append(a**3)
        elif i == "#":
            ans[-1] = -ans[-1]
        else:
            ans.append(i)
    li = []
    for j,i in enumerate(ans):
        if type(i) == int:
            li.append(i)
        else:
            li = [i*2 for i in li]
    if ans[-1] == "*":
        li[0] = li[0]//2

    return sum(li)

