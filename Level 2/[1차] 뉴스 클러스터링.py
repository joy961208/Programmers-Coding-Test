def solution(str1, str2):
    s = "abcdefghijklmnopqrstuvwxyz"
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = []
    s2 = []
    for i,j in enumerate(str1[:-1]):
        if j in s and str1[i+1] in s:
            s1.append(j+str1[i + 1])

    for i,j in enumerate(str2[:-1]):
        if j in s and str2[i+1] in s:
            s2.append(j+str2[i + 1])
    b = 0
    a = 0
    s = set()
    s.update(s1)
    s.update(s2)
    for i in s:
        a += max(s1.count(i),s2.count(i))
        b += min(s1.count(i), s2.count(i))
    if a == 0 and b == 0:
        return 65536
    return int((b/a) * 65536)