def solution(n, lost, reserve):
    answer = 0
    # 진짜 0벌인 사람들과 진짜 2벌인 사람들을 뽑음
    only_lost = set(lost) - set(reserve)
    only_reserve = set(reserve) - set(lost)
    
    # (진짜 2벌인 사람들)이 (진짜 0벌인 사람들)에게 옷을 나눠줄 수 있는가
    for i in sorted(only_reserve):
        if i-1 in only_lost:
            only_lost.remove(i-1)
        elif i+1 in only_lost:
            only_lost.remove(i+1)

    answer = n - len(only_lost)
            
    return answer