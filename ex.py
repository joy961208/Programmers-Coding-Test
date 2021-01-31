def solution(n):
    max_ = n
    min_ = 0
    while min_ <= max_:
        a = (min_ + max_)//2
        if a*a == n:
            return (a+1) **2
        elif a*a >n:
            max_ = a-1
        else:
            min_ = a+1

    return -1