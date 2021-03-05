def solution(n, words):
    words_li = []
    words.reverse()
    t = 0
    words_li.append(words.pop())
    le = len(words)

    for i in range(le):
        a = words.pop()
        if words_li[-1][-1] != a[0]:
            t = 1
            words_li.append(a)
            break
        if a in words_li:
            t = 1
            words_li.append(a)
            break
        else:
            words_li.append(a)
    if t == 0:
        return [0,0]
    else:
        a = len(words_li)%n
        b = (len(words_li)//n) + 1
        if a == 0:
            a = n
            b = len(words_li)//n

        return [a,b]
    return [a,b]