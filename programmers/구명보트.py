def solution(people, limit):
    answer = 0
    people.sort()
    
    start = 0
    end = len(people)-1
    
    while start <= end:
        if people[start]+people[end] <= limit:
            start += 1    # 몸무게가 적은 사람도 함께 탐
        end -= 1    # 조건에 맞든 안맞든 몸무게가 큰 사람은 일단 탐
        
        answer += 1    # if문을 충족했다면 2명이 함께 탄 것이고, 아니라면 무거운 사람만 탄 것임
        
    return answer