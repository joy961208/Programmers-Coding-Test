def clock(time1,time2):
    time1 = list(time1.split(":"))
    time2 = list(time2.split(":"))
    a  = 0
    if int(time1[0]) < int(time2[0]):
        a = int(time2[0]) - int(time1[0])
    t1 = int(time1[1])
    t2 = int(time2[1])
    t2 += a*60
    return t2 - t1
def solution(m, musicinfos):
    answer = []
    m = list(m)
    for i in range(m.count("#")):
        a = m.index("#")
        m[a-1] = m[a-1] + "#"
        m.pop(a)
    for i in musicinfos:
        a = list(i.split(","))
        tt = clock(a[0],a[1])
        ans = []
        c = 0
        k = 0
        for i in range(tt):
            if c != len(a[3])-1:
                if a[3][c+1] == "#":
                    ans.append(a[3][c:c+2])
                    c+=2
                else:
                    ans.append(a[3][c])
                    c+=1
            else:
                ans.append(a[3][c])
                c+=1
            if c >= len(a[3]):
                c -= len(a[3])
        for ii,z in enumerate(ans):
            if z == m[0]:
                if ans[ii:len(m)+ii] == m:
                    answer.append([tt,k,a[2]])
                    k+=1
                    break
    if answer == []:
        return "(None)"
    else:
        answer.sort(key = lambda x: x[0],reverse=True)
        return answer[0][2]
