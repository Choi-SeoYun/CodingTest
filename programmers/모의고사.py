def solution(answers):
    answer = []
    student_1 = [1,2,3,4,5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score_1, score_2, score_3 = 0, 0, 0
    
    for index, i in enumerate(answers):
        if i == student_1[index%5]:
            score_1 += 1
        if i == student_2[index%8]:
            score_2 += 1
        if i == student_3[index%10]:
            score_3 += 1
    
    scores = [score_1, score_2, score_3]
    
    for index, score in enumerate(scores):
        if score == max(scores):
            answer.append(index+1)
            
            
    return answer