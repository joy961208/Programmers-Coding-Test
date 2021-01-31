def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    r = [rocks[0]]
    for i,j in enumerate(rocks[1:]):
        r.append(j - rocks[i])
    for i in range(n):
        ind = r.index(min(r))
        if ind == 0:
            a = r[0] + r[1]
            del r[0:2]
            r.insert(0,a)
        elif ind == len(r)-1:
            a = r[-2] + r[-1]
            del r[-2:]
            r.append(a)
        else :
            if r[ind+1] >= r[ind-1]:
                a = r[ind-1] + r[ind]
                del r[ind-1:ind+1]
                r.insert(ind-1,a)
            else:
                a = r[ind + 1] + r[ind]
                del r[ind:ind + 2]
                r.insert(ind , a)

    return min(r)