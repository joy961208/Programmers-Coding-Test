import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    a = len(scoville)
    for i in range(a):
        if scoville[0] > K:
            break
        elif len(scoville) == 1:
            return -1
        else:
            a1 = heapq.heappop(scoville)
            a2 = heapq.heappop(scoville)
            c = a1 + a2 *2
            heapq.heappush(scoville, c)
            answer += 1
    return answer