def dfs(graph, start_node):
    
    visit = list()
    stack = list()
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

def solution(n, computers):
    answer = 0
    num = [i+1 for i in range(n)]
    li = {}
    
    for i,j in enumerate(computers):
        sub_li = []
        for v,t in enumerate(j):
            if t == 1:
                sub_li.append(v+1)
        li[i+1] = sub_li
        
    a = []
    for i in li:
        if i not in a:
            a.extend(dfs(li,i))
            answer += 1
    return answer


