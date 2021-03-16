def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []

    while truck_weights:
        if len(bridge) == bridge_length:
            bridge.pop()
        if sum(bridge) + truck_weights[0] > weight:
            bridge.insert(0,0)
        else:
            bridge.insert(0,truck_weights.pop(0))
        answer += 1
    answer += bridge_length
    return answer
