from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    
    all_numbers = []
    for i in range(1, len(numbers)+1):
        all_numbers += permutations(numbers, i)
        
    new_numbers = []
    for i in all_numbers:
        new_numbers.append(int(''.join(i)))
    
    new_numbers = list(set(new_numbers))
    print(new_numbers)
    
    for n in new_numbers:
        if n >= 2:        
            k = int(n**(0.5)) + 1
            check = True
            
            for i in range(2, k):
                if n % i == 0:
                    check = False
                    break
                    
            if check:
                answer+=1

    return answer