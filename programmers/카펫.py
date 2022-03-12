def solution(brown, yellow):
    answer = []
    area = brown + yellow
    
    for h in range(1, area//2):
        if area%h == 0:
            l = area / h
            if 2*(h+l-2)==brown:
                return [l,h]
    return answer