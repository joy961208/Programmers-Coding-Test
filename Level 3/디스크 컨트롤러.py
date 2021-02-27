import heapq
def solution(jobs):
    t = len(jobs)
    a = []
    jobs.sort(reverse = True)
    
    for i in jobs:
        i.reverse()
        a.append(i)
        
    jobs = a
    answer = jobs[-1][1]
    ans = 0 #대기시간 + 실행시간계산
    wait = []
    while jobs:
        if jobs[-1][1] <= answer:
            heapq.heappush(wait, jobs.pop())
            continue
        elif wait == []:
            answer = jobs[-1][1]
        else :
            a = heapq.heappop(wait)
            answer += a[0]
            ans += answer - a[1]

    while wait:
        a  = heapq.heappop(wait)
        answer += a[0]
        ans += answer - a[1]
    return ans//t