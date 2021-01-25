def solution(arr):
    answer = arr.copy()
    if len(arr) == 1:
        return [-1]
    answer.remove(min(arr))
    return answer