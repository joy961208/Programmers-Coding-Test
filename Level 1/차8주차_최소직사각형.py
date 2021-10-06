def solution(sizes):
    answer = 0
    width = 0
    length = 0
    for i in sizes:
        if width  < max(i):
            width = max(i)
        if length < min(i):
            length = min(i)
    return width * length
