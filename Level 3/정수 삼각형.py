def solution(triangle):
    answer = 0
    li = triangle[0]
    for i,j in enumerate(triangle[1:]):
        sub_li = []
        for k,v in enumerate(j):
            if k == 0:
                sub_num = li[0] + v
            elif k == len(triangle[i+1]) - 1 :
                sub_num = li[-1] + v
            else:
                sub_num = max(li[k],li[k-1]) + v
            sub_li.append(sub_num)
        li = sub_li
    return max(li)