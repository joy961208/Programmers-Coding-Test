def solution(skill, skill_trees):
    answer = len(skill_trees)

    for i in skill_trees:
        a = list(i)
        b = 0
        for j in a:
            if j in skill:
                if skill[b] != j:
                    answer -= 1
                    break
                else:
                    b += 1
    return answer
