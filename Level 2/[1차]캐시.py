def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    cities = [i.lower() for i in cities]
    cache = []
    
    for i in cities:
        if i in cache:
            answer += 1
            cache.remove(i)
            cache.append(i)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop(0)
                cache.append(i)
            else:
                cache.append(i)
    return answer
