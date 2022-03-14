def solution(clothes):
    answer = 1
    clothes_dict = {}
    for i in clothes:
        if i[1] in clothes_dict:
            clothes_dict[i[1]] += 1
        else:
            clothes_dict[i[1]] = 1
            
    value = list(clothes_dict.values())
    
    for i in value:
        answer *= (i+1)
    answer -= 1
    
    return answer