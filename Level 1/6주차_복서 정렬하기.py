def solution(weights, head2head):
    answer = []
    num_dic = {}
    for i,j in enumerate(weights):
        num_dic[i+1] = []
        win_lose = head2head[i]
        lose = win_lose.count('L')
        win = win_lose.count('W')
        if lose == 0 and win == 0:
            winpersent = 0
        else :
            winpersent = win/(lose+win)
        num_dic[i+1].append(winpersent)
        heavy_win = 0
        for ind, w in enumerate(win_lose):
            if w == "W" and weights[i] < weights[ind]:
                heavy_win += 1
        num_dic[i+1].append(heavy_win)
        num_dic[i+1].append(j)
        num_dic[i+1].append(-(i+1))
    ss = sorted(num_dic.items(), key = lambda item: item[1])
    ss.reverse()
    for i in ss:
        answer.append(i[0])
    return answer
