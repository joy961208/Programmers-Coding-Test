def solution(skill, skill_trees):
    answer = len(skill_trees)

    for i in skill_trees:
        skill_tree = 0
        for j in i:
            if j in skill:
                if skill[skill_tree] != j:
                    answer -= 1
                    break
                else:
                    skill_tree += 1
    return answer
