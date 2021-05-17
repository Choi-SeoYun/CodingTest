from itertools import combinations

def solution(nums):
    answer = 0

    all_sums = list(combinations(nums, 3))
    checks = []
    for sums in all_sums:
        checks.append(sum(sums))
    
    for check in checks:
        for i in range(2, check//2+1):
            # 나눠지면 소수가 아님
            if check % i == 0:
                break
        else:
            answer += 1
    return answer