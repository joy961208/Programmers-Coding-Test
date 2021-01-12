def change2(n):
    a = n
    b = []
    while True:
        b.append(a%3)
        a = a//3
        if a == 0:
            break
    b.reverse()
    return b

def solution(n):
    answer = ''
    b = change2(n)
    while 0 in b:
        print(b)
        index0 = b.index(0)
        if index0 == 0:
            b.remove(0)
            continue
        b[index0] = 4
        if b[index0 - 1] == 4:
            b[index0 -1] = 2
        else:
            b[index0 -1] -= 1
        print(b)
    for i in b:
        answer += str(i)
    return answer

