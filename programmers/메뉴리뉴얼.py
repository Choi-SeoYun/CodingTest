from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for i in course:
        menu = []
        for order in orders:    # course에 대해서 모든 주문 다 훑음
            for li in combinations(order, i):    # combinations로 구할 수 없으면 그냥 넘어감
                # print(i, order, li)
                res = ''.join(sorted(li))
                menu.append(res)
        
        counter = Counter(menu).most_common()
        # print(counter)
        answer += [new_menu for new_menu, cnt in counter if cnt > 1 and cnt == counter[0][1]]  # counter[0][1]은 최댓값(즉, max값인 것들만 뽑아라)
            
    return sorted(answer)