import heapq

def solution(n, edge):
    answer = 0
    dic = {}

    for i in edge:
        p1 = i[0]
        p2 = i[1]
        l = 1
        if p1 not in dic.keys():
            dic[p1] = {p2:l}
        if p2 not in dic.keys():
            dic[p2] = {p1:l}
        if p1 in dic.keys():
            if p2 in dic[p1].keys() and dic[p1][p2] > l: 
                dic[p1][p2] = l
            elif p2 not in dic[p1].keys():
                dic[p1][p2] = l
        if p2 in dic.keys():
            if p1 in dic[p2].keys() and dic[p2][p1] > l: 
                dic[p2][p1] = l
            elif p1 not in dic[p2].keys():
                dic[p2][p1] = l
    first = 1
    distance = {node:float('inf') for node in range(1,n+1)}
    distance[first] = 0  
    queue = []
    heapq.heappush(queue, [distance[first], first])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distance[current_node] < current_distance: 
            continue

        for next_node, weight in dic[current_node].items():
            total_distance = current_distance + weight

            if total_distance < distance[next_node]:
                distance[next_node] = total_distance
                heapq.heappush(queue, [total_distance, next_node])
    
    return list(distance.values()).count(max(distance.values()))
