def solution(name):
    answer = 0
    name = list(name)
    Al1 = "ABCDEFGHIJKLMN"
    Al2 = "AZYXWVUTSRQPO"
    AA = "A" * len(name)

    for i in name:
        if i in Al1:
            answer += Al1.index(i)
        else:
            answer += Al2.index(i)
    ind = 0

    while True :
        name[ind] = "A"
        if name == list(AA):
            break
        a , b = 1 , 1
        while name[ind - a] == "A":
            a += 1
        while name[ind + b] == "A":
            b += 1
        answer += min(a,b)
        ind += -a if a<b else b

    return answer