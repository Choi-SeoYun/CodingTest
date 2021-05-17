def solution(absolutes, signs):
    answer = 0
    for index,i in enumerate(signs):
        if i:
            answer += absolutes[index]
        else:
            answer -= absolutes[index]
    return answer