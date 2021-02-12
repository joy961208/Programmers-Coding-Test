def find(n,gp):
    if n != gp[n]:
        gp[n] = find(gp[n],gp)
    return gp[n]

def union(a,b,gp):
    r1 = find(a,gp)
    r2 = find(b,gp)
    gp[max(r1,r2)] = min(r1,r2)
    return gp

def solution(n, costs):
    answer = 0
    gp = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])
    for i in costs:
        if find(i[0], gp) != find(i[1], gp):
            gp = union(i[0],i[1],gp)
            answer += i[2]

    return answer