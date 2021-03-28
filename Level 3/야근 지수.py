import heapq
def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    heap = []
    for i in works:
        heapq.heappush(heap,(-i,i))
    for i in range(n):
        a = heapq.heappop(heap)[1]
        heapq.heappush(heap,(-(a-1),a-1))
    for i in heap:
        answer += i[1]**2
    return answer
