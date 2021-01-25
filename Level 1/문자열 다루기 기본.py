def solution(s):
    if len(s) == 4 or len(s) == 6 :
        for i in list(s):
            if i not in ["0","1","2","3","4","5","6","7","8","9"]:
                return False
        return True
    return False