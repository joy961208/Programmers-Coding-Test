def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    nums = "0123456789abcdefghijklmnopqrstuvwxyz.-_"
    new_id = [i for i in new_id if i in nums]

    if new_id == []:
        return "aaa"

    while True:
        a = 0
        if new_id[0] == ".":
            new_id.remove(".")
            a = 1
        elif new_id[-1] == ".":
            new_id.pop()
            a = 1
        if new_id == []:
            return "aaa"
        for i,j in enumerate(new_id[:-1]):
            if j == "." and new_id[i+1] == ".":
                new_id.pop(i)
                a = 1
                break
        if a == 0:
            break

    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == ".":
            new_id.pop()

    if len(new_id) == 2:
        return new_id[0] + new_id[1]*2

    elif len(new_id) == 1:
        return new_id[0]*3

    for i in new_id:
        answer += i

    return answer