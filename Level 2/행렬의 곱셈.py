import  numpy as np
def solution(arr1, arr2):
    answer = []
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    a = np.dot(arr1,arr2)
    return a.tolist()